# Generated by Django 3.2.20 on 2023-08-02 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opaque_keys.edx.django.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agreements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LTIPIISignature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_key', opaque_keys.edx.django.models.CourseKeyField(db_index=True, max_length=255)),
                ('lti_tools', models.JSONField()),
                ('lti_tools_hash', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
