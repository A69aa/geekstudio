# Generated by Django 4.0.4 on 2022-05-01 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='password',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='userProfile',
        ),
    ]
