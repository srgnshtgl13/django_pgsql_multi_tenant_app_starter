from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ObjectDoesNotExist
from tenant_schemas.middleware import BaseTenantMiddleware
from tenant_schemas.utils import get_public_schema_name


class SchemaMiddleware(BaseTenantMiddleware):

    def get_tenant(self, model, hostname, request):
        try:
            public_schema = model.objects.get(schema_name=get_public_schema_name())
        except ObjectDoesNotExist:
            public_schema = model.objects.create(
                domain_url=hostname,
                schema_name=get_public_schema_name(),
                tenant_name=get_public_schema_name().capitalize(),
                paid_until=date.today() + relativedelta(months=+1),
                on_trial=True)
        public_schema.save()
        user = request.user
        if user.is_anonymous or user.is_superuser:
            return public_schema
        if user:
            tenant_model = model.objects.get(tenant_uuid=user.client.tenant_uuid)
            return tenant_model if not None else public_schema
        return public_schema


class CorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"

        return response