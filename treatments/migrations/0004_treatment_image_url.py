# Generated by Django 3.2 on 2021-04-25 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0003_treatment_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
