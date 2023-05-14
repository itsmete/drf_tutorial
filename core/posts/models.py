from django.db import models



class ForumUser(models.Model):
    username = models.CharField(max_length=50,blank=False,unique=True)
    name = models.CharField(max_length=100,blank=True)
    lastname = models.CharField(max_length=100,blank=True)
    bio = models.TextField(max_length=512,blank=True)

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = 'Forum User'
        verbose_name_plural =  'Forum Users'


class Forum(models.Model):

    author = models.ForeignKey(to=ForumUser , on_delete=models.CASCADE,related_name='forums')

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

    
