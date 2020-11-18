from _ast import mod

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return super().__str__()


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    mark = models.IntegerField()
    title = models.CharField(max_length=100)


class Answer(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()


class Image(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    cellType = models.CharField(max_length=50)
    component = models.CharField(max_length=50)
    description = models.TextField()
    doi = models.CharField(max_length=100)
    mode = models.CharField(max_length=100)
    name = models.ImageField(upload_to="images")
    organism = models.CharField(max_length=50)


class QuizUser(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
