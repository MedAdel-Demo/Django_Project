from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Policy
from .models import Customer
from django.views import View
from django.http import JsonResponse
from django.core.serializers import serialize
from django.http import Http404
from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView

from rest_framework import viewsets
from .serializers import CustomerSerializer


class HomeView(TemplateView):
    template_name = 'DemocranceAppTemplates\index.html'
    extra_context = {'today': datetime.today()}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'DemocranceAppTemplates\\403.html'
    login_url='/admin'

# @login_required(login_url='/admin')
# def Authorized(request):
#     return render(request, 'DemocranceAppTemplates\\403.html', {})

class CustomersListView(ListView):
    model = Customer
    context_object_name = "customers"
    template_name = 'DemocranceAppTemplates\\customersView.html'

# CustomersListView class view to replace the function view below
# def customerView(request):
#     # Customer.objects.all().delete()
#     All_Customers = Customer.objects.all()
#     return render(request, 'DemocranceAppTemplates\\customersView.html', {'customers': All_Customers})

class CustomerDetailsView(DetailView):
            model = Customer
            context_object_name = 'customer'
            template_name = 'DemocranceAppTemplates\\customers\\customer_details.html'

#class view replaces this view, even no need to add the try and catches - it is already handled
# def customerdetails(request, pk):
#         try:
#             customer = Customer.objects.get(pk=pk)
#             return render(request, 'DemocranceAppTemplates\\customers\\customer_details.html', {'customer' : customer})
#         except Customer.DoesNotExist:
#             raise Http404("Customer Doesn't exist")


class CreateCustomerView(CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'dob']
    success_url = '../customersView/'
    template_name = "DemocranceAppTemplates\\customers\\create_customer.html"

class CustomerViewSet(viewsets.ModelViewSet):
   queryset = Customer.objects.all()
   serializer_class = CustomerSerializer

# def CreateCustomer(request):
#     return PoliciesView()

# class PoliciesView(View): #or TemplateView
#     def get(self, request):
#         policies_count = Policy.objects.count()  # TOTAL books in the database
#         policies = Policy.objects.all()  # Get all book objects from the database

#         policies_serialized_data = serialize('python', policies)

#         data = {
#             'Policies': policies_serialized_data,
#             'count': policies_count,
#         }
#         return JsonResponse(data)