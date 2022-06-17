from cgitb import text
from django.db import models
get_user_model
User=get_user_model()
# Create your models here
title = models.CharField(('title'), max_length=200)
text = models.TextField()
author = models.ForeignKey(User,on_delete=models.CASCADE)
date_created = models.DateTimeField()
date_published = models.DateTimeField()
