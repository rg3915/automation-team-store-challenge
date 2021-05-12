from typing import List
from uuid import UUID

from django.shortcuts import get_object_or_404
from ninja import Router, Schema

from .models import Product

router = Router()


class ProductSchema(Schema):
    id: int
    uuid: UUID
    title: str
    description: str
    price: float
    image: str


@router.get("/products", response=List[ProductSchema])
def list_products(request):
    qs = Product.objects.all()
    return qs


@router.get("/products/{id}", response=ProductSchema)
def get_product(request, id: int):
    product = get_object_or_404(Product, id=id)
    return product
