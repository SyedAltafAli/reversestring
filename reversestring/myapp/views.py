from django.shortcuts import render
from django.http import JsonResponse

def reverse_string(request):
    reversed_str = ''
    if request.method == 'POST':
        input_str = request.POST.get('input')
        reversed_str = input_str[::-1]
    return render(request, 'reverse_string.html', {'reversed': reversed_str})


