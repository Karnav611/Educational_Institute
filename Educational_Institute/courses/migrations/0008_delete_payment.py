# Generated by Django 3.1.6 on 2021-03-18 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_payment_usercourse'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]