# Generated by Django 3.2 on 2021-04-29 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='username',
            field=models.CharField(blank=True, default=False, max_length=30, null=True),
        ),
    ]