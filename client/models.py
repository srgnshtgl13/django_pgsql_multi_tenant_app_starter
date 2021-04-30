import uuid
import os
from django.db import models
from django.utils.text import slugify

from tenant_schemas.models import TenantMixin

def generate_unique_schema(credentials):
    name, model = credentials
    generated_schema_name = slugify(name.replace("ı","i")).replace("-","_")
    unique_schema_name = generated_schema_name
    counter = 1
    while model.objects.filter(schema_name=unique_schema_name).exists():
        unique_schema_name = f"{unique_schema_name}_{counter}"
        counter+=1
    return f"schm_{unique_schema_name}"

class Client(TenantMixin):
    REQUIRED_FIELDS = ('tenant_name', 'paid_until', 'on_trial')
    tenant_name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    tenant_uuid = models.UUIDField(default=uuid.uuid4, null=False, blank=False)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)
    domain_url = models.URLField(blank=True, null=True, default=os.getenv('DOMAIN'))

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

    def save(self, *args, **kwargs):
        if not self.schema_name:
            self.schema_name = generate_unique_schema((self.tenant_name, Client))
        super(Client,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.tenant_name