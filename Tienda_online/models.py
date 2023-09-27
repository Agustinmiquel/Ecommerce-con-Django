from django.db import models

from django.utils.text import slugify

class Product(models.Model):
    title= models.CharField(max_length=100)
    description= models.TextField()
    price= models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='products/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args,**kwargs )

    def __str__(self):
        return self.title
