from django.db import models

# Create your models here.
class Contact(models.Model):  # Changed "models.model" to "models.Model"
    name = models.CharField(max_length=250)  # Fixed typo in "max_length"
    email = models.EmailField()
    number = models.CharField(max_length=12)  # Specify max length for number field
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approve = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Table"

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image1 = models.ImageField(upload_to='about_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='about_images/', null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Table"   



class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio_images/')
    link = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Portfolio Table"


class LatestNews(models.Model):
    news_image = models.ImageField(upload_to='news_images/')
    news_heading = models.TextField()
    news_description = models.TextField()

    def __str__(self):
        return self.news_heading

    class Meta:
        verbose_name_plural = "Latest News Table"


class OurGallery(models.Model):  # Changed the class name to follow the convention
    gallery_image = models.ImageField(upload_to='gallery_images/')  # Changed the upload_to path
    gallery_link = models.TextField()
    gallery_description = models.TextField()

    def __str__(self):
        return self.gallery_link

    class Meta:
        verbose_name_plural = "Our Gallery"

        

class Testimonial(models.Model):
    testimonial_image = models.ImageField(upload_to='testimonial_images/')  # Changed the upload_to path
    testimonial_heading = models.TextField()
    testimonial_description = models.TextField()

    def __str__(self):
        return self.testimonial_heading

    class Meta:
        verbose_name_plural = "Testimonial"
      



