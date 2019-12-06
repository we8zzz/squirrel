from django.db import models

class squirrel(models.Model):
    AM='AM'
    PM='PM'
    shift_choice = ((AM, 'am'),(PM, 'pm'))
    longitude = models.FloatField()
    latitude = models.FloatField()
    unique_squirrel_id = models.CharField(primary_key=True, max_length=30)
    shift = models.CharField(max_length=2, choices=shift_choice)
    date = models.CharField(max_length=10)
    age = models.CharField(max_length=20, null=True)
    primary_fur_color = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=50, null=True)
    specific_location = models.CharField(max_length=50, null=True)
    running = models.BooleanField(null=True)
    chasing = models.BooleanField(null=True)
    climbing = models.BooleanField(null=True)
    eating = models.BooleanField(null=True)
    foraging = models.BooleanField(null=True)
    other_activities = models.CharField(max_length=100, null=True)
    kuks = models.BooleanField(null=True)
    quaas = models.BooleanField(null=True)
    moans = models.BooleanField(null=True)
    tail_flags = models.BooleanField(null=True)
    tail_twitches = models.BooleanField(null=True)
    approaches = models.BooleanField(null=True)
    indifferent = models.BooleanField(null=True)
    runs_from = models.BooleanField(null=True)
