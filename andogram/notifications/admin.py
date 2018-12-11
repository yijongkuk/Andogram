from django.contrib import admin
from . import models


@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    
    passlist_dispaly = (
        'creator',
        'to_user',
        'notification_type'
    )