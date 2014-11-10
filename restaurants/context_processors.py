from .forms import SearchForm

#added this here because its used in everypage
def search_form(request):
    search_form = SearchForm()

    return {'search_form': search_form}

