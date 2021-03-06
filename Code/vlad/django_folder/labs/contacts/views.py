# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Contacts
from django.urls import reverse
from django.http import HttpResponseRedirect

# def index(request):
#   return HttpResponse('hello world!') # in order to see hello world I needed to use the following URL: http://localhost:8000/contacts/index/


def index(request):
    # I need to import model in the view in order to access it = from .models import Contacts
    contacts = Contacts.objects.all().order_by(
        'last_name')  # to see it by last_name
    context = {
        'contacts': contacts  # this is a dictionary of the whole contacts with the key contacts

        # 'message': 'Hello World!!'
    }
    # contacts will link with index.html with is going to connect to the detail page from the index.html
    return render(request, 'contacts/index.html', context)
    # this for loop will loop for each contact in contacts {% for contact in contacts %} then with the following div we are connecting to the detail page which I ordered by last name first name: <a href="{% url 'contacts:detail' contact.id %}"> {{contact.last_name}}, {{contact.first_name}} </a>

# View for the Detail


def detail(request, contact_id):  # contact_id each person have a unique contact_id
    contact = get_object_or_404(Contacts, pk=contact_id)
    # {'contact': contact}) this is giving a single contact this is why is singular because when we click the name of one of the people in the contact list it will give only that person contact details instead of everyone else
    return render(request, 'contacts/detail.html', {'contact': contact})


def create_contact_page(request):
    return render(request, 'contacts/contact_new.html')


def create_contact(request):
    # When creating a new contact in the new contact page it will show and create a field for the first name
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    age = request.POST['age']
    birthday = request.POST['birthday']
    phone_number = request.POST['phone_number']
    # we have a in here because it is a checkbox and if you do not have it it wont work
    is_cell = 'is_cell' in request.POST
    comments = request.POST['comments']

    # Create a tuple
    create_contact = Contacts(first_name=first_name,
                              last_name=last_name,
                              age=age,
                              birthday=birthday,
                              phone_number=phone_number,
                              is_cell=is_cell,
                              comments=comments)
    create_contact.save()  # to save to the database

    # remember to putting a comma at the end
    # redirecting to the detail page
    return HttpResponseRedirect(reverse('contacts:detail', args=(create_contact.id,)))

# I am having issues with the  first_name=first_name, and  ) on line 54
# the terminal is giving me the following error:

#     from . import views
#   File "/Users/owner/Desktop/Program/class_armadillo/Code/vlad/django_folder/labs/contacts/views.py", line 48
#     first_name=first_name,
#               ^
# SyntaxError: invalid syntax
