# Generated by Django 4.2.4 on 2023-08-23 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_newsdata_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='newsdata',
            unique_together={('title', 'time')},
        ),
    ]