from django import forms
from .models import Contact, Reservation

class ContactModelForm(forms.ModelForm):

    class Meta:

        model = Contact
        fields = ['user_name', 'user_email', 'user_message']

class ReservationModelForm(forms.ModelForm):

    class Meta:

        model = Reservation
        fields = ['user_name', 'user_phone', 'user_time', 'user_date', 'user_count', 'user_message']