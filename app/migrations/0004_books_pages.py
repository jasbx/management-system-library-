# Generated by Django 5.0.1 on 2024-05-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_books_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='pages',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
