# Generated by Django 4.0.2 on 2022-02-12 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_hakkimda_onhome'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]