# Generated by Django 4.2.15 on 2024-08-31 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_posted']},
        ),
    ]
