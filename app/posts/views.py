from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):

    return HttpResponse('post_list')


def post_detail(request, pk):
    return HttpResponse(f'post_detail: {pk}')