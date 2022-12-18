from django.db import models


# Create your models here.

class Reporter(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=64)


    def __str__(self):
        return f"Obeject_name: {self.id}, {self.first_name}, {self.last_name}, {self.email}, {self.password}"


class Article(models.Model):
    title = models.TextField()
    body = models.TextField()
    reporter_details = models.ForeignKey("Reporter", related_name="posted_reporter", on_delete=models.CASCADE)
    created_on = models.DateField()
    article_image = models.ImageField(upload_to="media/", default=None)
    article_category = models.CharField(max_length=64, null=True)
