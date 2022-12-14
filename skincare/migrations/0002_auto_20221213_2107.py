# Generated by Django 3.2 on 2022-12-13 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skincare', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skincare',
            name='skin_concern',
        ),
        migrations.AddField(
            model_name='skincare',
            name='skin_concern',
            field=models.ManyToManyField(to='skincare.SkinConcern'),
        ),
        migrations.RemoveField(
            model_name='skincare',
            name='skin_type',
        ),
        migrations.AddField(
            model_name='skincare',
            name='skin_type',
            field=models.ManyToManyField(to='skincare.SkinType'),
        ),
    ]
