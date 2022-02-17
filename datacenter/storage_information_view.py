from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    
    unclosed_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for unclosed_visit in unclosed_visits:

        duration = unclosed_visit.get_duration()
        is_strange = unclosed_visit.check_duration()

        non_closed_visits.append(
            {
                'who_entered': unclosed_visit.passcard.owner_name,
                'entered_at': unclosed_visit.entered_at,
                'duration': duration,
                'is_strange': is_strange
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
