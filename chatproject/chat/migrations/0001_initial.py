# Generated by Django 5.0.6 on 2024-05-23 21:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('has_been_seen', models.BooleanField(default=False)),
                ('from_who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_from', to=settings.AUTH_USER_MODEL)),
                ('to_who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
