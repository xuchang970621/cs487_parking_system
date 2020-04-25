from django.shortcuts import render

# Create your views here.
'''chang: ->'''
from django.http import HttpResponse
from .models import ParkingLot
from .models import ParkingSpot
from .models import Address
from .models import Payment



from django.shortcuts import render

def index(request):
#    latest_question_list = ParkingSpot.objects.order_by('-lot_id')[:5]
    latest_question_list = ParkingSpot.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'parking/index.html', context)

def detail(request, lot_id):
    latest_question_list = ParkingSpot.objects.filter(lot_id__lot_id = lot_id)
    lot_name = ParkingLot.objects.filter(lot_id = lot_id).values('lot_name')[0]['lot_name']
    lot_hours = ParkingLot.objects.filter(lot_id = lot_id).values('lot_hours')[0]['lot_hours']
    context = {'latest_question_list': latest_question_list,
            'lot_id': lot_id,
            'lot_name': lot_name,
            'lot_hours': lot_hours
            }    
    return render(request, 'parking/detail.html', context)

'''<- chang'''

