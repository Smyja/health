# Generated by Django 3.1 on 2020-08-14 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('username', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('signup_confirmation', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, null=True)),
                ('margin', models.FloatField(default=20, null=True)),
                ('amount', models.FloatField(default=20, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('phonenumber', models.CharField(max_length=20, null=True)),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
                ('appointment_with', models.ManyToManyField(blank=True, related_name='appontment_with', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('book', 'book'), ('approved', 'approved')], default='none', max_length=50)),
                ('hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hospital', to='core.profile')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patientt', to='core.profile')),
            ],
        ),
    ]
