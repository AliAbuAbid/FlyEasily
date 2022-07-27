from django.contrib import admin

from Workers.models import Workersorders,report

# Register your models here.


admin.site.register(Workersorders,admin.ModelAdmin)
admin.site.register(report,admin.ModelAdmin)

