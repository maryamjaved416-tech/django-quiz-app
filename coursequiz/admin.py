from django.contrib import admin
from.models import Course, Lesson, Enrollment, Question, Choice, Submission

# Inline classes
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2

# Admin classes
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'lesson', 'grade')
    inlines = [ChoiceInline]
    search_fields = ['question_text']

# Models register
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
