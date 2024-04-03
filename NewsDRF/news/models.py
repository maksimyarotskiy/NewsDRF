from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    source = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

