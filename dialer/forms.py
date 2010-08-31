from django import forms
from django.contrib.localflavor.us.forms import USPhoneNumberField 
from dialer.models import Call

class DialerForm(forms.ModelForm):
    """
    A simple form for creating a new dial
    """
    name1 = forms.CharField(max_length=50, label='First friend', required=False)
    number1 = USPhoneNumberField(max_length=19, label = 'ph #')
    name2 = forms.CharField(max_length=50, label='Second friend', required=False)
    number2 = USPhoneNumberField(max_length=19, label = 'ph #')

    class Meta:
        model = Call
        fields = ('name1', 'number1', 'name2', 'number2')
