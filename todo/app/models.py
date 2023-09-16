from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.name
