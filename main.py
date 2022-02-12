import os
import datetime
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    post_passcards = Passcard.objects.all()
    post_passcard = post_passcards[0]
    pass_cards = {
        'owner_name': post_passcard.owner_name,
        'passcode': post_passcard.passcode,
        'created_at': '{}'.format(post_passcard.created_at),
        'is_active': post_passcard.is_active
    }
    active_post_passcards = post_passcards.filter(is_active=True)
    #print(len(active_post_passcards))
    #print(pass_cards)
    #print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    Visits = Visit.objects.all()
    unclosed_visits = Visits.filter(leaved_at=None)

    for num in range(len(unclosed_visits)):

        entered_at = unclosed_visits[num].entered_at
        located_in = django.utils.timezone.localtime().replace(microsecond=0) -entered_at
        passcard = unclosed_visits[num].passcard

        print('{}\nЗашёл в хранилище, время по Москве: {}\nНаходится в хранилище: {}'.format(passcard, entered_at, located_in))
