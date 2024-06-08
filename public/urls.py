from django.urls import path
from .views import ShowCaregoryWise,ShowCarDetails

urlpatterns = [
    path('productascategory/<int:category_id>',ShowCaregoryWise,name='productascategory'),
    path('car_details/<int:id>',ShowCarDetails,name='showcardetails'),
]