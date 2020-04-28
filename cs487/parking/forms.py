from django import forms
import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
'''
class BookSpot(forms.Form):
    renewal_date = forms.DateField(label="booking date", help_text="Enter a date.")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - booking in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
#        if data > datetime.date.today() + datetime.timedelta(weeks=4):
#            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data
'''

class BookTime(forms.Form):
    renewal_time = forms.DateTimeField(label="booking time", help_text="Enter a start time of your estimated parking.")
    renewal_minute = forms.IntegerField(label="booking minute", help_text="Enter how long do you estimat you will park.")
    renewal_license = forms.CharField(label="booking minute", help_text="Enter your license plate number.")
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_time']
        if data < datetime.datetime.now():
            raise ValidationError(_('Invalid time - booking in past.'))
        return data
    def clean_renewal_minute(self):
        data = self.cleaned_data['renewal_minute']
        return data
    def clean_renewal_license(self):
        data = self.cleaned_data['renewal_license']
        if len(data) > 7:
            raise ValidationError(_('Invalid license plate number.'))
        return data

