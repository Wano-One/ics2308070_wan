# Generated by Django 5.1 on 2024-08-26 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_phone',
            field=models.IntegerField(),
        ),
    ]
