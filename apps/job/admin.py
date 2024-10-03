from django.contrib import admin

from apps.job.models import JobAnnounce, JobTechnology, JobLocation


class JobTechnologyInline(admin.TabularInline):
    model = JobTechnology
    extra = 0

@admin.register(JobAnnounce)
class JobAnnounceAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'price', 'price_measure', 'level', 'payment_verified')
    inlines = (JobTechnologyInline,)


@admin.register(JobTechnology)
class JobTechnologyAdmin(admin.ModelAdmin):
    list_display = ('technology', 'job', 'level')

@admin.register(JobLocation)
class JobLocationAdmin(admin.ModelAdmin):
    pass