# Generated by Django 4.2.4 on 2023-08-22 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_newsdata_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='newsdata',
            unique_together=set(),
        ),
    ]
