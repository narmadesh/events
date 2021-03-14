from django.shortcuts import render
from django.http import HttpResponse
from .models import Events
from django.shortcuts import redirect


def index(request):
	events = Events.objects.all()
	return render(request, 'index.html', {'events':events})

def events(request):
	event_name = request.POST.get('event_name')
	date = request.POST.get('date')
	time = request.POST.get('time')
	location = request.POST.get('location')
	image = request.FILES.get('image')
	event = Events(event_name=event_name, date=date, time=time, location=location, image=image, is_liked=False)
	if event.save():
		return redirect('index');
	else:
		return redirect('index');


def like(request):
	event_id = request.POST.get('like')
	like = Events.objects.filter(id=event_id).update(is_liked=True)
	if like:
		return HttpResponse('Liked')
	else:
		return HttpResponse('Failed')


def unlike(request):
	event_id = request.POST.get('unlike')
	unlike = Events.objects.filter(id=event_id).update(is_liked=False)
	if like:
		return HttpResponse('Unliked')
	else:
		return HttpResponse('Failed')