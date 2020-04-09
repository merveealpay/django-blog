from django.shortcuts import render, HttpResponse


def post_index(request):
    return HttpResponse('Index page')


def post_detail(request):
    return HttpResponse('Detail page')


def post_create(request):
    return HttpResponse('Create page')


def post_update(request):
    return HttpResponse('Update page')


def post_delete(request):
    return HttpResponse('Delete page')
