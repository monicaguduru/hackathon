"""# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here."""
from django.shortcuts import render,get_object_or_404
from .models import Sensors
from django.http import HttpResponse
from django.forms.models import model_to_dict
def aaa(request):
	"""all_sensors = Sensors.objects.all()"""
	all_sensors = Sensors.objects.all()
	return render(request ,'sensors/aaa.html',{'all_sensors':all_sensors})
	#return HttpResponse(template.render(context,request))


def Display(request,ps=None,ss=None,dw=None,spw=None,tpw=None):
    all_sensors = Sensors()
    #all_sensors = Sensors.objects.all()
    #if (sensor1 != None):
    all_sensors.ps=float(ps)
    all_sensors.ss=float(ss)
    all_sensors.dw=float(dw)
    all_sensors.spw=float(spw)
    all_sensors.tpw=float(tpw)
    #print(all_sensors.dw)
    all_sensors.save()
    return render(request ,'sensors/sensors.html',{'all_sensors':all_sensors})
	#return render(request ,'sensors/detail.html',{'all_sensors':all_sensors})"""
def new_disp(request):
    all_sensors = Sensors.objects.get(pk=Sensors.objects.count())
    return render(request ,'sensors/sensors.html',{'all_sensors':all_sensors})



