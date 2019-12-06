from django.core.management import BaseCommand
from sightings.models import squirrel
import csv

class Command(BaseCommand):
    help = 'Export Data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        qs = squirrel.objects.all()
        writer = csv.writer(open(path, 'w'), delimiter=',')

        headers = []
        for header in squirrel._meta.get_fields():
            headers.append(header.name)
        writer.writerow(headers)

        for data in qs:
            row = []
            for header in headers:
                value = getattr(data, header)
                row.append(value)
            writer.writerow(row)
