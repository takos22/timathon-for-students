from django.db import models
from django.utils.timezone import now

class Homework(models.Model):
    subject = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    description = models.TextField()
    added_date = models.DateTimeField(default=now)
    due_date = models.DateTimeField()
    finished = models.BooleanField(default=False)

    def __repr__(self):
        return "<Homework id={0.id} subject={0.subject} name={0.name}>"
