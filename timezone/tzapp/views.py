from django.shortcuts import redirect, render
from django.http import HttpResponse
import pytz

def dummy_view(request):
    print("hi")
    return HttpResponse("hi")

def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'template.html', {'timezones': pytz.common_timezones})
