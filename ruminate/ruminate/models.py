from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
    	return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    course_teaching = models.ManyToManyField(Course, related_name='+', blank=True)
    course_enrolled = models.ManyToManyField(Course, related_name='+', blank=True)

    def __str__(self):
        return self.name

class Office_Hour(models.Model):
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False)

    course = models.ForeignKey(Course)
    teaching_assistant = models.ForeignKey(User)
    is_live = models.BooleanField(default=False)

    def __str__(self):
        return (str(self.course) + "    " + str(self.start_time) + "    " + str(self.teaching_assistant))

class Question(models.Model):
    office_hour = models.ForeignKey(Office_Hour) 

    content = models.CharField(max_length=1024)
    time_created = models.DateTimeField(auto_now=True, auto_now_add=False)
 
    is_answered = models.BooleanField(default=False)






