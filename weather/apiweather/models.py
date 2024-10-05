from django.db import models

# Create your models here.
DESCRIPTIONS = (
    (0, "Sunny"),
    (1, "Rain"),
    (3, "Cloudy"),
    (4, "Snow"),
    (5, "Partly Cloudy"),
    (6, "Mostly Cloudy"),
)


class Description(models.Model):
    weather_description = models.IntegerField(choices=DESCRIPTIONS, default=0)
    temperature = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.created_on)