from django.contrib import admin
from .models import Choice, Lesson, Question, Submission, Enrollment

admin.site.register(Choice)
admin.site.register(Lesson)
admin.site.register(Question)
admin.site.register(Submission)
admin.site.register(Enrollment)  # <-- ye line add karo