from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)
    
    def get_friendly_name(self):
        return str(self.friendly_name)


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    on_sale = models.BooleanField(default=False)
    normal_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    summary = models.TextField()
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
    
    def get_price(self):
        return str(self.price)
    
    def get_sale(self):
        return str(self.on_sale)
    
    def get_rating(self):
        return str(self.rating)