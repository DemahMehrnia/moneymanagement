# Generated by Django 4.0.3 on 2022-03-02 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymoudles', '0008_outro_fordebt'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
