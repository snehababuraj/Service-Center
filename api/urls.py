from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.routers import DefaultRouter

from api import views

router=DefaultRouter()

router.register("customers",views.CustomerViewSetView,basename="customers")

urlpatterns=[

    path("token/",ObtainAuthToken.as_view()),

    path('customers/<int:pk>/work/',views.WorkCreateView.as_view()),

    path('work/<int:pk>/',views.workDetailView.as_view())
    
]+router.urls