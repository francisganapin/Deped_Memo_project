from django.db import models



class MemoTable(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    reference_data = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    recent = models.BooleanField(default=True)  
    file = models.FileField(upload_to='pdf/')

  
    class Meta:
        dn_table = 'memo_table'