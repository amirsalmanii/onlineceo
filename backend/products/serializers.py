from rest_framework import serializers
from .models import Product
from categories.serializers import CategoriesUpdateSerializer
from mark.models import Mark

class ProductsSerializerm1(serializers.ModelSerializer):
    categories = CategoriesUpdateSerializer(many=True)
    is_fav = serializers.SerializerMethodField()

    def get_is_fav(self, instance):
        """
        check this product fav of user or not
        if fav send true else send false
        """
        user = self.context.get('request').user
        try:
            Mark.objects.get(user=user, product=instance)
        except:
            return False
        else:
            return True


    class Meta:
        model = Product
        fields = [
        'id',
        'categories',
        'is_fav',
        'name',
        'slug',
        'image',
        'image2',
        'image3',
        'thumbnail',
        'body',
        'pdf_file',
        'hide',
        'price',
        'price_after_discount',
        'company_price',
        'manufacturer_company',
        'repository_quantity',
        ]


class ProductsSerializerm2(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
