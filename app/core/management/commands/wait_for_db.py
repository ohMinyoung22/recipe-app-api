from django.core.management.base import BaseCommand

from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

import time

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("wait for db ..")
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('db unavailable, wait for a secodn..')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('DB CONNECTED'))
