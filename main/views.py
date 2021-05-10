from django.shortcuts import render
from django.http import HttpResponse
import easypost 
import json
from .forms import searchPost

easypost.api_key = "EZTK9926332bdce64f5497b58fe743fcf653dIhj5YuJMXD3chpOP735qQ"

tracker = easypost.Tracker.create(
    tracking_code="EZ1000000001"
)
peso = tracker['weight']
stato = tracker['status']
dettagli = tracker['tracking_details']
data_consegna = tracker['est_delivery_date']

def track(code):
	track.tracker = easypost.Tracker.create(
    	tracking_code= code
	)
	track.peso = tracker['weight']
	track.stato = tracker['status']
	track.dettagli = tracker['tracking_details']
	track.data_consegna = tracker['est_delivery_date']
	track.corriere = tracker['carrier']
	track.da_pagare = tracker['fees']

mauro = track('EZ3000000003')
print(mauro)


def index(request):
	form = searchPost()
	args = {
		'form':form,
	}
	return render(request, 'main/index.html', args)

def track_page(request):
	form = searchPost()
	if request.method == 'GET':
		form_info = searchPost(request.GET)
		if form_info.is_valid():
			code = form_info.cleaned_data['code']
			track_post = track(code)
			peso = track.peso
			stato = track.stato
			dettagli = track.dettagli
			data_consegna = track.data_consegna
			da_pagare = track.da_pagare
			corriere = track.corriere
			args = {
				'da_pagare':da_pagare,
				'corriere':corriere,
				'tracker':tracker,
				'code':code,
				'form':form,
				'data_consegna':data_consegna,
				'peso':peso,
				'stato':stato,
				'dettagli':dettagli
				}
		return render(request, 'main/track.html', args)
	else: 
		return HttpResponse("<h1>Something went wrong</h1><br><a href='/'>Go to home page</a>")
