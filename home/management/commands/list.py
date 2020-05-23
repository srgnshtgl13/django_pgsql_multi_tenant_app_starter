from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from firmalar.models import Firma

class Command(BaseCommand):
    help = 'Semalar'

    def handle(self, *args, **options):
        firmalar = Firma.objects.all()
        cursor = connection.cursor()
        semalar = []
        try:
            cursor.execute("SELECT schema_name FROM information_schema.schemata")
            semalar = cursor.fetchall()
            # print(semalar)
            for firma in firmalar:
                
                if not ('{}'.format(firma.firmasema),) in semalar:
                    cursor.execute("create schema {}".format(firma.firmasema))
                    cursor.execute("SELECT schema_name FROM information_schema.schemata")
                    semalar = cursor.fetchall()
                    print("{} was created.".format(firma.firmasema))
                else:
                    print("{} exists.".format(firma.firmasema))
        finally:
            cursor.close()
        
        
        