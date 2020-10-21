from django.contrib import admin
from jobsapp.models import SoftwareJobs,PharmaJobs,AgricultureJobs

# Register your models here.
class SoftwareJobsAdmin(admin.ModelAdmin):
    list_display=['id','company_name','city','vaccancy','experience','skills']

admin.site.register(SoftwareJobs, SoftwareJobsAdmin)
#-------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

class PharmaJobsAdmin(admin.ModelAdmin):
    list_display=['id','company_name','city','vaccancy','experience','skills']

admin.site.register(PharmaJobs, PharmaJobsAdmin)

#---------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------

class AgricultureJobsAdmin(admin.ModelAdmin):
    list_display=['id','company_name','city','vaccancy','experience','skills']

admin.site.register(AgricultureJobs, AgricultureJobsAdmin)
