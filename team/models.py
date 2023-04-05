from django.db import models

YEAR_CHOICES = (
    ('1st Year', '1st Year'),
    ('2nd Year', '2nd Year'),
    ('3rd Year', '3rd Year'),
    ('4th Year', '4th Year'),
    ('Undergraduate', 'Undergraduate'),
    ('Graduate', 'Graduate'),
    ('Alumni', 'Alumni'),
)

VERTICAL_CHOICES = (
    ('Investments Team', 'Investments Team'),
    ('Industrials', 'Industrials'),
    ('Technology, Media & Telecom', 'Technology, Media & Telecom'),
    ('Consumers & Healthcare', 'Consumers & Healthcare'),
    ('Energy & Commodities', 'Energy & Commodities'),
    ('Finance, Insurance & Real Estate', 'Finance, Insurance & Real Estate'),
    ('Market & Trends', 'Market & Trends'),
    ('Analytics', 'Analytics'),
)

POSITION_CHOICES = (
    ('No Display', 'No Display'),
    ('Co-Chair', 'Co-Chair'),
    ('PM/Director', 'PM/Director'),
    ('Senior Investment Analyst', 'Senior Investment Analyst'),
    ('Junior Investment Analyst', 'Junior Investment Analyst'),
    ('Team Photo', 'Team Photo'),
)

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=30, choices=POSITION_CHOICES, default='No Display')
    headshot = models.ImageField(upload_to='Headshots/', default='Headshots/None/headshot_default.jpeg')
    year = models.CharField(max_length=15, choices=YEAR_CHOICES, default='Undergraduate', null=True, blank=True)
    vertical = models.CharField(max_length=100, choices=VERTICAL_CHOICES, default='', null=True, blank=True)
    custom_vertical = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=250, blank=True, null=True)
    LinkedIn = models.URLField(max_length=250, blank=True, null=True)
    order = models.IntegerField(default=0)
    do_not_display = models.BooleanField(default=False)







