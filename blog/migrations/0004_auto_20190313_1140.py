# Generated by Django 2.1.7 on 2019-03-13 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='update',
            new_name='updated',
        ),
    ]
