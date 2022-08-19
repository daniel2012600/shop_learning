from django.shortcuts import render

# Create your views here.
from tools.R import R
from .models import Product

from tools.db import ProductStatus,ProductCategory
def product(request,categoryID = None,productID = None):
    if 'category' in request.path:
        return R.ok(ProductCategory.dict())

    if request.method == "GET" and categoryID is not None:

        if not categoryID.isdigit():
            return R.badRequest("categoryID is number only!")

        if int(categoryID) not in ProductCategory.list():
            return R.badRequest("category ID does not exist")
        products = Product.objects.filter(status = ProductStatus.activate.value).filter(category = categoryID)
        products = [i.toJson() for i in products]
        return R.ok(products)
