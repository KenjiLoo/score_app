from django.db import models

# Create your models here.
class Score(models.Model):
    user_id = models.CharField(max_length=255)
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)