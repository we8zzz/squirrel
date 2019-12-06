import csv
from django.core.management import BaseCommand
from sightings.models  import squirrel

class Command(BaseCommand):
    help = 'Import Data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        import datetime
        path = kwargs['path']
        with open(path) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                for i in (15,16,17,18,19,21,22,23,24,25,26,27,28):
                    if row[i] == 'false' or row[i] == 'FALSE':
                        row[i] = False
                    else:
                        row[i] = True

                longitude = row[0]
                latitude = row[1]
                unique_squirrel_id = row[2]
                shift = row[4]
                date = datetime.datetime.strptime(row[5],"%m%d%Y").strftime("%Y-%m-%d")
                age = row[7]
                primary_fur_color = row[8]
                location = row[12]
                specific_location = row[14]
                running = row[15]
                chasing = row[16]
                climbing = row[17]
                eating = row[18]
                foraging = row[19]
                other_activities = row[20]
                kuks = row[21]
                quaas = row[22]
                moans = row[23]
                tail_flags = row[24]
                tail_twitches = row[25]
                approaches = row[26]
                indifferent = row[27]
                run_from = row[28]

                db = squirrel(longitude = longitude, latitude = latitude, unique_squirrel_id = unique_squirrel_id, shift = shift, date = date, age = age, primary_fur_color = primary_fur_color, location = location, specific_location = specific_location, running = running, chasing = chasing, climbing = climbing, eating = eating, foraging = foraging, other_activities = other_activities, kuks = kuks, quaas=quaas, moans=moans, tail_flags = tail_flags,tail_twitches = tail_twitches, approaches = approaches, indifferent = indifferent, runs_from = run_from)

                db.save()
