from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title
