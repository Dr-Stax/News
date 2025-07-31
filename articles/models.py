from django.db import models
from django.conf import settings
from django.urls import reverse

class Articles(models.Model):
    title = models.CharField(max_length=29)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("Articles_detail", kwargs={"pk": self.pk})
# Create your models here.


class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
    
    def get_absolute_url():
        return reverse('article_list')