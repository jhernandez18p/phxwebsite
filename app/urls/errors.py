"""
Custom error views
"""
def bad_request_view(request):
    context = {
        'pg_title':'',
        'title':'',
    }
    n_error = '400'
    template = 'errors/400.html'
    return render(request, template, status=400)

def permission_denied_view(request):
    context = {
        'pg_title':'',
        'title':'',
    }
    n_error = '403'
    template = 'errors/403.html'
    return render(request, template, status=403)

def page_not_found_view(request):
    context = {
        'pg_title':'',
        'title':'',
    }
    n_error = '404'
    template = 'errors/404.html'
    return render(request, template, status=404)

def error_view(request):
    context = {
        'pg_title':'',
        'title':'',
    }
    n_error = '500'
    template = 'errors/500.html'
    return render(request, template, status=500)