# Generated by Django 3.1 on 2023-12-23 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_numer',
            new_name='order_number',
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
