from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Customer, Policy, Policy_History
from django.views import View
from django.http import JsonResponse
from django.core.serializers import serialize
from django.http import Http404
from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from rest_framework import viewsets
from .serializers import CustomerSerializer, PolicySerializer
from django.core.exceptions import ValidationError
from .forms import CustomerForm, PolicyForm

# class HomeView(TemplateView):
#     template_name = 'DemocranceAppTemplates\\index.html'
#     extra_context = {'today': datetime.today()}
#     form_class = CustomerForm

def home(request):
    # check if the request is post
    if request.method =='POST': 
        # Pass the form data to the form class
        details = CustomerForm(request.POST)

        if details.is_valid(): 
 
            # Temporarily make an object to be add some
            # logic into the data if there is such a need
            # before writing to the database  
            post = details.save(commit = False)
 
            # redirect it to some another page indicating data

            fn = str(details['first_name'])
            fn = fn.split('\"')[5]
            ln = str(details['last_name'])
            ln = ln.split('\"')[5]
            dob = str(details['dob'])
            dob= dob.split('\"')[5]
            return redirect("CreateQuote/"+"?fn="+ fn+"&ln="+ln+"&dob="+dob)
             
        else:
         
            # Redirect back to the same page if the data
            # was invalid
            return render(request, "DemocranceAppTemplates\\index.html", {'form':details}) 
    else:
 
        # If the request is a GET request then,
        # create an empty form object and
        # render it into the page
        form = CustomerForm(None)  
        return render(request, 'DemocranceAppTemplates\\index.html', {'form':form})


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'DemocranceAppTemplates\\403.html'
    login_url='/admin'


class CustomersListView(ListView):
    model = Customer
    context_object_name = "customers"
    template_name = 'DemocranceAppTemplates\\customers\\customersView.html'

class PoliciesListView(ListView):
    model = Policy
    context_object_name = "policies"
    template_name = 'DemocranceAppTemplates\\policies\\policiesView.html'

class PoliciesListViewofCustomer(ListView):
        model = Policy
        context_object_name = "policies"
        template_name = 'DemocranceAppTemplates\\policies\\policiesViewofcustomer.html'
    
        def get_queryset(self):
            id = self.request.build_absolute_uri() # self.request.GET.get("id")
            id = int(id.rsplit("/")[-1])
            combined_queryset = Policy.objects.filter(customer_id=id)
            return combined_queryset

class PolicyHistoryListView(ListView):
    model = Policy_History
    context_object_name = "policies_history"
    template_name="DemocranceAppTemplates\\policies\\policy_details.html"
    
    def get_queryset(self):
        id = self.request.build_absolute_uri() # self.request.GET.get("id")
        id = int(id.rsplit("/")[-1])
        combined_queryset = Policy_History.objects.filter(ph_pid=id)
        return combined_queryset


class CustomerDetailsView(DetailView):
            model = Customer
            context_object_name = 'customer'
            template_name = 'DemocranceAppTemplates\\customers\\customer_details.html'

class CreateCustomerView(CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'dob']
    success_url = '../customersView/'
    template_name = "DemocranceAppTemplates\\customers\\create_customer.html"
    

class CustomerViewSet(viewsets.ModelViewSet):
   queryset = Customer.objects.all()
   serializer_class = CustomerSerializer


class CreatePolicyView(CreateView):
    model = Policy
    success_url = '../policiesView/'
    template_name = "DemocranceAppTemplates\\policies\\create_policy.html"
    form_class = PolicyForm
    


class PolicyViewSet(viewsets.ModelViewSet):
   queryset = Policy.objects.all()
   serializer_class = PolicySerializer

class UpdatePolicyView(UpdateView):
    model = Policy
    success_url = '../policiesView/'
    template_name = "DemocranceAppTemplates\\policies\\update_policy.html"
    form_class = PolicyForm

class SearchView(TemplateView):
    template_name = 'DemocranceAppTemplates\search.html'

class SearchResultsView(ListView):
    model = Customer
    context_object_name = 'customer_policies_list'
    template_name = 'DemocranceAppTemplates\\search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        radiogroup = self.request.GET.get("r")
        
        if radiogroup == "Customer Name":
            combined_queryset = Customer.objects.filter(first_name=query) | Customer.objects.filter(last_name=query)
            combined_queryset.order_by('first_name')
        elif radiogroup == "Customer Date of Birth":
            combined_queryset = Customer.objects.filter(dob=query)
            combined_queryset.order_by('first_name')
        else:
            ids = Policy.objects.select_related('cid').filter(type=query).values_list('cid', flat=True)
            combined_queryset = Customer.objects.filter(id__in=ids)

        return combined_queryset
