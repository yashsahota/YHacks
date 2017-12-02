from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    course_teaching =
    course_enrolled = 

    def __str__(self):
        return self.name

class Office_Hours(models.Model):

	course_listing = models.ForeignKey(Course)
	start_time = models.DateTimeField()
