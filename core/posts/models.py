from django.db import models


class Forum(models.Model):

    author = models.CharField(max_length=100,verbose_name='Author')

    title = models.CharField(max_length=100,verbose_name='Title')
    content = models.TextField(max_length=100,verbose_name='Content')

    active = models.BooleanField(default=True,verbose_name='Active Status')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Forums'
        ordering = ['-created','-updated']

    
