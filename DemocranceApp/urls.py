from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'create_customer', views.CustomerViewSet)

urlpatterns = [
    path('home/', views.HomeView.as_view(), name="index"),
    path('CreateCustomer/', views.CreateCustomerView.as_view(), name="customers.new"),
    path('customersView/', views.CustomersListView.as_view(), name="customers.list"),
    path('Authorized/', views.AuthorizedView.as_view()),
    path('customers/<int:pk>', views.CustomerDetailsView.as_view(), name="customers.details"),
    path('api/v1/', include(router.urls)),
]    
