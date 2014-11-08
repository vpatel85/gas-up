import json
import urllib
import requests
from django.http import HttpResponse
from django.views.generic import View, FormView, ListView, DetailView
from django.shortcuts import render, redirect
from .forms import SearchForm, CommentForm, SubCommentForm
from .models import Restaurant, Comment

class SearchRestaurant(FormView):
    form_class = SearchForm
    template_name = 'search_restaurant_form.html'
    success_url = '/restaurants/results'

    def form_valid(self,form):
        response = redirect('search_results')
        response['Location'] += '?query=%s' % form.cleaned_data['search']
        return response

class SearchResults(View):
    def get(self, request):

        #need to make this whole thing better
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

        return render(request, 'search_results.html', {'results': results})

class AddRestaurant(View):
    def get(self, request):
        icon = request.GET.get('icon')
        name = request.GET.get('name')
        rating = request.GET.get('rating')
        price_level = request.GET.get('price_level')

        try:
            r, created = Restaurant.objects.get_or_create(icon=icon, name=name, google_rating=rating, price_level=price_level)
            return redirect('restaurant_list')
        except Exception, e:
            print e

class RestaurantList(ListView):
    model = Restaurant

class RestaurantDetail(FormView):
    template_name = 'restaurants/restaurant_detail.html'
    model = Restaurant
    form_class = CommentForm

    def get_initial(self):
        restaurant = Restaurant.objects.get(pk=self.kwargs['pk'])
        return {'user':self.request.user, 'restaurant':restaurant}

    def get_context_data(self, **kwargs):
        context = super(RestaurantDetail, self).get_context_data(**kwargs)
        context['object'] = Restaurant.objects.get(pk=self.kwargs['pk'])

        comments = Comment.objects.filter(restaurant=context['object']).order_by('-created')
        context['comments'] = comments

        context['sub_comment_form'] = SubCommentForm(initial={'user':self.request.user})

        return context

    def form_valid(self, form):
        form.save()
        return redirect('restaurant_detail', pk=self.kwargs['pk'])

class SubCommentView(FormView):
    form_class = SubCommentForm

    def post(self, request, pk):
        parent = Comment.objects.get(pk=self.kwargs['pk'])
        form = SubCommentForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Thank you for your comment'
        else:
            msg = 'This field is required'

        response = HttpResponse(json.dumps(msg), content_type="application/json")
        return response
