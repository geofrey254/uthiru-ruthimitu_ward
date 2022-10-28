from django.contrib import admin
from .models import Birth_Certificate, Projects, Progress_status, Post, Gallery, Events, Category, Downloads, Facility, Committee

# Register your models here.
class Progress_statusAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
admin.site.register(Progress_status, Progress_statusAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','status','created_on')
    list_filter=("status","created_on")
    search_fields=['title','body']
    prepopulated_fields={'slug':('title',)}
admin.site.register(Post,PostAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display=('img_title','created_on',)
    list_filter=('img_title','created_on',)
    search_fields=['img_title']
    prepopulated_fields={'slug':('img_title',)}
admin.site.register(Gallery,GalleryAdmin)

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

class EventsAdmin(admin.ModelAdmin):
    list_display=('ev_title',)
    list_filter=('ev_title', 'created_on')
    search_fields=['ev_title', 'created_on', 'ev_loc', 'ev_date']
    prepopulated_fields={'slug':('ev_title',)}
admin.site.register(Events,EventsAdmin) 

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
admin.site.register(Category,CategoryAdmin)

class DownloadsAdmin(admin.ModelAdmin):
    list_display=('d_title', 'created_on',)
    list_filter=('d_title', 'created_on',)
    search_fields=['d_title']
    prepopulated_fields={'slug':('d_title',)}
admin.site.register(Downloads,DownloadsAdmin)

# Facilities Admin Reg
class FacilityAdmin(admin.ModelAdmin):
    list_display=('fac_title', 'created_on', 'fac_availability', 'fac_price', 'fac_state')
    list_filter=('fac_title', 'created_on', 'fac_availability', 'fac_price', 'fac_state')
    search_fields=['fac_title', 'created_on', 'fac_availability', 'fac_price', 'fac_state']
admin.site.register(Facility, FacilityAdmin)

# Ward Committee Admin Reg
class CommitteeAdmin(admin.ModelAdmin):
    list_display=('name', 'role',)
    list_filter=('name', 'role')
    search_fields=['name', 'role']
admin.site.register(Committee, CommitteeAdmin)
