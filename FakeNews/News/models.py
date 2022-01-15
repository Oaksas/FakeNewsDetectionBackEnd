from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

#news model
class News(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    title = models.TextField()
    description = models.TextField()
    url = models.CharField(max_length=255)
    urlToImg= models.TextField()
    publishedAt=models.CharField(max_length=255)
    content=models.TextField()

    def get_absolute_url(self):
        return reverse('news_post_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['publishedAt']

        def __unicode__(self):
            return self.title



  