# Generated by Django 5.1 on 2024-09-04 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0006_remove_book_stud_satus_student_stud_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
        ),
    ]
