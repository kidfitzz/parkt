# Generated by Django 4.1.3 on 2022-11-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_keeper', '0006_course_location_course_user_alter_course_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
