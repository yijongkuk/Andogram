from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from andogram.users import models as user_models
from andogram. images import models as image_models


class Notification(models.Model):

    TYPE_CHOICES = (
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow')
    )

    from_user = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name='to_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image = models.ForeignKey(image_models.Image, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)