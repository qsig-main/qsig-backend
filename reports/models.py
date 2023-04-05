from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Report(models.Model):
    # user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    # user = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    pdf = models.FileField(upload_to='Pdfs/', default='Pdfs/None/pdf_default.pdf')
    order = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    do_not_display = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='Images/', default='Images/None/image_default.png')

    def __str__(self):
        return """user: %s | title: %s
        """%(self.user, self.title)

class ReportImage(models.Model):
    # user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='Images/', default='Images/None/image_default.png')
    order = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    do_not_display = models.BooleanField(default=False)

    def __str__(self):
        return  """title: %s"""%(self.title)
