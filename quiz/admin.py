from django.contrib import admin
from .models import Lesson, Question, Choice, Submission

admin.site.register(Lesson)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site_header = "OnlineCourse Admin"