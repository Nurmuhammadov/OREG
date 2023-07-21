from django.db import models
from django.contrib.auth.models import User


class Information(models.Model):
    logo = models.ImageField(upload_to='info/')
    logo_text = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Category(models.Model):
    img = models.ImageField(upload_to='category/')
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class CounterArea(models.Model):
    actives = models.IntegerField()
    per_day = models.IntegerField()
    satisfied_clients = models.IntegerField()
    awards = models.IntegerField()


class AboutUsImg(models.Model):
    text = models.CharField(max_length=255)
    img_one = models.ImageField(upload_to='about/')
    img_two = models.ImageField(upload_to='about/')


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    about_side = models.ForeignKey(AboutUsImg, on_delete=models.CASCADE)


class WhyChooseUs(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    img = models.ImageField(upload_to='choose/')


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    definition = models.CharField(max_length=255)
    stars = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_slid = models.BooleanField(default=True)


class Partner(models.Model):
    img = models.ImageField(upload_to='partner/')


class GalleryCategory(models.Model):
    name = models.CharField(max_length=255)


class Gallery(models.Model):
    img = models.ImageField(upload_to="gallery/")
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE)


class FaqImg(models.Model):
    img = models.ImageField(upload_to='stage/')


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)


class PricingTable(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()


class ContactUs(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    web_site_link = models.URLField()
    subject = models.CharField(max_length=255)
    message = models.TextField()


class Blog(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='blog/')
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)


class Comment(models.Model):
    comment_text = models.CharField(max_length=255)
    which_blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


class Subscriber(models.Model):
    email = models.EmailField()


class Cart(models.Model):
    project = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)