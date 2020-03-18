from django.db import models

# Create your models here.


#don't forget to write important __str__ function for each
class School(models.Model):
    name=models.CharField(max_length=200)
    degree=models.CharField(max_length=100)
    start=models.DateField()
    end=models.DateField()
    marks_type=models.CharField(max_length=20)
    marks=models.FloatField()

class Skill(models.Model):
    name=models.CharField(max_length=100)
    image_path=models.CharField(max_length=100)

class Interest(models.Model):
    name=models.CharField(max_length=100)

class Achievement(models.Model):
    name=models.CharField(max_length=100)

class Experience(models.Model):
    post=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    start=models.DateField()
    end=models.DateField()

class KeyPoint(models.Model):
    experience_id=models.ForeignKey(Experience,on_delete=models.CASCADE)
    point=models.CharField(max_length=300)

class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=3000)
    repositoryLink=models.CharField(max_length=2048)

class Technology(models.Model):
    name=models.CharField(max_length=100)
    imagePath=models.CharField(max_length=2048)

class ScreenShot(models.Model):
    project_id=models.ForeignKey(Project,on_delete=models.CASCADE)
    path=models.CharField(max_length=2048)
    name=models.CharField(max_length=100)

class Video(models.Model):
    project_id=models.ForeignKey(Project,on_delete=models.CASCADE)
    path=models.CharField(max_length=2048)
    name=models.CharField(max_length=100)
