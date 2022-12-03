from django.shortcuts import render, get_object_or_404
from .models import Brand, SkinType, SkinConcern


def all_products(request):
    """ A View To Render All Products  """

    return render(request, 'products/all_products.html')


def product_details(request):
    """ A View To Render A Single Detailed Product """

    return render(request, 'products/product_details.html')


def all_brands(request):

    """ A view to render all brands and organize them alphabetically """

    # Retrieves Brand Object
    brands = Brand.objects.all()

    # Renders Brand Starting Letters & Ommits Duplicate Values
    brand_letters_query = brands.values_list(
        'character_identifier', flat=True
        )
    brand_letters = []
    for letters in brand_letters_query:
        if letters not in brand_letters:
            brand_letters.append(letters)

    # Renders & Orders Brands By Friendly Name
    brand_letter_startswith = brands.order_by('friendly_name').values

    context = {
        'brands': brands,
        'brand_letters': brand_letters,
        'brand_letter_startswith': brand_letter_startswith,
    }

    return render(request, 'brands/brands.html', context)


def full_brands(request, slug):

    """ A view to use the slug field to take user to the correct brand and
    relevant information """

    # Retrives Brand object
    queryset = Brand.objects.all()

    # Retrives the slug from the Brand object then applies it to each brand
    full_brand = get_object_or_404(queryset, slug=slug)

    context = {
        'full_brand': full_brand,
    }

    return render(request, 'brands/full_brands.html', context)


def skin_type(request):
    """ A View To Render & Filer For Skin Types  """

    # Retrives Skin Type Object
    skin_type = SkinType.objects.all()
    
    context = {
        'skin_type': skin_type,
    }

    return render(request, 'skin_type/skin_type.html', context)


def skin_concern(request):
    """ A View To Render & Filer For Skin Concerns  """

    skin_concern = SkinConcern.objects.all()

    context = {
        'skin_concern': skin_concern,
    }

    return render(request, 'skin_concern/skin_concern.html', context)
