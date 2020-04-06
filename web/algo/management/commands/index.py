from django.core.management.base import BaseCommand

from algo.indicies import Calculation


class Command(BaseCommand):
    help = 'Reset index'

    def add_arguments(self, parser):
        parser.add_argument('--reset', action='store_true', default=False, required=False)

    def handle(self, *args, **options):
        reset = options.get('reset')

        print(options)
        try:
            index = Calculation._index

            if reset:
                index.delete()

            if not index.exists():
                Calculation.init()
                print(f'{Calculation} index initialised')

        except Exception as e:
            print(f'{e}')
