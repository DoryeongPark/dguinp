from django.db import models
from django.conf import settings
from django.utils import timezone
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields

class Detail(summer_model.Attachment):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    issue = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class_detail=summer_fields.SummernoteTextField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Detail)
    comment = models.TextField()


