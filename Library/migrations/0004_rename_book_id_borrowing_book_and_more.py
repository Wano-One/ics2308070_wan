# Generated by Django 5.1 on 2024-08-27 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0003_alter_student_student_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowing',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='borrowing',
            old_name='student_id',
            new_name='student',
        ),
    ]
