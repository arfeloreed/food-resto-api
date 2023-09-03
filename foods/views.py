from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Food
from .serializers import FoodSerializer

# Create your views here.
# view route for home page
# def index(request):
#     foods = Food.objects.all()
#     food_list = []
#     for food in foods:
#         food_list.append(
#             {
#                 "name": food.name,
#                 "price": food.price,
#                 "description": food.description,
#             }
#         )
# print(f"\n{food_list}\n")
# return JsonResponse(food_list, safe=False)


# using django rest framework serializer to render json objects
# def index(request):
#     foods = Food.objects.all()
#     serializer = FoodSerializer(foods, many=True)
#     return JsonResponse(serializer.data, safe=False)


# using the DRF for home page
@api_view(["GET"])
def index(request):
    foods = Food.objects.all()
    serializer = FoodSerializer(foods, many=True)
    return Response(serializer.data)


# view route for a food detail
@api_view(["GET"])
def food_detail(request, pk):
    food = Food.objects.get(pk=pk)
    serializer = FoodSerializer(food)
    return Response(serializer.data)
