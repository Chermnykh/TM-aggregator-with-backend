# Generated by Django 4.0.4 on 2022-06-04 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('time_management', '0005_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timer_time_1', models.IntegerField(default=10)),
                ('timer_time_2', models.IntegerField(default=10)),
                ('timer_time_3', models.IntegerField(default=10)),
                ('timer_time_4', models.IntegerField(default=10)),
                ('timer_time_5', models.IntegerField(default=10)),
                ('timer_time_6', models.IntegerField(default=10)),
                ('timer_time_7', models.IntegerField(default=10)),
                ('timer_time_8', models.IntegerField(default=10)),
                ('timer_time_max_1', models.IntegerField(default=10)),
                ('timer_time_max_2', models.IntegerField(default=10)),
                ('timer_time_max_3', models.IntegerField(default=10)),
                ('timer_time_max_4', models.IntegerField(default=10)),
                ('timer_time_max_5', models.IntegerField(default=10)),
                ('timer_time_max_6', models.IntegerField(default=10)),
                ('timer_time_max_7', models.IntegerField(default=10)),
                ('timer_time_max_8', models.IntegerField(default=10)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
