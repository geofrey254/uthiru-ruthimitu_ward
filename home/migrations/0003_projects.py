# Generated by Django 4.1 on 2022-10-23 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_birth_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('proj_img', models.ImageField(null=True, upload_to='proj_pics/')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=2000, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('progress', models.IntegerField(choices=[(0, 'In Progress'), (1, 'Complete')], default=0)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
