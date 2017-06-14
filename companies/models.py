from django.core.validators import RegexValidator
from django.db import models
from django import forms


class Company(models.Model):
    company_name = models.CharField(max_length=50)
    creation_date = models.DateTimeField('date added', auto_now_add=True)
    update_date = models.DateTimeField('date updated', auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='companies', on_delete=models.CASCADE)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: "
                                                                   "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=20, validators=[phone_regex], blank=True)
    address_line1 = models.CharField("Address line 1", max_length=45, default="address")
    address_line2 = models.CharField("Address line 2", max_length=45,
                                     blank=True)
    postal_code = models.CharField("Postal Code", max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state_province = models.CharField("State/Province", max_length=40,
                                      blank=True)
    country_code = models.CharField("Country Code", max_length=10, blank=True, null=True)

    def __str__(self):
        return '%s@user:%s' % (self.company_name, self.owner)


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['creation_date', 'update_date', 'owner']
