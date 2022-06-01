from django.db import models

# модуль формы для связи с бд
class Form(models.Model):
    name = models.CharField(max_length=35)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=35)
# возвращает в название в админке ебейл
    def __str__(self):
        return self.email
# обяз класс для названия строк бд  с админки
    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'


