from django.shortcuts import render
import time

# Create your views here.


def whoiam(request):
    browser = request.META['HTTP_USER_AGENT']
    ip_address = request.META['REMOTE_ADDR']
    current_time = time.strftime('%A %B, %d %Y %H:%M:%S')

    return render(request, 'whoiam.html', {'values': [browser, ip_address, current_time]})


def source_code(request):
    return render(request, 'source_code.html')
