from django.shortcuts import render

# Create your views here.
def dummy(request):
    return render(request,'dummy.html')
def home(request):
    return render(request,'home.html')
def courses(request):
    return render(request,'courses.html')
def batches(request):
    return render(request,'batches.html')
def placements(request):
    return render(request,'placements.html')
def corporates(request):
    return render(request,'corporates.html')

def contacts(request):
    return render(request,'contacts.html')

def enquiry(request):
    return render(request,'enquiry.html')
