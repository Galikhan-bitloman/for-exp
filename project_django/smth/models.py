from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length= 200)
    date = models.DateTimeField('date published')
   
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Number(models.Model):
    name_people = models.CharField("Name", max_length=30)
    people_number = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name_people
        
