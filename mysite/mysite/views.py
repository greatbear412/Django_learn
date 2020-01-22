from django.shortcuts import render, get_object_or_404


def not_found(request, exp):
    return render(request,'mysite/404.html')