from imdb.models import Actor,Movie,Director,Cast,Rating
from django.db.models import Q 
def populate_database(actors_list, movies_list, directors_list, movie_rating_list):
    for actor in actors_list:
        actor_a=Actor(actor_id=actor['actor_id'],name=actor['name'])
        actor_a.save()

    for director in directors_list:
        director_d=Director(name=director)
        director_d.save()

    for movies in movies_list:
        d1= Director.objects.get(pk=movies['director_name'])
        movie_m=Movie(movie_id=movies['movie_id'],name=movies['name'],release_date=movies['release_date'],box_office_collection_in_crores=movies['box_office_collection_in_crores'],director=d1)
        movie_m.save()
        m1=Movie.objects.get(pk=movies['movie_id'])
        for actor_cast in movies['actors']:
            a1=Actor.objects.get(pk=actor_cast['actor_id'])
            Cast.objects.create(actor=a1,movie=m1,role=actor_cast['role'],is_debut_movie=actor_cast['is_debut_movie'])
            #print(cast_c)
        
    for rating in movie_rating_list:
        m1=Movie.objects.get(pk=rating['movie_id'])
        rating_r=Rating(movie=m1,rating_one_count=rating['rating_one_count'],rating_two_count=rating['rating_two_count'],rating_three_count=rating['rating_three_count'],rating_four_count=rating['rating_four_count'],rating_five_count=rating['rating_five_count'])
        rating_r.save()

    
def get_movies_by_given_movie_names(movie_names):
    movie_objs=Movie.objects.filter(name__in=movie_names)
    list_of_movies,cast_list=[],[]
    for movie_obj in movie_objs:
        cast_obj=Cast.objects.filter(moive=movie_obj)
        for cast in cast_obj: 
            cast_list.append({
                    "actor":{
                        "name":cast.actor.name,
                        "actor_id":cast.actor.actor_id,
                        },
                    "role":cast.role,
                    "is_debut_movie":cast.is_debut_movie,
                    })
        list_of_movies.append({
            "movie_id":movie_obj.movie_id,
            "name":movie_obj.name,
            "cast":cast_list,
            "box_office_collection_in_crores":movie_obj
        })
    
        
def get_no_of_distinct_movies_actor_acted(actor_id):
    list=Movie.objects.filter(actors__actor_id=actor_id).distinct()
    return len(list)
    
    
def get_movies_directed_by_director(director_obj):
    return list(Movie.objects.filter(director=director_obj))
    
def get_average_rating_of_movie(movie_obj):
    m1=Movie.objects.get(pk=movie_obj.movie_id)
    try:
        r1=Rating.objects.get(movie_id=m1.movie_id)
        one,two,three,four,five=r1.rating_one_count,r1.rating_two_count,r1.rating_three_count,r1.rating_four_count,r1.rating_five_count
        rate_sum=one*1+two*2+three*3+four*4+five*5
        rate_count=one+two+three+four+five
        if rate_sum:
            average=(rate_sum)/rate_count
            return average
    except Rating.DoesNotExist:return 0
    return 0
    
def delete_movie_rating(movie_obj):
    r1=Rating.objects.get(movie_id=movie_obj.movie_id)
    r1.delete()
    
def get_all_actor_objects_acted_in_given_movies(movie_objs):
    return list(Actor.objects.filter(movie__in=movie_objs).distinct())
    
    
    
def update_director_for_given_movie(movie_obj, director_obj):
    movie_obj.director=director_obj
    movie_obj.save()
    
def get_distinct_movies_acted_by_actor_whose_name_contains_john():
    return list(Movie.objects.filter(actors__name__contains='john').distinct())



def remove_all_actors_from_given_movie(movie_obj):
    movie_obj.actors.clear()

    
def get_all_rating_objects_for_given_movies(movie_objs):
    return list(Rating.objects.filter(movie__in=movie_objs))
    
def get_movie_names_with_ratings_in_given_range():
    return list(Movie.objects.filter(rating__rating_five_count__gte=1000,rating__rating_five_count__lte=3000).values_list('name',flat=True))
    
def get_movie_names_with_actor_name_ending_with_smith():
    return list(Movie.objects.filter(actors__name__endswith='smith').values_list('name',flat=True))
    
def get_movie_names_with_ratings_above_given_minimum():
    return list(Movie.objects.filter(release_date__year__gt=2000).filter(Q(rating__rating_five_count=500)|Q(rating__rating_four_count=1000)|Q(rating__rating_three_count=2000)|Q(rating__rating_two_count=4000)|Q(rating__rating_one_count=8000)).values_list('name',flat=True))
    
def get_actor_names_debuted_in_21st_century():
    return list(Movie.objects.filter(cast__is_debut_movie=True,release_date__year__gt=2000).values_list('actors__name',flat=True))            
    
def get_director_names_containing_big_as_well_as_movie_in_may():
    return list(Movie.objects.filter(name__contains='big').filter(release_date__month=5).values_list('director__name',flat=True))
    
def get_director_names_containing_big_and_movie_in_may():
    return list(Movie.objects.filter(name__contains='big',release_date__month=5).values_list('director__name',flat=True))
    
def reset_ratings_for_movies_in_this_year():
    Movie.objects.filter(release_date__year=2000).update(rating__rating_five_count=0,rating__rating_four_count=0,rating__rating_three_count=0,rating__rating_two_count=0,rating__rating_one_count=0)