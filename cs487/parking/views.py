from django.shortcuts import render

# Create your views here.
'''chang: ->'''
from django.http import HttpResponse
from .models import ParkingLot
from .models import ParkingSpot
from .models import Address
from .models import Payment
#from parking.forms import BookSpot
from parking.forms import BookTime
#from parking.forms import BookMinute

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count
from datetime import timedelta

@login_required
def index(request):
    #    latest_question_list = ParkingSpot.objects.order_by('-lot_id')[:5]
    lot_list = ParkingLot.objects.order_by('lot_id')
    empty_count_list = ParkingSpot.objects.values('lot_id', 'spot_occupancy').annotate(number_spots=Count('spot_occupancy')).filter(spot_occupancy = 'n').order_by('lot_id').values_list('number_spots', flat=True)
    print(list(empty_count_list))
    latest_question_list = zip(lot_list, empty_count_list)
    context = {'latest_question_list': latest_question_list,
            }
    return render(request, 'parking/index.html', context)

@login_required
def detail(request, lot_id):
    latest_question_list = ParkingSpot.objects.filter(lot_id__lot_id = lot_id)
    lot_name = ParkingLot.objects.filter(lot_id = lot_id).values('lot_name')[0]['lot_name']
    lot_hours = ParkingLot.objects.filter(lot_id = lot_id).values('lot_hours')[0]['lot_hours']
    address_id = ParkingLot.objects.filter(lot_id = lot_id).values('lot_address')[0]['lot_address']
    lot_address = Address.objects.filter(address_id = address_id)[0]

    context = {'latest_question_list': latest_question_list,
            'lot_id': lot_id,
            'lot_name': lot_name,
            'lot_hours': lot_hours,
            'lot_address': lot_address
            }    

    return render(request, 'parking/detail.html', context)


class MySpots(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = ParkingSpot
    context_object_name = 'bookinstance_list' 
    template_name ='parking/myspots.html'
    paginate_by = 10
    def get_queryset(self):
        return ParkingSpot.objects.filter(spot_user=self.request.user).filter(spot_occupancy='o').all()


@permission_required('parking.booked')
def book(request, spot_id):
    book_instance = get_object_or_404(ParkingSpot, spot_id=spot_id)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
#        form = BookSpot(request.POST)
        form1 = BookTime(request.POST)
#        form2 = BookMinute(request.POST)
        # Check if the form is valid:
        if form1.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.booked_time = form1.cleaned_data['renewal_time']
            book_instance.spot_occupancy = 'o'
            book_instance.spot_user = request.user

            booked_minute = form1.cleaned_data['renewal_minute']
            book_instance.end_time = book_instance.booked_time + timedelta(minutes = booked_minute)
            book_instance.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('parking:myspots') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_time = datetime.datetime.now()
        proposed_renewal_minute = 30
        form1 = BookTime(initial={'renewal_time': proposed_renewal_time, 'renewal_minute': proposed_renewal_minute})
#        form2 = BookTime(initial={'renewal_minute': proposed_renewal_minute})

    context = {
        'form1': form1,
        'book_instance': book_instance,
        }

    return render(request, 'parking/book.html', context)

'''<- chang'''

