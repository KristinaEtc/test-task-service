from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default='project is awesome')
    def __str__(self):
        return self.title

class Task(models.Model):
    assigned_to = models.ForeignKey('auth.User', related_name='assigned', on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, null=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    due_date = models.DateField()
    #is_complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['-due_date']

    def __str__(self):
        return self.title