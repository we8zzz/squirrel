from django.db import models

class squirrel(models.Model):
    AM='AM'
    PM='PM'
    shift_choice = ((AM, 'am'),(PM, 'pm'))
    longitude = models.FloatField()
    latitude = models.FloatField()
    unique_squirrel_id = models.CharField(primary_key=True, max_length=30)
    shift = models.CharField(max_length=2, choices=shift_choice)
    date = models.CharField(max_length=10, blank=True)
    age = models.CharField(max_length=20, null=True, blank=True)
    primary_fur_color = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    specific_location = models.CharField(max_length=50, null=True, blank=True)
    running = models.BooleanField(default=False)
    chasing = models.BooleanField(default=False)
    climbing = models.BooleanField(default=False)
    eating = models.BooleanField(default=False)
    foraging = models.BooleanField(default=False)
    other_activities = models.CharField(max_length=100, null=True, blank=True)
    kuks = models.BooleanField(default=False)
    quaas = models.BooleanField(default=False)
    moans = models.BooleanField(default=False)
    tail_flags = models.BooleanField(default=False)
    tail_twitches = models.BooleanField(default=False)
    approaches = models.BooleanField(default=False)
    indifferent = models.BooleanField(default=False)
    runs_from = models.BooleanField(default=False)
