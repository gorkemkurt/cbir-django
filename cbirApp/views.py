from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from cbirApp.image_retrieval import get_similar_images


def image_list(request):
    return JsonResponse(get_similar_images(), safe=False)


# Create your views here.
def dest_image_view(request):
    if request.method == 'POST':
        form = DestImageForm(request.POST, request.FILES)

        if form.is_valid():
            form = form.save()
            return JsonResponse(get_similar_images(form.dest_image, form.feature_extraction_method), safe=False)
    else:
        form = DestImageForm()
    return JsonResponse("OK", safe=False)


def success(request):
    return JsonResponse('successfuly uploaded', safe=False)
