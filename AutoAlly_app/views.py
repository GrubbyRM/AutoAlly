from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarSerializer
from .databases_tools.cars_handler import CarsHandler
from .databases_tools.external_api import get_car_brands  # Import funkcji z pliku external_api

class CarView(APIView):
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            CarsHandler().add_car_to_db(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, vin):
        car = CarsHandler().get_car(vin)
        if car:
            return Response(car, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, vin):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            CarsHandler().update_car(vin, serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, vin):
        CarsHandler().delete_car(vin)
        return Response(status=status.HTTP_204_NO_CONTENT)

class CarBrandsView(APIView):
    def get(self, request):
        brands = get_car_brands()
        if brands:
            return Response(brands, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
