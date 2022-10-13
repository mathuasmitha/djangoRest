from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskStatus(models.TextChoices):
    AVAILABLE = "AVL","Available"
    NOTAVAILABLE = "NA", "NotAvailable"

class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name='Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    name = models.CharField(verbose_name=('Name'),help_text=('Required'),max_length=255)
    description = models.TextField(verbose_name=('description'),help_text=('Not Required'),blank=True)
    quantity = models.IntegerField(verbose_name=('Quantity'))
    price = models.DecimalField(verbose_name=('Regular_price'),help_text=('Maximum 999.99'),
                                error_messages={'name':{
                                    'max_length':('The price must be between 0 and 999.99')}},
                                     max_digits=5,
                                     decimal_places = 2,
                                )
    discount = models.DecimalField(verbose_name=('Discount_price'),help_text=('Maximum 999.99'),max_digits=5,decimal_places = 2,)
    slug = models.SlugField(max_length=255,blank=True)
    stock = models.IntegerField()
    imageUrl = models.URLField(null=True,blank=True)       
    status = models.CharField(choices=TaskStatus.choices,default=TaskStatus.AVAILABLE,max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    createdby=models.ForeignKey('auth.User',related_name='products',on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    cart_id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ['cart_id','-created']

    def __str__(self) -> str:
        return f'{self.cart_id}'
