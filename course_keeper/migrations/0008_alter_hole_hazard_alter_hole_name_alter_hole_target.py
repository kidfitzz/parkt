# Generated by Django 4.1.3 on 2022-11-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_keeper', '0007_alter_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hole',
            name='hazard',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hole',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='hole',
            name='target',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
