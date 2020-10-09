# Generated by Django 3.1.2 on 2020-10-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='book',
            name='length',
            field=models.IntegerField(default=250),
            preserve_default=False,
        ),
    ]
