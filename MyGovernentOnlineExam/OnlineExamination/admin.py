from django.contrib import admin
from .models import Student, Exams

# Register your models here.
admin.site.site_header = "My Government Job Online Exam"
admin.site.register(Student)


class ExamModelAdmin(admin.ModelAdmin):
    list_display = ["exam_name", "no_of_ques", "total_marks", "time_duration"]


admin.site.register(Exams, ExamModelAdmin)
