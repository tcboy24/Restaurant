from django.shortcuts import render_to_response
from restaurants.models import Restaurants, CuisineType, RestaurantType, Rating


def homepage(request):
    rests = Restaurants.objects.order_by('name')
    cuisines=CuisineType.objects.order_by('cuisine_type')
    restaurants=RestaurantType.objects.order_by('restaurant_type')
    ratings=Rating.objects.all()
    return render_to_response('homepage.html', {
        'rests': rests,
        'cuisines': cuisines,
        'restaurants': restaurants, 
        'ratings': ratings,  
    })

def detail(request, restaurants_id):
    rests = Restaurants.objects.get(id=restaurants_id)
    cuisines=CuisineType.objects.order_by('cuisine_type')
    restaurants=RestaurantType.objects.order_by('restaurant_type')
    ratings=Rating.objects.all()
    return render_to_response('detail.html', {
        'rests': rests,
        'cuisines': cuisines,
        'restaurants': restaurants,
        'ratings': ratings, 
    })

def cuisinedetail(request, cuisines_id):
    cuisine = CuisineType.objects.get(id=cuisines_id)
    rests= Restaurants.objects.filter(cuisine_type=cuisine)
    cuisines=CuisineType.objects.order_by('cuisine_type')
    restaurants=RestaurantType.objects.order_by('restaurant_type')
    ratings=Rating.objects.all()
    return render_to_response('cuisinedetail.html', {
        'cuisine': cuisine,
        'rests': rests,
        'cuisines': cuisines,
        'restaurants': restaurants,
        'ratings': ratings, 
    })
def restaurantdetail(request, restauranttype_id):
    restaurant = RestaurantType.objects.get(id=restauranttype_id)
    rests= Restaurants.objects.filter(restaurant_type=restaurant)
    cuisines=CuisineType.objects.order_by('cuisine_type')
    restaurants=RestaurantType.objects.order_by('restaurant_type')
    ratings=Rating.objects.all()
    return render_to_response('restaurantdetail.html', {
        'restaurant': restaurant,
        'rests': rests,
        'cuisines': cuisines,
        'restaurants': restaurants,
        'ratings': ratings, 
    })

def ratingdetail(request, rating_id):
    rating = Rating.objects.get(id=rating_id)
    rests= Restaurants.objects.filter(rating=rating)
    ratings=Rating.objects.order_by('rating')
    restaurants=RestaurantType.objects.order_by('restaurant_type')
    ratings=Rating.objects.all()
    cuisines=CuisineType.objects.order_by('cuisine_type')
    return render_to_response('ratingdetail.html', {
        'rating': rating,
        'rests': rests,
        'cuisines': cuisines,
        'restaurants': restaurants,
        'ratings':ratings,
    })

