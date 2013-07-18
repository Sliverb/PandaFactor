from django.contrib import admin
from RegisterBusiness.models import Business, Job

class JobInline(admin.TabularInline):
    model = Job
    extra = 1

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
      (None,           {'fields': ['name']}),
      ('Contact Info', {'fields': ['email']}),
    ]
    inlines = [JobInline]

admin.site.register(Business, PollAdmin)
admin.site.register(Job)