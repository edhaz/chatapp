from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Chatter


def index(request):
    latest_chatter_list = Chatter.objects.order_by('-date_joined')[:10]
    context = {
        'latest_chatter_list': latest_chatter_list,
    }
    return render(request, 'chat/index.html', context)


def detail(request, chatter_name):
    chatter = get_object_or_404(Chatter, name=chatter_name)
    return render(request, 'chat/detail.html', {'chatter': chatter})


def results(request, chatter_name):
    return HttpResponse(f"These are the votes for {chatter_name.capitalize()}'s messages.")


def vote(request, chatter_name):
    return HttpResponse(f"You're voting on {chatter_name.capitalize()}'s messages.")
