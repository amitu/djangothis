from django.core.management.base import NoArgsCommand
import os

class Command(NoArgsCommand):
    help = 'Run Gunicorn'

    def handle_noargs(self, **options):
        os.execlp("gunicorn", "gunicorn", "djangothis.app:d")

