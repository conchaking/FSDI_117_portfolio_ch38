from django.db import models

# Create your models here.
class TechnologySkill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Experience(models.Model):
    entity = models.CharField(max_length=225)
    title = models.CharField(max_length=225)
    description = models.TextField(max_length=500)
    period = models.CharField(max_length=100)
    technologiesSkills = models.ManyToManyField(TechnologySkill)

    def __str__(self):
        return f"{self.entity} - {self.title} ({self.period})"