from django.contrib import admin
from .models import Firma
from django import forms
from django.contrib.auth.hashers import PBKDF2PasswordHasher
# Register your models here.
hasher = PBKDF2PasswordHasher()

class FirmaCreationForm(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    

    class Meta:
        model = Firma
        fields = ('name', 'email', 'schema_name', 'paid_until', 'on_trial')

    def save(self, commit=True):
        # Save the provided password in hashed format
        firma = super().save(commit=False)
        firma.password = hasher.encode(password=self.cleaned_data["password"],
                                  salt='salt',
                                  iterations=50000)
        if commit:
            firma.save()
        return firma


class FirmaAdmin(admin.ModelAdmin):
    form = FirmaCreationForm
    list_display = ['name', 'schema_name', 'created_on']
    list_display_links = ['name', 'schema_name']

    """ 
    def save_model(self, request, obj, form, change):
        obj.password = hasher.encode(password=obj.password,
                                  salt='salt',
                                  iterations=50000)
        super().save_model(request, obj, form, change)
     """
    class Meta:
        model = Firma

admin.site.register(Firma, FirmaAdmin)
