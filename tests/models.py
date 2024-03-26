from django.db import models

import uuid

class Basemodel(models.Model):
    create_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Category(Basemodel):
    cetagory_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.cetagory_name

class Question(Basemodel):
    category = models.ForeignKey(Category, related_name='category',on_delete = models.CASCADE)
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.question

class Answer(Basemodel):
    question = models.ForeignKey(Question, related_name='question_answer',on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer



