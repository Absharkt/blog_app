# Generated by Django 4.2.1 on 2023-06-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_user', '0003_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='blog_user.profile'),
        ),
        migrations.DeleteModel(
            name='Friends',
        ),
    ]
