from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.template.defaultfilters import slugify
from django.urls import reverse

class Post(models.Model):
    name = models.CharField(max_length=100)
    # bio = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image', blank = True)
    # productPic = models.ImageField(upload_to='profile_image', blank = True)
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(default="Hello, I am newbie here")
    PFeaturedimage = models.ImageField(default='Pdefault.jpg', upload_to='PFeatured_pics')
    PFeaturedimage2 = models.ImageField(default='Pdefault.jpg', upload_to='PFeatured_pics2')
    TFeaturedimage = models.ImageField(default='Tdefault.jpg', upload_to='TFeatured_pics')
    TFeaturedimage2 = models.ImageField(default='Tdefault.jpg', upload_to='TFeatured_pics2')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class ProductPic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_pics',
                              verbose_name='Image')
    location = models.TextField()
    title = models.TextField()
    story = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def save(self, *args, **kwargs):
        super(ProductPic, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 350 or img.width > 900:
            output_size = (350,900)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    def __str__(self):
        return str(self.item) + ": $" + str(self.price)


    def __str__(self):
        return f'{self.user.username} Product'

    def get_absolute_url(self):
        return reverse('base:post-detail', kwargs={'pk': self.pk})

    
class TravelPic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='travel_pics',
                              verbose_name='Image')
    location = models.TextField()
    title = models.TextField()
    story = models.TextField()
    TravelExpenses = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def save(self, *args, **kwargs):
        super(TravelPic, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 350 or img.width > 900:
            output_size = (350,900)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    def __str__(self):
        return str(self.item) + ": $" + str(self.TravelExpenses)

    def __str__(self):
        return f'{self.user.username} Travel'

    def get_absolute_url(self):
        return reverse('base:travel-detail', kwargs={'pk': self.pk})

class FoodPic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='food_pics',
                              verbose_name='Image')
    location = models.TextField()
    title = models.TextField()
    story = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def save(self, *args, **kwargs):
        super(FoodPic, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 350 or img.width > 900:
            output_size = (350,900)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    def __str__(self):
        return str(self.item) + ": $" + str(self.price)


    def __str__(self):
        return f'{self.user.username} Food'

    def get_absolute_url(self):
        return reverse('base:food-detail', kwargs={'pk': self.pk})

    