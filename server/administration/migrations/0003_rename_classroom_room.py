# Generated by Django 4.1.1 on 2023-02-04 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_classroom_committee_alter_faculty_id_events_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Classroom',
            new_name='Room',
        ),
    ]