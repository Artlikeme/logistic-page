from django.db import models

class Articles(models.Model):
    title = models.CharField('Name',max_length=35, default='New Article')
    anons = models.TextField('Anons',max_length=250)
    article_info = models.TextField('Article')
    full_text = models.TextField('Full text')
    
    date = models.DateTimeField('Date of publication')

    def  __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'