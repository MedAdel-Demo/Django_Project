from django.contrib import admin
from . import models
# Register your models here.

class DemocranceAdmin (admin.ModelAdmin):
    pass

admin.site.register(models.Customer, DemocranceAdmin)
admin.site.register(models.Policy, DemocranceAdmin)
admin.site.register(models.Policy_State, DemocranceAdmin)
admin.site.register(models.Policy_Type, DemocranceAdmin)

admin.site.register(models.Policy_History, DemocranceAdmin)