from django.http import HttpResponse
from django.shortcuts import render, redirect

from visits.models import PageVisits
def home_page_view(request, *args, **kwargs):
    my_title = "My Title"
    queryset = PageVisits.objects.all()
    my_context = {
        "title": my_title,
        "page_visits_count": queryset.count()
    }
    PageVisits.objects.create()
    return render(request, 'home.html',my_context)