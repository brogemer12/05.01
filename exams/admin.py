from django.contrib import admin
from .models import Exam

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_public')
    list_filter = ('is_public', 'date')
    search_fields = ('title',)
    filter_horizontal = ('users',)
