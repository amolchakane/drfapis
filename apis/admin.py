from django.contrib import admin

from apis import models

admin.site.register(models.UserProfile)
admin.site.register(models.Content)
