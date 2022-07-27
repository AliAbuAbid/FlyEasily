from django.contrib import admin

from Managers.models import schedule,managerreport,passengerfiless,news

# Register your models here.


admin.site.register(schedule,admin.ModelAdmin)
admin.site.register(managerreport,admin.ModelAdmin)
admin.site.register(passengerfiless,admin.ModelAdmin)
admin.site.register(news,admin.ModelAdmin)


