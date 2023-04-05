# Generated by Django 4.1.5 on 2023-03-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_rename_linked_in_member_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='position',
            field=models.CharField(blank=True, choices=[('Co-Chair', 'Co-Chair'), ('Executive', 'Executive'), ('Senior Investment Analyst', 'Senior Investment Analyst'), ('Junior Investment Analyst', 'Junior Investment Analyst')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='vertical',
            field=models.CharField(blank=True, choices=[('Industrials', 'Industrials'), ('Technology, Media & Telecom', 'Technology, Media & Telecom'), ('Consumers & Healthcare', 'Consumers & Healthcare'), ('Energy & Commodities', 'Energy & Commodities'), ('Finance, Insurance & Real Estate', 'Finance, Insurance & Real Estate'), ('Market & Trends', 'Market & Trends'), ('Analytics', 'Analytics'), ('Commodities', 'Commodities'), ('Consumers', 'Consumers'), ('Energy', 'Energy'), ('Finance', 'Finance'), ('Healthcare', 'Healthcare'), ('Insurance', 'Insurance'), ('Market', 'Market'), ('Media', 'Media'), ('Real Estate', 'Real Estate'), ('Technology', 'Technology'), ('Telecom', 'Telecom'), ('Trends', 'Trends')], default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='year',
            field=models.CharField(blank=True, choices=[('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year'), ('Undergraduate', 'Undergraduate'), ('Graduate', 'Graduate'), ('Alumni', 'Alumni')], default='Undergraduate', max_length=15, null=True),
        ),
    ]
