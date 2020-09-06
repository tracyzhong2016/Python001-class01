import json

from django.shortcuts import render

# Create your views here.
from .models import Smzdm1
from django.db.models import Avg

def mobile_comments(request):
    shorts = Smzdm1.objects.all()
    # 评论数量
    counter = Smzdm1.objects.all().count()


    # 平均星级
    # star_value = Smzdm1.objects.values('n_star')
    # star_avg =f" {Smzdm1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "
    # 情感倾向
    # sent_avg =f" {Smzdm1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    # 正向数量
    # queryset = Smzdm1.objects.values('sentiment')
    # condtions = {'sentiment__gte': 0.5}
    # plus = queryset.filter(**condtions).count()
    #
    # # 负向数量
    # queryset = Smzdm1.objects.values('sentiment')
    # condtions = {'sentiment__lt': 0.5}
    # minus = queryset.filter(**condtions).count()

    return render(request, 'index.html',locals())