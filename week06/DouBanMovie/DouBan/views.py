from django.shortcuts import render

# Create your views here.
from .models import DoubanMovie

def movie_short(request):
    shorts=DoubanMovie.objects.all()
    counter=DoubanMovie.objects.all().count()


    queryset=DoubanMovie.objects.values('rate')
    conditons={'rate__gte':3}
    plus=queryset.filter(**conditons).count()

    return render(request,'result.html',locals())

