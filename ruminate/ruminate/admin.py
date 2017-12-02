from django.contrib import admin

from .models import User, Course, Office_Hour, Question

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Office_Hour)
admin.site.register(Question)