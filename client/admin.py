from django.contrib import admin
from .models import Client



class ClientAdmin(admin.ModelAdmin):
    list_display = ['tenant_name', 'tenant_uuid', 'schema_name', 'created_on']
    list_display_links = ['tenant_name', 'schema_name']
    readonly_fields = ['schema_name', 'tenant_uuid']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('tenant_name', 'paid_until', 'on_trial', 'domain_url'),
        }),
    )
    class Meta:
        model = Client


admin.site.register(Client, ClientAdmin)