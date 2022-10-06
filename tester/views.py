from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Profile


class profile_name1(ListView):
    model= Profile
    template_name= 'list1.html'

class profile_name2(ListView):
    model= Profile
    template_name= 'list2.html'

def dashboard(request):
        if request.method == 'POST':
            #basic
            profileimg = request.FILES['profileimg']
            name=request.POST['name']
            lname=request.POST['lname']
            phone=request.POST['phone']
            email=request.POST['email']
            #address
            address1=request.POST['address1']
            address2=request.POST['address2']
            city=request.POST['city']
            state=request.POST['state']
            zip=request.POST['zip']
            #education
            school=request.POST['school']
            schoolclass=request.POST['schoolclass']
            schooly1=request.POST['schooly1']
            schooly2=request.POST['schooly2']

            degree=request.POST['degree']
            stream = request.POST['stream']
            university=request.POST['university']
            degreein=request.POST['degreein']
            collegey1=request.POST['collegey1']
            collegey2=request.POST['collegey2']
            #projects
            projectheading = request.POST['projectheading']
            project_dis = request.POST['project_dis']
            #experience
            ex1pos = request.POST['ex1pos']
            ex1com = request.POST['ex1com']
            ex1years = request.POST['ex1years']

            ex2pos = request.POST['ex2pos']
            ex2com = request.POST['ex2com']
            ex2years = request.POST['ex2years']

            #about
            designation=request.POST['designation']
            about=request.POST['about']
            skill=request.POST['skill']
            interest = request.POST['interest']

            profile = Profile(
                #basic
                profileimg=profileimg,name=name,lname=lname,phone=phone,email=email,
                #address
                address1=address1,address2=address2,city=city,state=state,zip=zip,
                #education
                school=school,schoolclass=schoolclass,schooly1=schooly1,schooly2=schooly2,
                degree=degree,stream=stream,university=university,degreein=degreein,collegey1=collegey1,collegey2=collegey2,
                #projects
                projectheading=projectheading,project_dis=project_dis,
                #experience
                ex1pos=ex1pos,ex1com=ex1com,ex1years=ex1years,ex2pos=ex2pos,ex2com=ex2com,ex2years=ex2years,
                #about
                designation=designation,about=about,skill=skill,interest=interest
                )
            profile.save()
            return HttpResponseRedirect('/pdflist')
        return render(request, 'progress.html')
        
def landingpage(request):
    return render(request, 'landing.html')

def pdflist(request,*args, **kwargs):
    return render(request, 'pdflist.html')


#render view template 1

def render_pdf_view1(request, *args, **kwargs):
    pk = kwargs.get('pk')
    user_profile=Profile.objects.get(pk = pk)

    filename = user_profile.name
    template_path = 'resume.html'
    context = {'profile': user_profile}
    return render(request, template_path, context)

#render view template 2

def render_pdf_view2(request, *args, **kwargs):
    pk = kwargs.get('pk')
    user_profile=Profile.objects.get(pk = pk)

    filename = user_profile.name
    template_path = 'resume2.html'
    context = {'profile': user_profile}
    return render(request, template_path, context)
