from django.contrib import admin
from .models import Birth_Certificate, Projects, Progress_status

# Register your models here.
class Progress_statusAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
admin.site.register(Progress_status, Progress_statusAdmin)

class Birth_CertificateAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','phone_number','ordered_on', 'Date_of_Birth')
    list_filter=("ordered_on","Date_of_Birth")
    search_fields=['first_name','last_name','e_mail_address','phone_number','Date_of_Birth']
admin.site.register(Birth_Certificate,Birth_CertificateAdmin)

class ProjectsAdmin(admin.ModelAdmin):
    list_display=('title',)
    list_filter=('title','created_on')
    search_fields=['title', 'created_on']
    prepopulated_fields={'slug':('title',)}
admin.site.register(Projects, ProjectsAdmin)
