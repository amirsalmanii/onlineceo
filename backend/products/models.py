import os
from uuid import uuid4
from io import BytesIO
from random import randrange
from PIL import Image
from django.db import models
from django.core.files.base import ContentFile
from categories.models import Category
THUMB_SIZE = (400, 400)


def path_and_rename(instance, filename):
    """
    change file name when upload
    """
    upload_to = 'products'
    ext = filename.split('.')[-1]
    filename = f'{uuid4().hex}.{ext}'
    return os.path.join(upload_to, filename)


class Product(models.Model):
    categories = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, allow_unicode=True)
    image = models.ImageField(upload_to=path_and_rename, blank=True, null=True)
    image2 = models.ImageField(upload_to=path_and_rename, blank=True, null=True)
    image3 = models.ImageField(upload_to=path_and_rename, blank=True, null=True)
    # Todo save video for products
    thumbnail = models.ImageField(upload_to=path_and_rename, blank=True, null=True)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    hide = models.BooleanField(default=False)
    price = models.BigIntegerField(default=0)
    price_after_discount = models.BigIntegerField(default=0)
    company_price = models.BigIntegerField(default=0)
    manufacturer_company = models.CharField(max_length=120, null=True, blank=True)
    repository_quantity = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name

    # make thumbnail from original image and save it.
    def save(self, *args, **kwargs):
        if not self.make_thumbnail():
            pass
        self.slug = self.name.replace(' ', '-')
        super(Product, self).save(*args, **kwargs)

    def make_thumbnail(self):
        # if user set image
        if self.image:
            image = Image.open(self.image)
            image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)

            thumb_name, thumb_extension = os.path.splitext(self.image.name)
            thumb_extension = thumb_extension.lower()

            thumb_filename = thumb_name + '_thumb' + thumb_extension

            if thumb_extension in ['.jpg', '.jpeg']:
                FTYPE = 'JPEG'
            elif thumb_extension == '.gif':
                FTYPE = 'GIF'
            elif thumb_extension == '.png':
                FTYPE = 'PNG'
            else:
                return False  # Unrecognized file type

            # Save thumbnail to in-memory file as StringIO
            temp_thumb = BytesIO()
            image.save(temp_thumb, FTYPE)
            temp_thumb.seek(0)

            # set save=False, otherwise it will run in an infinite loop
            self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
            temp_thumb.close()

            return True
        else:
            return ''
