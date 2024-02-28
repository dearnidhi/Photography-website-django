from django.shortcuts import render
from myapp.models import Contact, About,Portfolio,LatestNews
from myapp.models import Contact, About, Portfolio, LatestNews, Testimonial,OurGallery
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # Assuming you want to display the latest news, gallery, and testimonials on the index page
    latest_news = LatestNews.objects.all()[:5]  # Adjust the number based on how many latest news you want to display
    gallery = OurGallery.objects.all()[:3]  # Adjust the number based on how many gallery images you want to display
    testimonials = Testimonial.objects.all()[:3]  # Adjust the number based on how many testimonials you want to display
    
    return render(request, 'index.html', {'latest_news': latest_news, 'gallery': gallery, 'testimonials': testimonials})
    #return render(request, 'index.html', {'latest_news': latest_news})


def contact_us(request):
        context={}
        if request.method=="POST":
               name=request.POST.get("name")
               em=request.POST.get("email")
               num=request.POST.get("number")
               msz=request.POST.get("message")
               obj=Contact(name=name, email=em,number=num,message=msz) 
               obj.save()  
               #return HttpResponse(f"Dear {name},Thanks For your Time") 
               context['message']=f"Dear {name},Thanks For Your Time!"     
        return render(request, 'contact.html',context)



def about(request):
        
    about_data = About.objects.first()  # Assuming you have an About instance in the database
    return render(request, 'about.html', {'about_data': about_data})
    #return render(request, 'about.html')


def portfolio(request):
    portfolio_data = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'portfolio_data': portfolio_data})
