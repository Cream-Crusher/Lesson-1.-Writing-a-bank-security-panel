import datetime
from datacenter.models import Visit
from django.shortcuts import render


def check_duration(duration, hour=datetime.timedelta(hours=1)):

    return duration > hour


def storage_information_view(request):

    unclosed_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for unclosed_visit in unclosed_visits:

        duration = unclosed_visit.get_duration()
        non_closed_visits.append(
            {
                'who_entered': unclosed_visit.passcard.owner_name,
                'entered_at': unclosed_visit.entered_at,
                'duration': duration,
                'is_strange': check_duration(duration)
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
