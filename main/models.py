from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField("Date published")
    body = models.TextField()


    def __str__(self):
        return self.title