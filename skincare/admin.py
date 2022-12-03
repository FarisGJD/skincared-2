from django.contrib import admin
from .models import Brand, ProductType, SkinType, SkinConcern, Skincare


class BrandAdmin(admin.ModelAdmin):
    """ Customise Brand Admin Panel """

    prepopulated_fields = {'slug': ('friendly_name',)}
    list_display = (
        'friendly_name',
        'name',
    )
    ordering = ('friendly_name',)


class ProductTypeAdmin(admin.ModelAdmin):
    """ Customise Product Type Admin Panel """

    list_display = (
        'friendly_name',
        'name'
    )
    ordering = ('friendly_name',)


class SkinTypeAdmin(admin.ModelAdmin):
    """ Customise Skin Type Admin Panel """

    prepopulated_fields = {'slug': ('type',)}
    list_display = (
        'type',
    )


class SkinConcernAdmin(admin.ModelAdmin):
    """ Customise Skin Type Admin Panel """

    list_display = (
        'concern',
    )


class SkincareAdmin(admin.ModelAdmin):
    """ Customise Skincare Admin Panel """

    list_display = (
        'name',
        'brand',
        'usage',
        'price',
        'sku',
        'product_type',
        'skin_type',
        'skin_concern',
        'crultey_free',
        'vegan',
        'alchol_free',
        'fragrance_free',
        'rating'
    )


admin.site.register(Brand, BrandAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(SkinType, SkinTypeAdmin)
admin.site.register(SkinConcern, SkinConcernAdmin)
admin.site.register(Skincare, SkincareAdmin)
