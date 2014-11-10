import json
import urllib
import requests
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View, FormView, ListView, DetailView, UpdateView
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from .forms import SearchForm, CommentForm, SubCommentForm, UserProfileForm
from .models import Restaurant, Comment, UserProfile

class SearchRestaurant(FormView):
    form_class = SearchForm
    template_name = 'search_restaurant_form.html'
    success_url = reverse_lazy('search_results')

    def form_valid(self,form):
        response = redirect('search_results')
        response['Location'] += '?query=%s' % form.cleaned_data['search']
        return response

class SearchResults(View):
    api_key = settings.GOOGLE_API_KEY

    def get(self, request):

        #gets places based on address provided in search
        geo = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=%s&API_KEY=%s" % (request.GET.get('query'), self.api_key)).json()

        location = geo['results'][0]['geometry']['location']

        places = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s,%s&radius=500&types=food&key=%s' % (location['lat'], location['lng'], self.api_key)).json()

        results = []
        for p in places['results']:
            result = {}
            result['icon'] = p['icon']
            result['name'] = p['name']
            if 'rating' in p:
                result['rating']= p['rating']
            if 'price_level' in p:
                result['price_level']= p['price_level']

            p_location = p['geometry']['location']
            result['lat'] = p_location['lat']
            result['lng'] = p_location['lng']

            results.append(result)

        return render(request, 'search_results.html', {'results': results})

class AddRestaurant(View):
    api_key = settings.GOOGLE_API_KEY

    def get(self, request):
        icon = request.GET.get('icon')
        name = request.GET.get('name')
        rating = request.GET.get('rating')
        price_level = request.GET.get('price_level')
        lat = request.GET.get('lat')
        lng = request.GET.get('lng')

        #get address of added restaurant
        address = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&key=%s' % (lat, lng, self.api_key)).json()
        formatted_address = address['results'][0]['formatted_address']
        #add restaurant from search to DB
        try:
            r, created = Restaurant.objects.get_or_create(icon=icon, name=name, google_rating=rating, price_level=price_level, lat=lat, lng=lng, formatted_address=formatted_address)
            return redirect('restaurant_list')
        except Exception, e:
            #add better exception catching
            print e
            return redirect('search_results?query=%s' % request.GET.get('query'))

class RestaurantList(ListView):
    model = Restaurant
    context_object_name = 'restaurant'

    def post(self, request):
        restaurant = Restaurant.objects.get(pk=request.POST['restaurant_id'])
        if request.POST['vote'] == 'down':
            restaurant.down_vote += 1
        else:
            restaurant.up_vote += 1

        restaurant.save()

        response = HttpResponse(json.dumps('voted'), content_type="application/json")
        return response

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
        print request.POST
        parent = Comment.objects.get(pk=self.kwargs['pk'])
        form = SubCommentForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Thank you for your comment'
        else:
            msg = 'This field is required'

        response = HttpResponse(json.dumps(msg), content_type="application/json")
        return response

class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'restaurants/userprofile_form.html'

    def form_valid(self, form):
        form.save()
        return redirect('restaurant_list')

class RemoveRestaurantUser(View):

    def post(self, request, pk):
        user_profile = UserProfile.objects.get(user=request.user)

        if request.POST['group'] == 'visited':
            user_profile.visited.remove(user_profile.visited.get(pk=pk).id)
        elif request.POST['group'] == 'dislike':
            user_profile.dislike.remove(user_profile.dislike.get(pk=pk).id)

        response = HttpResponse(json.dumps('removed'), content_type="application/json")
        return response

class AddRestaurantUser(View):

    def post(self, request, pk):
        print 'test'
        user_profile = UserProfile.objects.get(user=request.user)

        if request.POST['group'] == 'visited':
            user_profile.visited.add(Restaurant.objects.get(pk=pk).id)
        elif request.POST['group'] == 'dislike':
            user_profile.dislike.add(Restaurant.objects.get(pk=pk).id)

        response = HttpResponse(json.dumps('added'), content_type="application/json")
        return response
