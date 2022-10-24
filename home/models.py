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


class Progress_status(models.Model):
    title = models.CharField(max_length=20, unique=True, null=True)
    slug = models.SlugField(max_length=250, unique=True, null=True)

    class Meta:
        verbose_name_plural = 'progress_status'

    def get_absolute_url(self):
        return reverse('blog_category', args=[self.slug])

    def __str__(self):
        return self.title

# Projects Model
class Projects(models.Model):
    title = models.CharField(max_length=255, unique=True)
    proj_img = models.ImageField(upload_to="proj_pics/", null=True)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=2000, null=True, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    progress_status  =   models.ManyToManyField(Progress_status, related_name='projects')

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural =   'Projects'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.proj_img = self.compressImage(self.proj_img)
        super(Projects, self).save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def compressImage(self,proj_img):
        imageTemporary  =   Image.open(proj_img)
        outputIOStream  =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        proj_img    =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % proj_img.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return proj_img

# Blog Page Models
class Post(models.Model):
    title       =   models.CharField(max_length=255, unique=True)
    blog_img    =   models.ImageField(upload_to="blog_pics/", null=True, blank=True)
    slug        =   models.SlugField(max_length=250, null=True, blank=True, unique=True)
    author      =   models.CharField(max_length=100, default='Admin')
    updated_on  =   models.DateTimeField(auto_now=True)
    body        =   tinymce_models.HTMLField()
    created_on  =   models.DateTimeField(auto_now_add=True)
    status      =   models.IntegerField(choices=STATUS, default=0)


    class Meta:
        ordering    =   ['-created_on']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article-detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.blog_img   =   self.compressImage(self.blog_img)
        super(Post, self).save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def compressImage(self,blog_img):
        imageTemporary  =   Image.open(blog_img)
        outputIOStream  =   BytesIO()
        imageTemporaryResized   =   imageTemporary.resize((1020,573))
        imageTemporary.save(outputIOStream, format='JPEG', quality=60)
        outputIOStream.seek(0)
        blog_img    =   InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % blog_img.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
        return blog_img


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
