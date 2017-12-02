from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    live = models.BooleanField(default=False)

    def __str__(self):
        return self.name
