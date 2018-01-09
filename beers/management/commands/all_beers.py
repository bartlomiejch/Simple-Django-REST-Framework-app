from django.core.management.base import BaseCommand, CommandError
from beers.models import Beer


class Command(BaseCommand):
    help = 'Returns amount of beers in database'

    def handle(self, *args, **options):
        try:
            beers_number = Beer.objects.count()
        except Exception as ex:
            raise CommandError('Cannot get information from database because of %s' % ex)
        self.stdout.write(self.style.SUCCESS('Number of beers in database: %s' % beers_number))
