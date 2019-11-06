from django.db import models
import pandas as pd
import re

class Recon(models.Model):
    document = models.FileField(upload_to='recon/')
    image= models.ImageField()
    

# Create your models here.