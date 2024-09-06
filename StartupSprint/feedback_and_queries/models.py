from django.db import models

class FeedBack(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=50)
    ratings = models.FloatField(default=0.0)
    feedback_text = models.TextField()

class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

class Queries(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=250)
    query = models.TextField()
    answer = models.TextField(blank=True, null=True)
    question_date = models.DateTimeField(auto_now_add=True)