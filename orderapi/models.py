from django.db import models

# Create your models here.
class Category (models.Model):

    name = models.CharField(max_length=150, db_index=True)
    
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
        
class Product (models.Model):
    category = models.ForeignKey(Category, related_name='eateries', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100, db_index=True)
    
    price = models.DecimalField(decimal_places=0, max_digits=5)
    
    available = models.BooleanField(default=True)
    description = models.TextField(max_length=20000,blank=True,default="product is good")
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    image = models.URLField()
    
    def __str__(self):
        return self.name
        

    
    