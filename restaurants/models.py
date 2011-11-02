from django.db import models

class Location(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    def __unicode__(self):
        return self.address

class Rating(models.Model):
    rating = models.CharField(max_length=200)
    rating_agency = models.CharField(max_length=200)
    def __unicode__(self):
        return self.rating

class RestaurantType(models.Model):
    restaurant_type = models.CharField(max_length=200)
    def __unicode__(self):
        return self.restaurant_type

class CuisineType(models.Model):
    cuisine_type = models.CharField(max_length=200)
    def __unicode__(self):
        return self.cuisine_type

class Restaurants(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location)
    restaurant_type = models.ManyToManyField(RestaurantType)
    cuisine_type = models.ManyToManyField(CuisineType)
    rating = models.ManyToManyField(Rating)
    def __unicode__(self):
        return self.name



