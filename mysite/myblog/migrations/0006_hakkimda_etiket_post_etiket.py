# Generated by Django 4.0.2 on 2022-02-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_alter_hakkimda_content_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='hakkimda',
            name='etiket',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='etiket',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]