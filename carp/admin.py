from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.book),
admin.site.register(models.activity),
admin.site.register(models.notification)
admin.site.register(models.album)
