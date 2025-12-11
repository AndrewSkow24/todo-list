from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    completed = models.BooleanField(default=False, verbose_name="Статус выполнения")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    def __str__(self):
        return f"Задача: '{self.title}'"

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи "
