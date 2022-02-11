import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    post_passcards = Passcard.objects.all()
    post_passcard = post_passcards[0]
    pass_cards = {
        'owner_name': post_passcard.owner_name,
        'passcode': post_passcard.passcode,
        'created_at': '{}'.format(post_passcard.created_at),
        'is_active': post_passcard.is_active
    }
    print(pass_cards)
    active_post_passcards = post_passcards.filter(is_active=True)
    print(len(active_post_passcards))