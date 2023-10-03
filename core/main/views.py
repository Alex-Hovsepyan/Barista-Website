from django.shortcuts import render, redirect
from .models import Header, Home, About, Title, Member, Menu, MenuCategory, MenuContent, Testimonial, ContactInfo, Footer, OpenHours, Contact, ReservationInfo, Reservation
from .forms import ContactModelForm, ReservationModelForm

# Create your views here.

def double_content():
    header = Header.objects.all()[0]
    titles = Title.objects.all()[0]
    footer = Footer.objects.all()[0]
    open_hours = OpenHours.objects.all()

    return [header, titles, footer, open_hours]

def index(request):
    home = Home.objects.all()[0]
    about = About.objects.all()[0]
    members = Member.objects.all()
    menu = Menu.objects.all()[0]

    categoires = MenuCategory.objects.all()
    product_by_category = {}
    for category in categoires:
        product_by_category[category] = MenuContent.objects.filter(category=category)

    testimonials = Testimonial.objects.all()
    contact_info = ContactInfo.objects.all()[0]
    

    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = ContactModelForm()

    return render(request, 'index.html', context={
        'header':double_content()[0],
        'home':home,
        'about':about,
        'titles':double_content()[1],
        'members':members,
        'menu':menu,
        'product_by_category':product_by_category,
        'testimonials':testimonials,
        'contact_info':contact_info,
        'footer':double_content()[2],
        'open_hours':double_content()[3]
    })

def reservation(request):
    reservation_info = ReservationInfo.objects.all()[0]

    if request.method == 'POST':
        form = ReservationModelForm(request.POST)
        if form.is_valid():
            Reservation.objects.create(**form.cleaned_data)
            return redirect('reservation')
    else:
        form = ReservationModelForm()
    
    return render(request, 'reservation.html', context={
        'header':double_content()[0],
        'titles':double_content()[1],
        'footer':double_content()[2],
        'open_hours':double_content()[3],
        'reservation_info':reservation_info,
    })