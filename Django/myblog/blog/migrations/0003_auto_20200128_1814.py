# Generated by Django 2.2.6 on 2020-01-28 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_pud_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='pud_time',
            new_name='pub_time',
        ),
    ]
