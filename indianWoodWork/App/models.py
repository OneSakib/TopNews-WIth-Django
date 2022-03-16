from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from datetime import date
# Create your models here.


product_category = (
    ("Almiras", "Almiras"),
    ("LCD Panels", "LCD Panels"),
    ("Modular Kitchens", "Modular Kitchens"),
    ("Beds", "Beds"),
    ("Tables", "Tables"),
    ("Showroom Works", "Showroom Works"),
    ("Doors", "Doors"),
    ("Palles", "Palles"),

)


class ImageSlide(models.Model):
    s_no = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=150)
    description = models.CharField(default="", max_length=350)
    image = models.ImageField(upload_to='slide/', default="")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        im = Image.open(self.image)
        output = BytesIO()
        im = im.resize((600, 250))
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None
                                          )
        super(ImageSlide, self).save()


class Product(models.Model):
    s_no = models.AutoField(primary_key=True)
    slug = models.CharField(default="", max_length=50)
    name = models.CharField(default="", max_length=150)
    description = models.CharField(default="", max_length=350)
    update = models.DateField(default=date.today)
    product_cat = models.CharField(default="", choices=product_category, max_length=400)
    smallimage = models.ImageField(upload_to='product/', default="")
    hdimage1 = models.ImageField(upload_to='product/', default="")
    hdimage2 = models.ImageField(upload_to='product/', default="")
    hdimage3 = models.ImageField(upload_to='product/', default="")
    hdimage4 = models.ImageField(upload_to='product/', default="")
    arifmobile = models.IntegerField(default=0)
    arifwhatspp = models.IntegerField(default=0)
    danishmobile = models.IntegerField(default=0)
    danishwhatspp = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        im = Image.open(self.smallimage)

        output = BytesIO()
        im = im.resize((300, 225))
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        self.smallimage = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.smallimage.name.split('.')[0],
                                               'image/jpeg',
                                               sys.getsizeof(output), None
                                               )
        super(Product, self).save()


class ContactUs(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    phone = models.CharField(default="", max_length=4000)
    comment = models.TextField()

    def __str__(self):
        return self.comment[0:30] + " ...." + " by " + self.name
