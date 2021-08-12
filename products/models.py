from django.db import models


class ParentCategory(models.Model):
    class Meta:
        verbose_name_plural = "Parent Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return str(self.friendly_name)


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    parent_category = models.ForeignKey(
        'ParentCategory', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return str(self.friendly_name)
    
    def show_parent(self):
        return str(self.parent_category)


class Product(models.Model):
    class Meta:
        verbose_name_plural = "Products"

    salesOptions = (
        (1, "No"),
        (2, "Yes"),
    )
    planOptions = (
        (1, "No"),
        (2, "Yes"),
    )
    upsellOptions = (
        (1, "No"),
        (2, "Yes"),
    )
    # Title is for Meta description
    title = models.CharField(max_length=65, null=True, blank=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    plan = models.IntegerField(choices=planOptions, default=1)
    has_upsell = models.IntegerField(choices=planOptions, default=1)
    upsell_target = models.ForeignKey(
        'Product', null=True, blank=True, on_delete=models.SET_NULL)
    add_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    on_sale = models.IntegerField(choices=salesOptions, default=1)
    normal_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    summary = models.TextField()
    description = models.TextField()
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    rating_count = models.IntegerField(default=0)
    rating_total = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)
    rating_update = models.DateTimeField(null=True, blank=True)
    included = models.TextField()
    preview = models.URLField(max_length=1024, null=True, blank=True)
    image_url1 = models.URLField(max_length=1024, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image_url2 = models.URLField(max_length=1024, null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image_url3 = models.URLField(max_length=1024, null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image_url4 = models.URLField(max_length=1024, null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image_url5 = models.URLField(max_length=1024, null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    sold = models.IntegerField(null=True, default=0)
    available = models.IntegerField(null=True, default=10)

    def __str__(self):
        return str(self.name)

    def get_price(self):
        return str(self.price)

    def get_sale(self):
        return str(self.on_sale)

    def get_rating(self):
        return str(self.rating)

    def get_sold(self):
        return str(self.sold)
