from django.contrib import admin
from .models import Birth_Certificate

# Register your models here.
class Birth_CertificateAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','phone_number','ordered_on', 'Date_of_Birth')
    list_filter=("ordered_on","Date_of_Birth")
    search_fields=['first_name','last_name','e_mail_address','phone_number','Date_of_Birth']
admin.site.register(Birth_Certificate,Birth_CertificateAdmin)
