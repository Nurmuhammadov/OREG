# Generated by Django 4.2.2 on 2023-07-14 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_faq_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='img',
        ),
    ]
