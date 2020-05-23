import django
from django.conf import settings
from django.core.exceptions import DisallowedHost
from django.db import connection
from django.http import Http404
from tenant_schemas.utils import (
    get_public_schema_name,
    get_tenant_model,
    remove_www,
)


"""
These middlewares should be placed at the very top of the middleware stack.
Selects the proper database schema using request information. Can fail in
various ways which is better than corrupting or revealing data.
Extend BaseTenantMiddleware for a custom tenant selection strategy,
such as inspecting the header, or extracting it from some OAuth token.
"""


class BaseTenantMiddleware(django.utils.deprecation.MiddlewareMixin):
    TENANT_NOT_FOUND_EXCEPTION = Http404

    """
    Subclass and override  this to achieve desired behaviour. Given a
    request, return the tenant to use. Tenant should be an instance
    of TENANT_MODEL. We have three parameters for backwards compatibility
    (the request would be enough).
    """

    def get_tenant(self, model, firma_id, request):
        raise NotImplementedError

    def user_from_request(self, request):
        """ Extracts hostname from request. Used for custom requests filtering.
            By default removes the request's port and common prefixes.
        """
        if request.user.is_authenticated:
            return request.user

    def process_request(self, request):
        if not request.user.is_authenticated:
            pass
            return
        # Connection needs first to be at the public schema, as this is where
        # the tenant metadata is stored.
        if request.user.is_superuser:
            connection.set_schema_to_public()
            return
        connection.set_schema_to_public()
        
        firma_id = self.user_from_request(request).firma_id
        TenantModel = get_tenant_model()

        try:
            # get_tenant must be implemented by extending this class.
            tenant = self.get_tenant(TenantModel, firma_id, request)
            assert isinstance(tenant, TenantModel)
        except TenantModel.DoesNotExist:
            raise self.TENANT_NOT_FOUND_EXCEPTION(
                "No tenant for {!r}".format(request.get_host())
            )
        except AssertionError:
            raise self.TENANT_NOT_FOUND_EXCEPTION(
                "Invalid tenant {!r}".format(request.tenant)
            )

        request.tenant = tenant
        connection.set_tenant(request.tenant)

        # Do we have a public-specific urlconf?
        if (
            hasattr(settings, "PUBLIC_SCHEMA_URLCONF")
            and request.tenant.schema_name == get_public_schema_name()
        ):
            request.urlconf = settings.PUBLIC_SCHEMA_URLCONF


class TenantMiddleware(BaseTenantMiddleware):
    """
    Selects the proper database schema using the request host. E.g. <my_tenant>.<my_domain>
    """

    def get_tenant(self, model, firma_id, request):
        return model.objects.get(id=firma_id)


""" def get_user(request):
    if request.user.is_authenticated:
        firma = Firma.objects.get(id=request.user.firma_id)
        return firma.schema_name """