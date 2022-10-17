# Generated by Django 4.1 on 2022-10-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Birth_Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, null=True)),
                ('middle_name', models.CharField(max_length=250, null=True)),
                ('last_name', models.CharField(max_length=250, null=True)),
                ('ordered_on', models.DateTimeField(auto_now_add=True)),
                ('parent_identification', models.FileField(null=True, upload_to='P9s/')),
                ('Date_of_Birth', models.DateTimeField(blank=True, null=True)),
                ('e_mail_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=40, null=True)),
            ],
            options={
                'verbose_name_plural': 'Individual Returns',
                'ordering': ['-ordered_on'],
            },
        ),
    ]
