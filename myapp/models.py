from django.db import models
 
# Create your models here.
class item(models.Model):          # 追加
    code = models.IntegerField()   # 追加
    name = models.TextField()      # 追加
    price = models.IntegerField()  # 追加