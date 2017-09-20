from django.shortcuts import render
from .models import Tag

def tag_name(request):
    tags=Tag.objects.all()
    return render(request,'tag.html',{'tags':tags})

# Create your views here.
