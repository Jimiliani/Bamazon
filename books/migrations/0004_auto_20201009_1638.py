# Generated by Django 3.1.2 on 2020-10-09 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
