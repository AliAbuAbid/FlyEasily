from django.contrib import admin

from Passengers.models import passengers,Passengerorders,ratings

# Register your models here.


admin.site.register(passengers,admin.ModelAdmin)
admin.site.register(Passengerorders,admin.ModelAdmin)
admin.site.register(ratings,admin.ModelAdmin)
