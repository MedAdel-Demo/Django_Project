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

# Home Page class that is validating the login process (for Demo purposes)
def home(request):
    # check if the request is post
    if request.method =='POST': 
        
        #Validate login details entered by the user - security not implemented (just an example)
        details = CustomerForm(request.POST)

        #Split Login details function 
        if details.is_valid(): 
            
            #Get the Query string to be sent to the next page
            qs = extractlogindetails(details)
            if qs:
                return redirect(qs)
            
        else:
            # Redirect back to the same page if the data was invalid
            return render(request, "DemocranceAppTemplates\\index.html", {'form':details}) 
    else:
        # If the request is a GET request then, create an empty form object and render it into the page
        form = CustomerForm(None)  
        return render(request, 'DemocranceAppTemplates\\index.html', {'form':form})

#This class is used to build the query string that will be sent to the next page
#This is a hard-coded function just for the example showing a way of passing some normal attributes between pages // not considering any security measures
def extractlogindetails(details):
        try:
            fn = str(details['first_name'])
            fn = fn.split('\"')[5]
            ln = str(details['last_name'])
            ln = ln.split('\"')[5]
            dob = str(details['dob'])
            dob= dob.split('\"')[5]
            querystring = "CreateQuote/"+"?fn="+ fn+"&ln="+ln+"&dob="+dob
            return querystring
        except:
            return False

#This class is just showing an example of Authorization options - just an example for the test
class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'DemocranceAppTemplates\\403.html'
    login_url='/admin'

#This class is used for the Listing of the customers (Page displaying all the customers)
class CustomersListView(ListView):
    model = Customer
    context_object_name = "customers"
    template_name = 'DemocranceAppTemplates\\customers\\customersView.html'

#This class is used for the Listing of the Policies (Page displaying all the policies)
class PoliciesListView(ListView):
    model = Policy
    context_object_name = "policies"
    template_name = 'DemocranceAppTemplates\\policies\\policiesView.html'

#This class is used for Listing all the policies related to only a specific customer by Customer ID
class PoliciesListViewofCustomer(ListView):
        model = Policy
        context_object_name = "policies"
        template_name = 'DemocranceAppTemplates\\policies\\policiesViewofcustomer.html'

        #function to filter the needed results   
        def get_queryset(self):
            id = self.request.build_absolute_uri() 
            id = int(id.rsplit("/")[-1])
            combined_queryset = Policy.objects.filter(customer_id=id) #filtering the policies by Customer_ID taken from the URL (for Demo purposes)
            return combined_queryset

#This class is used for displaying the full history of a specific Policy (Single Policy History Page) 
class PolicyHistoryListView(ListView):
    model = Policy_History
    context_object_name = "policies_history"
    template_name="DemocranceAppTemplates\\policies\\policy_details.html"

    #function to filter the needed results   
    def get_queryset(self):
        id = self.request.build_absolute_uri() 
        id = int(id.rsplit("/")[-1])
        combined_queryset = Policy_History.objects.filter(ph_pid=id)
        return combined_queryset

#This class is used in a page created to display details of a single specific customer
class CustomerDetailsView(DetailView):
            model = Customer
            context_object_name = 'customer'
            template_name = 'DemocranceAppTemplates\\customers\\customer_details.html'

#This class is used in a page created to create a new customer
class CreateCustomerView(CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'dob']
    success_url = '../customersView/'
    template_name = "DemocranceAppTemplates\\customers\\create_customer.html"

#This class is used in a page created to create a new Quote/Policy
class CreatePolicyView(CreateView):
    model = Policy
    success_url = '../policiesView/'
    template_name = "DemocranceAppTemplates\\policies\\create_policy.html"
    form_class = PolicyForm

#This class is used by the Update Quote page to update the Quotes/Policies values
class UpdatePolicyView(UpdateView):
    model = Policy
    success_url = '../../policiesView/'
    template_name = "DemocranceAppTemplates\\policies\\update_policy.html"
    form_class = PolicyForm

#This class is used by the post API create_customer to create a new customer
class CustomerViewSet(viewsets.ModelViewSet):
   queryset = Customer.objects.all()
   serializer_class = CustomerSerializer

#This class is used by the post API create_quote to create a new policy
class PolicyViewSet(viewsets.ModelViewSet):
   queryset = Policy.objects.all()
   serializer_class = PolicySerializer

#This class is used for the Search page
class SearchView(TemplateView):
    template_name = 'DemocranceAppTemplates\search.html'

#This class is used to filter the search results
class SearchResultsView(ListView):
    model = Customer
    context_object_name = 'customer_policies_list'
    template_name = 'DemocranceAppTemplates\\search_results.html'

    #The sub-function used to filter the search results based on the search criterias chosen by the customer
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
