from django.views.generic import FormView
from .forms import SearchForm

class SearchRestaurant(FormView):
    form_class = SearchForm
    template_name = 'search_restaurant_form.html'

    def form_valid(self,form):
        return super(SearchView, self).form_valid(form)

