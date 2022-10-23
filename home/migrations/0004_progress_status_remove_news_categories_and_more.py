# Generated by Django 4.1 on 2022-10-23 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True, unique=True)),
                ('slug', models.SlugField(max_length=250, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'progress_status',
            },
        ),
        migrations.RemoveField(
            model_name='news',
            name='categories',
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'Projects'},
        ),
        migrations.RemoveField(
            model_name='projects',
            name='progress',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.AddField(
            model_name='projects',
            name='progress_status',
            field=models.ManyToManyField(related_name='projects', to='home.progress_status'),
        ),
    ]
