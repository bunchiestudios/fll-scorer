from django.db import models

class Season(models.Model):
    year = models.IntegerField(primary_key=True)
    json_shema = models.TextField()

    def __str__(self):
        return "year=%s" % self.year

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    admin = models.BooleanField()

    def __str__(self):
        return "name='%s', email='%s', admin=%s" % (self.name, self.email, self.admin)

class Event(models.Model):
    name = models.CharField(max_length=255, unique=True)
    date_start = models.DateField()
    date_end = models.DateField()

    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return "name='%s', date_start='%s', date_end='%s'" % (self.name, self.date_start, self.date_end)

class Team(models.Model):
    name = models.CharField(max_length=255)
    team_number = models.IntegerField(primary_key=True)

    def __str__(self):
        return "name='%s', team_number=%d" % (self.name, self.team_number)


class Scorekeeper(models.Model):
    PRIVILEGES = (
        ('AD', 'Admin'),
        ('SC', 'Score Keeper'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    privilege = models.CharField(max_length=2, choices=PRIVILEGES)
    
    class Meta:
        unique_together = ('user', 'event')
    
    def __str__(self):
        return "user_name='%s', event_name='%s', privilege='%s'" % (self.user.name, self.event.name, self.privilege)



class Enrollment(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    practice_data = models.TextField(null=True)
    match1_data = models.TextField(null=True)
    match2_data = models.TextField(null=True)
    match3_data = models.TextField(null=True)

    practice_noshow = models.NullBooleanField()
    match1_noshow = models.NullBooleanField()
    match2_data = models.NullBooleanField()
    match3_data = models.NullBooleanField()

    class Meta:
        unique_together = ('team', 'event')
    
    def __str__(self):
        return "team_number=%d, event_name='%s'" % (self.team.team_number, self.event.name)
