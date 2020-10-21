from django.shortcuts import render,redirect
from jobsapp.models import SoftwareJobs,PharmaJobs,AgricultureJobs

# Create your views here.
def show_software_view(request):
    data =SoftwareJobs.objects.all()
    return render(request, "showsoftwarejobs.html",{"data":data})   # this is for administrator

def bootstrap_view(request):
    return render(request,'bootstrap.html')

def software_view(request):
    data =SoftwareJobs.objects.all()
    return render(request,'software.html',{'data':data}) # this is for user

def add_view(request):
    if request.method =="POST":
        print(request.POST)
        company_name = request.POST.get("company_name") #get madhe key lihito =>value  means get(key)=value ani value madhe value deto
        city =request.POST.get("city")
        vaccancy=request.POST.get("vaccancy")
        experience=request.POST.get("experience")
        skills=request.POST.get("skills")
        o =SoftwareJobs(company_name=company_name,city=city,vaccancy=vaccancy,experience=experience,skills=skills)   #(company_name---key = company_name ---value)
        o.save()
        return redirect("/showsoftwarejobs/")
    return render(request,'add.html')

def delete(request,id):
    o=SoftwareJobs.objects.get(pk=id)
    print(id)
    o.delete()
    return redirect('/showsoftwarejobs/')

def update_view(request,id):
    o=SoftwareJobs.objects.get(pk=id)
    if request.method == "POST":
        o.company_name = request.POST.get("company_name")   #get madhe key lihito =>value
        o.city=request.POST.get("city")
        o.vaccancy=request.POST.get("vaccancy")
        o.experience=request.POST.get("experience")
        o.skills=request.POST.get("skills")
        o.save()
        return redirect("/showsoftwarejobs/")
    return render(request,'update.html',{'o':o})
#============================================================================================================
#=================2ND JOB CLASS IMPLEMENTATION===============================================================
#============================================================================================================

def show_pharma_view(request):
    data =PharmaJobs.objects.all()
    return render(request, "showpharmajobs.html",{"data":data})

def pharma_view(request):
    data =PharmaJobs.objects.all()
    return render(request,'pharma.html',{'data':data})

def add_view(request):
    if request.method =="POST":
        print(request.POST)
        company_name = request.POST.get("company_name")
        city =request.POST.get("city")
        vaccancy=request.POST.get("vaccancy")
        experience=request.POST.get("experience")
        skills=request.POST.get("skills")
        o =PharmaJobs(company_name=company_name,city=city,vaccancy=vaccancy,experience=experience,skills=skills)
        o.save()
        return redirect("/showpharmajobs/")
    return render(request,'add.html')

def delete(request,id):
    o=PharmaJobs.objects.get(pk=id)
    print(id)
    o.delete()
    return redirect('/showpharmajobs/')

def update_view(request,id):
    o=PharmaJobs.objects.get(pk=id)
    if request.method == "POST":
        o.company_name = request.POST.get("company_name")   #get madhe key lihito =>value
        o.city=request.POST.get("city")
        o.vaccancy=request.POST.get("vaccancy")
        o.experience=request.POST.get("experience")
        o.skills=request.POST.get("skills")
        o.save()
        return redirect("/showpharmajobs/")
    return render(request,'update.html',{'o':o})

#============================================================================================================
#================3RD JOB CLASS IMPLEMENTATION===============================================================
#============================================================================================================

def show_agriculture_view(request):
    data =AgricultureJobs.objects.all()
    return render(request, "showagriculture.html",{"data":data})

def agriculture_view(request):
    data =AgricultureJobs.objects.all()
    return render(request,'agriculture.html',{'data':data})

def add_view(request):
    if request.method =="POST":
        print(request.POST)
        company_name = request.POST.get("company_name")
        city =request.POST.get("city")
        vaccancy=request.POST.get("vaccancy")
        experience=request.POST.get("experience")
        skills=request.POST.get("skills")
        o =AgricultureJobs(company_name=company_name,city=city,vaccancy=vaccancy,experience=experience,skills=skills)
        o.save()
        return redirect("/showagriculturejobs/")
    return render(request,'add.html')

def delete(request,id):
    o=AgricultureJobs.objects.get(pk=id)
    print(id)
    o.delete()
    return redirect('/showagriculturejobs/')

def update_view(request,id):
    o=AgricultureJobs.objects.get(pk=id)
    if request.method == "POST":
        o.company_name = request.POST.get("company_name")   #get madhe key lihito =>value
        o.city=request.POST.get("city")
        o.vaccancy=request.POST.get("vaccancy")
        o.experience=request.POST.get("experience")
        o.skills=request.POST.get("skills")
        o.save()
        return redirect("/showagriculturejobs/")
    return render(request,'update.html',{'o':o})
