# Generated by Django 3.0.7 on 2020-08-03 17:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_auto_20200803_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_with',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='hospitals',
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('book', 'book'), ('approved', 'approved')], default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='appointment_with',
            field=models.ManyToManyField(blank=True, related_name='appointment_with', to=settings.AUTH_USER_MODEL),
        ),
    ]