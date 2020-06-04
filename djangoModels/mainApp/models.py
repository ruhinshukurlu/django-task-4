from django.db import models

# Create your models here.

class Products(models.Model):
    
    category_choices = (
        ('convenience_goods', 'Convenience Goods'),
        ('shopping_goods', 'Shopping Goods'),
        ('specialty_goods','Specialty Goods'),
    )

    name = models.CharField(max_length=125, unique=True)
    description = models.TextField(max_length=500)
    category = models.CharField( max_length=125, choices=category_choices)
    picture = models.ImageField(upload_to='products/images/')
    amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    production_date = models.DateTimeField(auto_now_add=True)
    is_new = models.BinaryField(default=False)
    certificate = models.FileField(upload_to='products/files/',blank=True, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    detailed_view_link = models.URLField(max_length=300, null=True, blank=True)

    class Meta:
        db_table = 'company_products'
        ordering = ['name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'