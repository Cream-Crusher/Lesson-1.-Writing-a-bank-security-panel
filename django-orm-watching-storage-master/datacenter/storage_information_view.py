import datetime
from datacenter.models import Visit
from django.shortcuts import render

def get_duration(duration, hour=datetime.timedelta(hours=1)):

    if duration > hour:
        return True
    else:
        return False


def storage_information_view(request):
    # Программируем здесь
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for visit in visits:

        duration = visit.get_duration()
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': duration,
                'is_strange': get_duration(duration)
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
