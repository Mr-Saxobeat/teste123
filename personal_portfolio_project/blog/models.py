from django.db import models
from datetime import date

class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField(default=date.today)
    description = models.TextField()

    def __str__(self):
        return self.title
