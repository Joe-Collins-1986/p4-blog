from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.contrib.auth.models import User
from django.views.generic import (
    View,
    ListView,
)
from .models import Country, Visit
from .forms import VisitForm


class MapView(ListView):
    model = Country
    template_name = 'map/home.html'
    context_object_name = 'countries'


class CountryView(View):

    def get(self, request, pk):
        countries = Country.objects.all()
        country = get_object_or_404(countries, pk=pk)

        visited = Visit.objects.filter(user_id=request.user.id)

        if visited.filter(country=country).exists():
            country_visited = visited.get(country=country)

            return render(
                    request,
                    "map/country.html",
                    {
                        "country": country,
                        "visit_form": VisitForm(instance=country_visited)
                    },
            )
        else:
            return render(
                    request,
                    "map/country.html",
                    {
                        "country": country,
                        "visit_form": VisitForm()
                    },
            )

    def post(self, request, pk, *args, **kwargs):
        countries = Country.objects.all()
        country = get_object_or_404(countries, pk=pk)
        visited = Visit.objects.filter(user_id=request.user.id)

        print(visited)

        if visited.filter(country=country).exists():
            country_visited = visited.get(country=country)

            visit_form = VisitForm(data=request.POST)
            if visit_form.is_valid():
                visit_form.instance.user_id = request.user.id
                visit_form.instance.country = country
                visit_form.instance.id = country_visited.id
                country_visited = visit_form.save(commit=False)
                country_visited.save()
                print(country_visited.id)
            else:
                visit_form = VisitForm()

        else:
            visit_form = VisitForm(data=request.POST)
            if visit_form.is_valid():
                visit_form.instance.user_id = request.user.id
                visit = visit_form.save(commit=False)
                visit.country = country
                visit.save()
            else:
                visit_form = VisitForm()

        return HttpResponseRedirect(reverse('country', args=[pk]))
