# Generated by Django 4.2.4 on 2023-08-23 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_newsdata_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='newsdata',
            unique_together={('time',)},
        ),
    ]
