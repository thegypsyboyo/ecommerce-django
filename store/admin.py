from django.contrib import admin
from .models import Product, Variations,ReviewRating, ProductGallery
# import admin_thumbnails - pip install the package to use it


class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'price', 'stock', 'category', 'modified_date', 'is_available' )
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

admin.site.register(Product, ProductAdmin)
admin.site.register(Variations, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
