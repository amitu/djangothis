from django.core.management.base import BaseCommand, CommandError
import sys
from pprint import pprint

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        pprint(sys.modules)
        for poll_id in args:
            self.stdout.write('Successfully closed poll "%s"\n' % poll_id)
