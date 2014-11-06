import json
import urllib
import requests
from django.views.generic import View, FormView, ListView
from django.shortcuts import render, redirect
from .forms import SearchForm

class SearchRestaurant(FormView):
    form_class = SearchForm
    template_name = 'restaurant/search_restaurant_form.html'
    success_url = '/restaurants/results'

    def form_valid(self,form):
        response = redirect('search_results')
        response['Location'] += '?query=%s' % form.cleaned_data['search']
        return response

class SearchResults(View):
    def get(self, request):

        geo = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=%s&API_KEY=AIzaSyC_gRLQGYxjQ7ij56u-kFTTA2USh_gxnmw" % request.GET.get('query')).json()

        location = geo['results'][0]['geometry']['location']

        places = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s,%s&radius=500&types=food&key=AIzaSyC_gRLQGYxjQ7ij56u-kFTTA2USh_gxnmw' % (location['lat'], location['lng'])).json()

        results = []
        for p in places['results']:
            result = {}
            result['icon'] = p['icon']
            result['name'] = p['name']
            if 'rating' in p:
                result['rating']= p['rating']
            if 'price_level' in p:
                result['price_level']= p['price_level']

            results.append(result)

        return render(request, 'restaurant/search_results.html', {'results': results})

