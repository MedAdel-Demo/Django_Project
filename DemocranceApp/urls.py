from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from . import views

#router created for the APIs
router = routers.DefaultRouter()
router.register(r'create_customer', views.CustomerViewSet)
router.register(r'create_quote', views.PolicyViewSet)
router.register(r'quote', views.PolicyViewSet)

#Pathes for all the pages of the project
urlpatterns = [
    path('', views.home , name="Login"),
    path('CreateCustomer/', views.CreateCustomerView.as_view(), name="customers.new"),
    path('CreateQuote/', views.CreatePolicyView.as_view(), name="Policy.new"),
    path('UpdateQuote/<int:pk>/edit', views.UpdatePolicyView.as_view(), name="Policy.Update"),
    path('customersView/', views.CustomersListView.as_view(), name="customers.list"),
    path('policiesView/', views.PoliciesListView.as_view(), name="policies.list"),
    path('policiesViewofCustomer/<int:pk>', views.PoliciesListViewofCustomer.as_view(), name="policiesofCustomer.list"),
    path('Authorized/', views.AuthorizedView.as_view()),
    path('customers/<int:pk>', views.CustomerDetailsView.as_view(), name="customers.details"),
    path('policies/<int:pk>', views.PolicyHistoryListView.as_view(), name="policy.details"),
    path("searchresults/", views.SearchResultsView.as_view(), name="search_results"),
    path("search/", views.SearchView.as_view(), name="search"),
    path('api/v1/', include(router.urls)),
]    
