from django.shortcuts import render

# Create your views here.
'''chang: ->'''
from django.http import HttpResponse
from .models import ParkingLot
from .models import ParkingSpot
from .models import Address
from .models import Payment
from parking.forms import BookSpot

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(request):
    #    latest_question_list = ParkingSpot.objects.order_by('-lot_id')[:5]
    latest_question_list = ParkingSpot.objects.all()
    context = {'latest_question_list': latest_question_list}
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
#        print (ParkingSpot.objects.filter(spot_user=self.request.user).filter(spot_occupancy='o').all())
        return ParkingSpot.objects.filter(spot_user=self.request.user).filter(spot_occupancy='o').all()

def book(request, pk):
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = BookSpot(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#            book_instance.due_back = form.cleaned_data['renewal_date']
#            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = BookSpot(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        }

    return render(request, 'parking/book.html', context)

'''<- chang'''

