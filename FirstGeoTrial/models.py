# from django.db import models

# # Create your models here.
# from django.db import models

# class Location(models.Model):
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Lat: {self.latitude}, Lng: {self.longitude} at {self.timestamp}"

from django.db import models

class UserLocation(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.lat}, {self.lng})"





