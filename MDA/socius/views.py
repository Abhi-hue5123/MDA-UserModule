from django.shortcuts import render, redirect
from .models import Destination
from .models import UserList , memberdirectory
from .resources import UserListResource
from django.contrib import messages
from tablib import Dataset 
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
UserModel = get_user_model()
from django.core import mail
#import uuid 
#from .models import MemberProfile,Phone,Address,Speciality,KeySKills,Certificates,Testimonial,Document,AcademicDetails,Event
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import profileForm,contactInfoForm,addressForm,skillsForm,certificateForm,testimonialForm,educationForm
from .models import profile, contactInfo, address,skills,certificate,testimonial,education

# Create your views here.

def index(response):
    
    '''dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city never sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = True

    dest2 = Destination()
    dest2.name = 'Vizag'
    dest2.desc = 'The City of Destiny'
    dest2.img = 'destination_2.jpg'
    dest2.price = 1000
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Bangalore'
    dest3.desc = 'The Silicon City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 750
    dest3.offer = True

    dests = [dest1, dest2, dest3]'''

    #dests = Destination.objects.all()

    mems = memberdirectory.objects.all()

    return render(response, "socius/index.html", {'mems': mems})

def Team(request):
    return render(request, "socius/team.html")

@login_required(login_url='login')
def Python(request):
    return render(request, "socius/Python.html")



@allowed_users(allowed_roles=['admin','superuser'])
def simple_upload(request):
    if request.method == 'POST':
        user_list = UserListResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']

        if not new_person.name.endswith('xlsx'):
            messages.info(request, 'Wrong Format')
            return render(request, 'socius/upload.html')

        imported_data = dataset.load(new_person.read(),format='xlsx')
        #print(imported_data)
        d=[]
        for data in imported_data:
        	#print(data[1])
            #UserListInvitation(data[2])
            d.append(data[2])
            '''send_mail(
                'MDA Invitation',
                'This is the Invitation of MDA applcation.',
                settings.EMAIL_HOST_USER,
                [data[2]],
                fail_silently=False,
            )'''

            value = UserList(
        		data[0],
        		data[1],
        		 data[2],
        		 data[3],
                 data[4]
        		)
            value.save()
        l=d
        user=User.objects.filter(is_superuser='True').first()
        current_site = get_current_site(request)
        mail_subject = 'Invite to Socius'
        message = render_to_string('socius/invite.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        for i in l:
            #reciever_list.append(i['email'])
            to_email = i
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
        return HttpResponse('Invitations sended')
        '''connection = mail.get_connection()
        connection.open()
        email1 = mail.EmailMessage('MDA Invitation', 'This is the Invitation of MDA applcation.', settings.EMAIL_HOST_USER, d, connection=connection)
        email1.send()
        connection.close()'''

            
            #send_mail('Invitation MDA','This is MDA application Invitation',settings.EMAIL_HOST_USER, data[2], fail_silently=False)
            #send_mail('Invitation MDA', 'This is MDA application Invitation', settings.EMAIL_HOST_USER, data[2], fail_silently=False)
    return render(request, 'socius/upload.html')

    

'''def UserListInvitation(to_email):
    current_site = get_current_site(request)
    mail_subject = 'Invitation MDA.'
    message = render_to_string('accounts/acc_active_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })
    #to_email = request.POST['email']
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()'''

def active(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
      #  user.save()
        if user.is_active==True:
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
            return redirect('register')
    else:
        return HttpResponse('Invitation link is invalid!')


@login_required()
def profileView(request):
    if request.method == 'POST':
        profile_form = profileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,('Your profile was successfully updated!'))
            return redirect('/')
        else:
            #messages.error(request,('Please correct the error below.'))
            messages.info(request, 'The profile_form is not Valid')
            return redirect('profile')
        return redirect('index')
    else:
        profile_form = profileForm()
    context = {'profile_form':profile_form}
    return render(request,'socius/profile.html',context)


@login_required
def contactInfoView(request):
    if request.method == 'POST':
        contactInfo_form = contactInfoForm(request.POST,instance=request.user)
        if contactInfo_form.is_valid():
            contactInfo_form.save()
            messages.success(request,('Your contact details updated successfully'))
        else:
            messages.error(request,('Please correct the error below.'))
        return redirect('index')
    else:
        contactInfo_form = contactInfoForm(instance=request.user)
    
    context = {'contactInfo_form':contactInfo_form}
    return render(request,'socius/contactInfo.html',context)


@login_required
def addressView(request):
    if request.method == 'POST':
        address_form = addressForm(request.POST,instance=request.user)
        if address_form.is_valid():
            address_form.save()
            messages.success(request,('Your addresss details updated successfully'))
        else:
            messages.error(request,('Please correct the error below.'))
        return redirect('index')
    else:
        address_form = addressForm(instance=request.user)
    
    context = {'address_form':address_form}
    return render(request,'socius/address.html',context)


@login_required
def skillsView(request):
    ''''
    template_name = 'skills.html'

    def get(self,request):
        form = skillsForm()
        skill = skills.objects.all()
        args = {'form':form,'skill':skill}
        return render(request, self.template_name,args)
    '''
    if request.method == 'POST':
        skills_form = skillsForm(request.POST,instance=request.user)
        if skills_form.is_valid():
            skills_form.save()
            messages.success(request,('Your skills updated successfully'))
            return redirect('/')
        else:
            messages.error(request,('Please correct the error below.'))
        return redirect('index')
    else:
        skills_form = skillsForm(instance=request.user)
    
    context = {'skills_form':skills_form}
    return render(request,'socius/skills.html',context)


@login_required
def certificateView(request):
    if request.method == 'POST':
        certificate_form = certificateForm(request.POST,instance=request.user)
        if certificate_form.is_valid():
            certificate_form.save()
            messages.success(request,('Your  certifications updated successfully'))
        else:
            messages.error(request,('Please correct the error below.'))
        return redirect('index')
    else:
        certificate_form = skillsForm(instance=request.user)
    
    context = {'certificate_form':certificate_form}
    return render(request,'socius/certificate.html',context)


@login_required
def testimonialView(request):
    if request.method == 'POST':
        testimonial_form = testimonialForm(request.POST,instance=request.user)
        if testimonial_form.is_valid():
            testimonial_form.save()
            messages.success(request,('Your testimonials updated successfully'))
        else:
            messages.error(request,('Please correct the error below.'))
        return redirect('index')
    else:
        testimonial_form = testimonialForm(instance=request.user)
    
    context = {'testimonial_form':testimonial_form}
    return render(request,'socius/testimonial.html',context)


@login_required
def educationView(request):
    if request.method == 'POST':
        education_form = educationForm(request.POST,instance=request.user)
        if education_form.is_valid():
            education_form.save()
            messages.success(request,('Your academic details updated successfully'))
        else:
            messages.error(request,('Please correct the error below.'))
        return redirect('index')
    else:
        education_form = educationForm(instance=request.user)
    
    context = {'education_form':education_form}
    return render(request,'socius/education.html',context)