from django.db import models
from django.contrib.auth.models import User, Group

class Exam(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    date = models.DateTimeField(verbose_name="Дата проведения")
    image = models.ImageField(upload_to='exams/', verbose_name="Картинка", blank=True, null=True)
    users = models.ManyToManyField(User, related_name='exams', verbose_name="Пользователи", blank=True)
    groups = models.ManyToManyField(Group, related_name='exams', verbose_name="Группы", blank=True)
    is_public = models.BooleanField(default=False, verbose_name="Опубликован")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Экзамен"
        verbose_name_plural = "Экзамены"
