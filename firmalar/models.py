from django.db import models
from django.utils.text import slugify
from account.models import MyUser
# Create your models here.

from tenant_schemas.models import TenantMixin

class Firma(TenantMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(
        max_length=255,
        unique=True
    )
    password = models.CharField(max_length=100)
    paid_until =  models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

    def save(self, verbosity=1, *args, **kwargs):
        # call the real save method
        super(Firma,self).save(verbosity=verbosity, *args, **kwargs)
        # create a user for firma
        if self.pk is not None:
            firma_user = MyUser(first_name=self.name, email=self.email,password=self.password, firma_id=self.pk)
            firma_user.save()

    def get_name(self):
        return self.name