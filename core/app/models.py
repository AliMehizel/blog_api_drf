from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
import re

article_category = [
    ('TECHNOLOGY','TECHNOLOGY'),  
    ('FOOD','FOOD'), 
    ('TRAVEL','TRAVEL') 
]



class User(AbstractUser):
    slug = models.SlugField(auto_created=True, unique=True,null=True)
    avatar = models.ImageField(upload_to='image/AVATAR/', default='image/avatar.png')
    
    
    def __str__(self):
        return self.slug

@receiver(pre_save, sender=User)
def generate_slug(sender, instance, **kwargs):
    if not instance.slug:
        slug_line = slugify(f'{instance.username}@youcant__@5426698463333')
        new_slug = re.sub(r'[^a-zA-Z0-9_-]', '', slug_line)
        instance.slug = new_slug
        
class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, blank=True,null=True)
    content = models.TextField(max_length=5000, blank=True,null=True)
    category = models.CharField(choices=article_category, max_length=100,blank=True,null=True)
    date_pub = models.DateField(auto_now=False, auto_now_add=True)
    image_art = models.ImageField(upload_to='images/', blank=True,null=True)
    
    
    
    def __str__(self):
        return self.title 
    
    
    

    
    
class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    article = models.ForeignKey(Article, related_name='rating',on_delete=models.CASCADE,null=True)
    count = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    
    
    def __str__(self):
        return str(self.id)
    
    
    @property
    def get_rate_total(self):
        total = sum([i for i in self.count])
        return total
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    article = models.ForeignKey("Article" ,on_delete=models.CASCADE,null=True)
    context = models.TextField(max_length=1000,blank=True)
    add_on =  models.DateField(auto_now=True, auto_now_add=False)
    
    
    
    def __str__(self):
        return str(self.id)
    
