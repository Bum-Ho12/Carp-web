from django.shortcuts import render,redirect, get_object_or_404
from .models import book, activity,notification, album
from .form import bookForm, activityForm,notificationForm, albumForm
from .serialiser import Book, Activity,Notification,Album
from django.http import JsonResponse,  HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

def bookView(request):
    form= bookForm( request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form .is_valid():
            form.save()
        return redirect('bookls')
    return render(request,'index.html',{'form':form})

def activityView(request):
    form= activityForm( request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form .is_valid():
            form.save()
        return redirect('activityls')
    return render(request,'activity.html',{'form':form})

def albumView(request):
    form= albumForm( request.POST or None)
    if request.method == 'POST':
        if form .is_valid():
            form.save()
        return redirect('albumls')
    return render(request,'album.html',{'form':form})


def notificationView(request):
    form= notificationForm( request.POST or None)
    if request.method == 'POST':
        if form .is_valid():
            form.save()
        return redirect('notificationls')
    return render(request,'notification.html',{'form':form})

def bookList(request):
    qs= book.objects.all()
    context={
        "books":qs,
    }
    template='bookList.html'
    return render(request,template,context)

def activityList(request):
    qs= activity.objects.all()
    context={
        "activities":qs,
    }
    template='activityList.html'
    return render(request,template,context)

def albumList(request):
    qs= album.objects.all()
    context={
        "albums":qs,
    }
    template='albumList.html'
    return render(request,template,context)

def notificationList(request):
    ls= notification.objects.all()
    context={
        "notifications":ls,
    }
    template='notificationList.html'
    return render(request,template,context)

def bookDetail(request, pk):
    obj = get_object_or_404(book, pk=pk)
    context={
        "object":obj,
    }
    template='bookDetail.html'
    return render(request,template,context)

def activityDetail(request, pk):
    obj = get_object_or_404(activity, pk=pk)
    context={
        "object":obj,
    }
    template='activityDetail.html'
    return render(request,template,context)

def albumDetail(request, pk):
    obj = get_object_or_404(album, pk=pk)
    context={
        "object":obj,
    }
    template='albumDetail.html'
    return render(request,template,context)



def notificationDetail(request, pk):
    obj = get_object_or_404(notification, pk=pk)
    context={
        "object":obj,
    }
    template='notificationDetail.html'
    return render(request,template,context)

def bookUpdate(request,pk):
    Book= get_object_or_404(book, pk=pk)
    form= bookForm(instance=Book)
    context={'form':form}
    if request.method == 'POST':
        form= bookForm(request.POST, request.FILES or None,instance=Book)
        if form .is_valid():
            form.save()
        return redirect('bookls')
    template='index.html'
    return render(request,template,context)

def activityUpdate(request,pk):
    Activity= get_object_or_404(activity, pk=pk)
    form= activityForm(instance=Activity)
    context={'form':form}
    if request.method == 'POST':
        form= activityForm(request.POST, request.FILES or None, instance=Activity)
        if form .is_valid():
            form.save()
        return redirect('activityls')
    template='activity.html'
    return render(request,template,context)

def albumUpdate(request,pk):
    Album= get_object_or_404(album, pk=pk)
    form= albumForm(instance=Album)
    context={'form':form}
    if request.method == 'POST':
        form= albumForm(request.POST, request.FILES or None, instance=Album)
        if form .is_valid():
            form.save()
        return redirect('albumls')
    template='album.html'
    return render(request,template,context)


def notificationUpdate(request,pk):
    Notification= get_object_or_404(notification, pk=pk)
    form= notificationForm(instance=Notification)
    context={'form':form}
    if request.method == 'POST':
        form= notificationForm(request.POST, instance=Notification)
        if form .is_valid():
            form.save()
        return redirect('notificationls')
    template='notification.html'
    return render(request,template,context)

def bookDelete(request,pk):
    Book= get_object_or_404(book, pk=pk)
    if request.method=='POST':
        Book.delete()
        return redirect('bookls')
    template= 'bookDelete.html'
    context={'item': Book}
    return render(request,template,context)

def activityDelete(request,pk):
    Activity= get_object_or_404(activity, pk=pk)
    if request.method=='POST':
        Activity.delete()
        return redirect('activityls')
    template= 'activityDelete.html'
    context={'item': Activity}
    return render(request,template,context)

def albumDelete(request,pk):
    Album= get_object_or_404(album, pk=pk)
    if request.method=='POST':
        Album.delete()
        return redirect('albumls')
    template= 'albumDelete.html'
    context={'item': Album}
    return render(request,template,context)


def notificationDelete(request,pk):
    Notification= get_object_or_404(notification, pk=pk)
    if request.method=='POST':
        Notification.delete()
        return redirect('notificationls')
    template= 'notificationDelete.html'
    context={'item': Notification}
    return render(request,template,context)

"""@api_view(['GET'])
def BookView(request,pk):
    id=request.query_params['pk']
    if id!=None:
        ob = book.objects.get(pk=pk)
        serialiser=Book(ob)
    return Response(serialiser.data)"""

@api_view(['GET'])
def BookView(request):
    ob = book.objects.all()
    serialiser = Book(ob, many=True)
    return Response(serialiser.data)


@api_view(['GET'])
def ActivityView(request):
    ob = activity.objects.all()
    serialiser = Activity(ob, many=True)
    return Response(serialiser.data)

@api_view(['GET'])
def AlbumView(request):
    ob = album.objects.all()
    serialiser = Album(ob, many=True)
    return Response(serialiser.data)

@api_view(['GET'])
def NotificationView(request):
    ob = notification.objects.all()
    serialiser = Notification(ob, many=True)
    return Response(serialiser.data)