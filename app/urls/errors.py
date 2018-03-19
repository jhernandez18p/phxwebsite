from django.shortcuts import render

def bad_request_view(request):
    context = {
        'pg_title':'',
        'title':'',
    }
    n_error = '400'
    template = 'errors/400.html'
    context['status'] = n_error
    return render(request, template, context)

def permission_denied_view(request):
    context = {
        'pg_title':'',
        'title':'',
    }
    n_error = '403'
    template = 'errors/403.html'
    context['status'] = n_error
    return render(request, template, context)

def page_not_found_view(request):
    context = {
        'pg_title':'',
        'title':'',
    }
    n_error = '404'
    template = 'errors/404.html'
    context['status'] = n_error
    return render(request, template, context)

def error_view(request):
    context = {
        'pg_title':'',
        'title':'',
    }
    n_error = '500'
    template = 'errors/500.html'
    context['status'] = n_error
    return render(request, template, context)