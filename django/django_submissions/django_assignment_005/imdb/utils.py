from imdb.models import Actor,Movie,Director,Cast,Rating
from django.db.models import Q 
from django.db.models import *
def populate_database(actors_list, movies_list, directors_list, movie_rating_list):
    
    actor_a=[Actor(actor_id=actor['actor_id'],name=actor['name'],gender=actor['gender']) 
    for actor in actors_list
    ]
    Actor.objects.bulk_create(actor_a)  

    director_d=[Director(name=director)for director in directors_list]
    Director.objects.bulk_create(director_d)
    dir=Director.objects.all()
    movie_list,cast_list=[],[]
    for movies in movies_list:
        for d in dir:
            if(d.name==movies['director_name']):
                break
        movie_m=Movie(movie_id=movies['movie_id'],
                name=movies['name'],
                release_date=movies['release_date'],
                box_office_collection_in_crores=movies['box_office_collection_in_crores'],
                director_id=d.id)
        movie_list.append(movie_m)
    #Movie.objects.bulk_create(movie_list)
    #for movies in movies_list:
        #m1=Movie.objects.get(movie_id=movies['movie_id'])
        for actor_cast in movies['actors']:
            #a1=Actor.objects.get(pk=actor_cast['actor_id'])
            cast_c=Cast(actor_id=actor_cast['actor_id'],movie_id=movies['movie_id'],role=actor_cast['role'],is_debut_movie=actor_cast['is_debut_movie'])
            cast_list.append(cast_c)
            
    Movie.objects.bulk_create(movie_list)
    Cast.objects.bulk_create(cast_list)   
    

    rating_r=[
                Rating(movie_id=rating['movie_id'],
                rating_one_count=rating['rating_one_count'],
                rating_two_count=rating['rating_two_count'],
                rating_three_count=rating['rating_three_count'],
                rating_four_count=rating['rating_four_count'],
                rating_five_count=rating['rating_five_count']) for rating in movie_rating_list ]
    Rating.objects.bulk_create(rating_r)
        
        
def get_no_of_distinct_movies_actor_acted(actor_id):
    list=Movie.objects.filter(actors__actor_id=actor_id).distinct()
    return len(list)
    
    
def get_movies_directed_by_director(director_obj):
    return list(Movie.objects.filter(director=director_obj))
    
def get_average_rating_of_movie(movie_obj):
    #m1=Movie.objects.get(pk=movie_obj.movie_id)
    try:
        r1=movie_obj.rating
        one,two,three,four,five=r1.rating_one_count,r1.rating_two_count,r1.rating_three_count,r1.rating_four_count,r1.rating_five_count
        rate_sum=one*1+two*2+three*3+four*4+five*5
        rate_count=one+two+three+four+five
        if rate_sum:
            average=(rate_sum)/rate_count
            return average
    except Rating.DoesNotExist:return 0
    return 0

def get_sum_rating_of_movie(movie_obj):
    #m1=Movie.objects.get(pk=movie_obj.movie_id)
    try:
        r1=movie_obj.rating
        one,two,three,four,five=r1.rating_one_count,r1.rating_two_count,r1.rating_three_count,r1.rating_four_count,r1.rating_five_count
        rate_sum=one+two+three+four+five
        if rate_sum:
            return rate_sum
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



def remove_all_actors_from_given_movie(movie_object):
    movie_object.actors.clear()

    
def get_all_rating_objects_for_given_movies(movie_objs):
    return list(Rating.objects.filter(movie__in=movie_objs))


def get_movies_by_given_movie_names(movie_names):
    # movie_objs=Movie.objects.prefetch_related('cast_set','director').filter(name__in=movie_names)
    # list_of_movies=[]
    # for movie_obj in movie_objs:
    #     cast_list=[]
    
    #     for cast in movie_obj.cast_set.all():
    #         cast_list.append({
    #                 "actor":{
    #                     "name":cast.actor.name,
    #                     "actor_id":cast.actor.actor_id,
    #                 },
    #                 "role":cast.role,
    #                 "is_debut_movie":cast.is_debut_movie
    #                 })
                    
    #     list_of_movies.append({
    #         "movie_id":movie_obj.movie_id,
    #         "name":movie_obj.name,
    #         "cast":cast_list,
    #         "box_office_collection_in_crores":movie_obj.box_office_collection_in_crores,
    #         "release_date":str(movie_obj.release_date),
    #         "director_name":movie_obj.director.name,
    #         "average_rating":get_average_rating_of_movie(movie_obj),
    #         "total_number_of_ratings":get_sum_rating_of_movie(movie_obj)
    #     })
    cast_obj=Cast.objects.filter(movie__name__in=movie_names).select_related('actor','movie__director','movie__rating')
    return get_movies_by_given_cast_objects(cast_obj)


    

def get_movies_released_in_summer_in_given_years():
    x=Movie.objects.prefetch_related('cast_set').filter(release_date__month__range=(5,7),release_date__year__range=(2006,2009)).distinct()
    return get_movies_by_given_movie_objects(x)
    
def get_movie_names_with_actor_name_ending_with_smith():
    x=Movie.objects.filter(actors__name__iendswith='smith').values_list('name',flat=True).distinct()
    return list(x)
    
def get_movie_names_with_ratings_in_given_range():
    x=Rating.objects.filter(rating_five_count__range=(1000,3000)).values_list('movie__name',flat=True).distinct()
    return list(x)
    
def get_movie_names_with_ratings_above_given_minimum():
    x=Rating.objects.filter(Q(movie__release_date__year__range=(2001,2100)),(Q(rating_five_count__gte=500)|Q(rating_four_count__gte=1000)|Q(rating_three_count__gte=2000)|Q(rating_two_count__gte=4000)|Q(rating_one_count__gte=8000))).values_list('movie__name',flat=True).distinct()
    return list(x)
    
def get_movie_directors_in_given_year():
    x=Movie.objects.filter(release_date__year=2000).values_list('director__name',flat=True).distinct()
    return list(x)
    
    
def get_actor_names_debuted_in_21st_century():
    x=Movie.objects.filter(cast__is_debut_movie=True,release_date__year__range=(2001,2100)).values_list('actors__name',flat=True).distinct()
    return list(x)     
    
def get_director_names_containing_big_as_well_as_movie_in_may():
    x=Movie.objects.filter(name__contains='big').filter(release_date__month=5).values_list('director__name',flat=True).distinct()
    return list(x)
    
def get_director_names_containing_big_and_movie_in_may():
    x=Movie.objects.filter(name__contains='big',release_date__month=5).values_list('director__name',flat=True).distinct()
    return x

def reset_ratings_for_movies_in_this_year():
    Rating.objects.filter(movie__release_date__year=2000).update(rating_five_count=0,rating_four_count=0,rating_three_count=0,rating_two_count=0,rating_one_count=0)
    
    
#task1
def get_average_box_office_collections():
    x=Movie.objects.aggregate(avg=Avg('box_office_collection_in_crores'))
    if x['avg']!=None:
        return round(x["avg"],3)
    return 0
    
#task2
def get_movies_with_distinct_actors_count():
    return list(Movie.objects.annotate(actors_count=Count('actors',distinct=True)))
    
#task3
def get_male_and_female_actors_count_for_each_movie():
    f_count=Count('actors',filter=Q(actors__gender='FEMALE'),distinct=True)
    m_count=Count('actors',filter=Q(actors__gender='MALE'),distinct=True)
    x=Movie.objects.annotate(female_actors_count=f_count).annotate(male_actors_count=m_count)
    return list(x)

#task4
def get_roles_count_for_each_movie():
    return list(Movie.objects.annotate(roles_count=Count('cast__role',distinct=True)))
    
#task5
def get_role_frequency():
    dict={}
    x=Cast.objects.all().values_list('role').annotate(num_actors=Count('actor',distinct=True))
    dict.update(x)
    return dict
    
#task6
def get_role_frequency_in_order():
    x=Cast.objects.all().values_list('role').annotate(num_actors=Count('actor',distinct=True)).order_by('-movie__release_date')
    return list(x)
    
#task7                                                                                             
def get_no_of_movies_and_distinct_roles_for_each_actor():
    a=Actor.objects.annotate(movies_count=Count('movie',distinct=True),roles_count=Count('cast__role',distinct=True)) 
    return list(a)
    
#task8
def get_movies_with_atleast_forty_actors():
    m=Movie.objects.annotate(actors_count=Count('actors',distinct=True)).filter(actors_count__gte=40)    
    return list(m)

#task9
def get_average_no_of_actors_for_all_movies():
    x=Movie.objects.annotate(actors_count=Count('actors',distinct=True)).aggregate(avg=Avg('actors_count'))
    if x['avg']!=None:
        return round(x['avg'],3)
    return 0
    
    
#task8 5
def reset_ratings_for_movies_in_given_year(year):
    Rating.objects.filter(movie__release_date__year=year).update(rating_five_count=0,rating_four_count=0,rating_three_count=0,rating_two_count=0,rating_one_count=0)
    
def get_movies_by_given_cast_objects(cast_objects):
    #movie_objs=Movie.objects.filter(movie_id__in=movie_ids)
    list_of_movies=[]
    movies=[]
    for cast in cast_objects:
        #cast_obj=Cast.objects.filter(movie=movie_obj)      
        if cast.movie not in movies:
            cast_list=[]
            movie_obj=cast.movie
            list_of_movies.append({
            "movie_id":movie_obj.movie_id,
            "name":movie_obj.name,
            "cast":cast_list,
            "box_office_collection_in_crores":movie_obj.box_office_collection_in_crores,
            "release_date":str(movie_obj.release_date),
            "director_name":movie_obj.director.name,
            "average_rating":get_average_rating_of_movie(movie_obj),
            "total_number_of_ratings":get_sum_rating_of_movie(movie_obj)
            })
            movies.append(cast.movie)
    
        cast_list.append({
                        "actor":{
                                "name":cast.actor.name,
                                "actor_id":cast.actor.actor_id,
                            },
                            "role":cast.role,
                            "is_debut_movie":cast.is_debut_movie
                        })

        
    return list_of_movies    
    
    

#task6 5
def get_female_cast_details_from_movies_having_more_than_five_female_cast():
    female_count = Count('actors', distinct=True,filter=Q(actors__gender__iexact='FEMALE'))
    cast_objs=Cast.objects.filter(movie__in=(Movie.objects.annotate(count=female_count).filter(count__gt=5))).filter(actor__gender__iexact='FEMALE').select_related('actor','movie__director','movie__rating')
    return get_movies_by_given_cast_objects(cast_objs)
    
#task7 5
def get_actor_movies_released_in_year_greater_than_or_equal_to_2000():
    m=Movie.objects.filter(release_date__year__gt=2000).select_related('director','rating').prefetch_related('cast_set')
    a=Actor.objects.filter(movie__release_date__year__gte=2000).prefetch_related(Prefetch('movie_set',queryset=m,to_attr='movies_list')).distinct()
    list_actors=[]
    for actor in a:
        list_of_movies=[]
        for movie_obj in actor.movies_list:
            #cast_obj=Cast.objects.filter(movie=movie_obj)      
            cast_list=[]
            for cast in movie_obj.cast_set.all():
                if cast.actor_id==actor.actor_id:
                    cast_list.append({
                            "role":cast.role,
                            "is_debut_movie":cast.is_debut_movie
                            })
                        
            list_of_movies.append({
                "movie_id":movie_obj.movie_id,
                "name":movie_obj.name,
                "cast":cast_list,
                "box_office_collection_in_crores":movie_obj.box_office_collection_in_crores,
                "release_date":str(movie_obj.release_date),
                "director_name":movie_obj.director.name,
                "average_rating":get_average_rating_of_movie(movie_obj),
                "total_number_of_ratings":get_sum_rating_of_movie(movie_obj)
            
            })
        list_actors.append({
                "name":actor.name,
                "actor_id":actor.actor_id,
                "movies":list_of_movies
                })
    return list_actors