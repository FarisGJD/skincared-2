from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField


class Brand(models.Model):
    """ Brands Model """

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(
        max_length=200, null=True, blank=True)
    character_identifier = models.CharField(
        max_length=10, null=True, blank=True
    )
    about = models.TextField()
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True)

    class Meta:
        """ Orders Brands Alphabetically """

        ordering = ['friendly_name']

    def __str__(self):
        return self.name

    def brand_friendly_name(self):
        """ Returns Brands User Friendly Name """

        return self.friendly_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.friendly_name)
        super(Brand, self).save(*args, **kwargs)


class ProductType(models.Model):
    """ Product Type Model """

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField()
    image = models.ImageField(null=True, blank=True)

    class Meta:
        """ Orders Product Types Alphabetically """

        verbose_name = "Product Type"
        ordering = ['name']

    def __str__(self):
        return self.name

    def product_type_friendly_name(self):
        """ Returns Product Type User Friendly Name """

        return self.friendly_name


class SkinType(models.Model):
    """ Skin Type Model """

    class Meta:
        verbose_name = "Skin Type"

    type = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.type)
        super(SkinType, self).save(*args, **kwargs)

    def __str__(self):
        return self.type


class SkinConcern(models.Model):
    """ Skin Concern Model """

    class Meta:
        verbose_name = "Skin Concern"

    concern = models.CharField(max_length=50, null=True, blank=True)
    concern_friendly_name = models.CharField(
        max_length=50, null=True, blank=True
        )
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.concern


class Skincare(models.Model):
    """ Skincare Products Model """

    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL
        )
    about = models.TextField()
    name = models.CharField(max_length=300)
    usage = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    directions = models.TextField()
    ingredients = models.TextField()
    product_type = models.ForeignKey(
        'ProductType', null=True, blank=True, on_delete=models.SET_NULL
        )
    product_subtype = models.CharField(max_length=300, null=True, blank=True)
    product_subtype_friendly_name = models.CharField(
        max_length=300, null=True, blank=True)
    star_ingredient = ArrayField(
        models.CharField(max_length=200, blank=True, null=True),
    )
    skin_type = models.ForeignKey(
        'SkinType', null=True, blank=True, on_delete=models.SET_NULL
        )
    skin_concern = models.ForeignKey(
        'SkinConcern', null=True, blank=True, on_delete=models.SET_NULL
        )
    crultey_free = models.CharField(max_length=10)
    vegan = models.CharField(max_length=10)
    alchol_free = models.CharField(max_length=10)
    fragrance_free = models.CharField(max_length=10)
    sku = models.CharField(max_length=200, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )

    class Meta:
        """ Orders Product Types Alphabetically """

        ordering = ['rating']
        verbose_name = 'Skincare Product'

    def __str__(self):
        return self.name
