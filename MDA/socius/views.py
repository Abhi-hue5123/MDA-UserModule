from django.shortcuts import render
from .models import Destination
from .models import UserList
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
import uuid 
from .models import MemberProfile,Phone,Address,Speciality,KeySKills,Certificates,Testimonial,Document,AcademicDetails,Event


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

    dests = Destination.objects.all()

    return render(response, "socius/index.html", {'dests': dests})

def Team(request):
    return render(request, "socius/team.html")

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
        		 data[3]
        		)
            value.save()
        connection = mail.get_connection()
        connection.open()
        email1 = mail.EmailMessage('MDA Invitation', 'This is the Invitation of MDA applcation.', settings.EMAIL_HOST_USER, d, connection=connection)
        email1.send()
        connection.close()

            
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


def PersonalDetails(request):
    if request.method == 'POST':
        M= MemberProfile()
        M.First_Name = request.POST['First_Name']
        M.Last_Name =  request.POST["Last_Name"]
        M.Bio =  request.POST["Bio"]
        M.Tag_Line =  request.POST["Tag_Line"]
        M.Status =  request.POST["Status"]
        M.save()

        P= Phone()
        P.Phone =  request.POST["Phone"]
        P.Email_Id =  request.POST["Email_id"]
        P.save()

        A= Address()
        A.Dno =  request.POST["Dno"]
        A.Street = request.POST["Street"]
        A.City =  request.POST["City"]
        A.State =  request.POST["State"]
        A.Country =  request.POST["Country"]
        A.Pin_Code =  request.POST["Pin_code"]
        A.save()
    return render(request,'socius/PersonalDetails.html')

def Education(request):
    if request.method == 'POST':
        E=AcademicDetails()
        E.Institution_Name = request.POST["Institution_Name"]
        E.Degree = request.POST["Degree"]
        E.Field_Of_Study = request.POST["Field_Of_Study"]
        E.Grade = request.POST["Grade"]
        E.Start_Date = request.POST["Start_Date"]
        E.End_Date = request.POST["End_Date"]
        E.Description = request.POST["Description"]
        E.save()
    return render(request,'socius/Education.html')

def Skills(request):
    if request.method == 'POST':
        Sk=KeySKills()
        Sk.Skills = request.POST['Skills']
        Sk.save()
        Sp= Speciality()
        Sp.speciality = request.POST['speciality']
        Sp.save()
    return render(request,'socius/Skills.html')

def  Certifications(request):
    if request.method == 'POST':
        C = Certificates()
        C.Name =  request.POST['Name']
        C.Issuing_Org = request.POST['Issuing_Org']
        C.Issued_Date = request.POST['Issued_Date']
        C.Expiration_Date = request.POST['Expiration_Date']
        C.Credential_Id = request.POST['Credential_Id']
        C.Credential_URL = request.POST['Credential_URL']
        C.Description = request.POST['Description']
        C.save()
    return render(request,'socius/Certifications.html')

def Testimonials(request):
    if request.method == 'POST':
        T=Testimonial()
        T.Description = request.POST['Description']
        T.Attestant = request.POST['Attestant']
        T.Date = request.POST['Date']
        T.Designation = request.POST['Designation']
        T.Location = request.POST['Location']
        T.save()
    return render(request,'socius/Testimonials.html')
