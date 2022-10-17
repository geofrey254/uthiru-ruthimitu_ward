import sys
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse
from tinymce import models as tinymce_models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.template.defaultfilters import slugify

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

TYPE = (
    (0, "None"),
    (1, "Featured"),
    (2, "Trending")
)

LABEL = (
    (0, "None"),
    (1, "Trending")
)


class Category(models.Model):
    title = models.CharField(max_length=20, unique=True, null=True)
    slug = models.SlugField(max_length=250, unique=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('blog_category', args=[self.slug])

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255, unique=True)
    blog_img = models.ImageField(upload_to="news_pics/", null=True, blank=True)
    img_credits = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    author = models.CharField(max_length=100, default='Admin')
    updated_on = models.DateTimeField(auto_now=True)
    body = tinymce_models.HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    blog_type = models.IntegerField(choices=TYPE, default=0)
    categories = models.ManyToManyField(Category, related_name='posts')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.id:
            self.blog_img = self.compressImage(self.blog_img)
        super(News, self).save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

# Individual Returns Model Structure


class Birth_Certificate(models.Model):
    first_name = models.CharField(max_length=250, null=True)
    middle_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    ordered_on = models.DateTimeField(auto_now_add=True)
    parent_identification = models.FileField(upload_to="P9s/", null=True)
    Date_of_Birth = models.DateTimeField(null=True, blank=True)
    e_mail_address = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=40, null=True)

    class Meta:
        ordering = ['-ordered_on']
        verbose_name_plural = 'Individual Returns'

    def __str__(self):
        return self.first_name + self.last_name

    def file_link(self):
        if self.parent_identification:
            return "<a href='%s'>download</a>" % (self.parent_identification.url,)
        else:
            return "No attachment"
    file_link.allow_tags = True
    file_link.short_description = 'File Download'
