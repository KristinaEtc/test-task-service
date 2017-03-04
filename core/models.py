from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default='project is awesome')
    def __str__(self):
        return self.title

    #project = models.ForeignKey(Project)
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    due_date = models.DateField()
    #is_complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['-due_date']

    def __str__(self):
        return self.title
