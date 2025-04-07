from django.db import models



class MemoTable(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    reference_data = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)  
    recent = models.BooleanField(default=True)  
    file = models.FileField(upload_to='pdf/')

  