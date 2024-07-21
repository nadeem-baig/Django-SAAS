from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from visits.models import PageVisits
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def home_page_view(request, *args, **kwargs):
    my_title = "My Title"
    queryset = PageVisits.objects.all()
    my_context = {
        "title": my_title,
        "page_visits_count": queryset.count()
    }
    PageVisits.objects.create()
    return render(request, 'home.html',my_context)

@staff_member_required
def staff_page_view(request, *args, **kwargs):
    my_title = "My Title"
    queryset = PageVisits.objects.all()
    my_context = {
        "title": my_title,
        "page_visits_count": queryset.count()
    }
    PageVisits.objects.create()
    return render(request, 'home.html',my_context)