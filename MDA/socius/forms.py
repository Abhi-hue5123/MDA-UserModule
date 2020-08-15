from django import forms
from multi_email_field.forms import MultiEmailField
from django.contrib.auth.models import User
from .models import profile,contactInfo,address,skills,certificate,testimonial,education

class profileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ('photo','firstName','lastName','bio','tagLine','status')



class contactInfoForm(forms.ModelForm):
    class Meta:
        model = contactInfo
        fields = ('emails','countryCode','phone')


class addressForm(forms.ModelForm):
    class Meta:
        model = address
        fields = ('flatNo','street','city','state','country','pinCode')

class skillsForm(forms.ModelForm):
    class Meta:
        model = skills
        fields = ('skill','speciality')
        '''
        widget = {
            'skill': forms.TextInput(attrs ={'class':'form-control'}),
            'speciality': forms.TextInput(attrs = {'class':'form-control'})
        }
        '''

class certificateForm(forms.ModelForm):
    class Meta:
        model = certificate
        fields = ('name','issuingOrg','issuedDate','expiryDate','credentialId','credentialUrl','description')

class testimonialForm(forms.ModelForm):
    class Meta:
        model = testimonial
        fields = ('attestant','issuedDate','services','designation','location','description')

class educationForm(forms.ModelForm):
    class Meta:
        model = education
        fields = ('institute','degree','branch','grade','startDate','endDate','description')