# Generated by Django 4.1.5 on 2023-03-10 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_remove_report_display_remove_reportimage_display_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='cover',
            field=models.ImageField(default='Images/None/image_default.png', upload_to='Images/'),
        ),
    ]
