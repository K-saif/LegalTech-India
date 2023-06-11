from django.shortcuts import render , redirect
from .models import *
from django.shortcuts import render, get_object_or_404
from .forms import ContactusForm

def home(request):
    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            Contactus.objects.create(name=name,  mobile=mobile, email=email, subject=subject, message=message,)
            return redirect('home')
    else:
        form = ContactusForm()

    return render(request, 'index.html', {'form': form})

def blog(request):
    return render(request , 'blog.html')

def blog_details(request):
    return render(request , 'blog-details.html')


def business(request):
    return render(request , 'sv-bs.html')

def licencing(request):
    return render(request , 'sv-reg.html')

def taxation(request):
    return render(request , 'sv-gst.html')

def ipr(request):
    return render(request , 'sv-ipr.html')

def it(request):
    return render(request , 'sv-it.html')

def business_registration(request, slug):
    # Retrieve the service object with the given slug
    service = get_object_or_404(Business_Registration, slug=slug)

    context = {
        'service': service,
    }

    return render(request, 'service_details.html', context)

def registration_licencing(request, slug):
    # Retrieve the service object with the given slug
    service = get_object_or_404(Registration_Licencing, slug=slug)

    context = {
        'service': service,
    }

    return render(request, 'service_details.html', context)

def gst_incometax(request, slug):
    # Retrieve the service object with the given slug
    service = get_object_or_404(Gst_IncomeTax, slug=slug)

    context = {
        'service': service,
    }

    return render(request, 'service_details.html', context)

def intellectual_property(request, slug):
    # Retrieve the service object with the given slug
    service = get_object_or_404(Intellectual_Property, slug=slug)

    context = {
        'service': service,
    }

    return render(request, 'service_details.html', context)

def information_technology(request, slug):
    # Retrieve the service object with the given slug
    service = get_object_or_404(Information_Technology, slug=slug)

    context = {
        'service': service,
    }

    return render(request, 'service_details.html', context)

def other_service(request, slug):
    # Retrieve the service object with the given slug
    service = get_object_or_404(Other_Service, slug=slug)
    context = {
        'service': service,
    }

    return render(request, 'service_details.html', context)
