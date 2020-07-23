def profile():
    def decorator(func):
        def handler(*args, **kwargs):
            import line_profiler
            profiler = line_profiler.LineProfiler()
            profiler.enable_by_count()
            profiler.add_function(func)
            result = func(*args, **kwargs)
            profiler.print_stats()
            return result

        handler.__doc__ = func.__doc__
        return handler

    return decorator
    
@profile()
def my_function():
    import time
    time.sleep(2)
    print("Exiting my function")
    
@profile()
def get_books_by_library_id(book_ids):
    from optimize.models import Book
    from collections import defaultdict
    result = defaultdict(list)
   
    for book_id in book_ids:
        book = Book.objects.get(id=book_id)
        result[book.library_id].append(book)
    return result
    
@profile()
def get_books_by_library_id_one_query(book_ids):
    from optimize.models import Book
    from collections import defaultdict
    books = Book.objects.filter(id__in=book_ids)
    result = defaultdict(list)
    
    for book in books:
        result[book.library_id].append(book)
    return result
@profile()    
def get_books_by_author():
    from optimize.models import Book         
    from collections import defaultdict    
    books = Book.objects.all()
    result = defaultdict(list)
    for book in books:
        author = book.author
        title_and_author = '{} by {}'.format(
            book.title,
            author.name
        )
        result[book.library_id].append(title_and_author)
    return result
@profile()
def get_books_by_author_select_related():
    from optimize.models import Book
    from collections import defaultdict
    books = Book.objects.all().select_related('author')
    result = defaultdict(list)
    for book in books:
        author = book.author
        title_and_author = '{} by {}'.format(
            book.title,
            author.name
        )
        result[book.library_id].append(title_and_author)
    return result
    
@profile()
def get_books_by_author_select_related_values():
    from optimize.models import Book
    from collections import defaultdict
    books = (
        Book.objects
         .all()
         .values('title', 'library_id', 'author__name')
    )
    result = defaultdict(list)
    for book in books.iterator():
        title_and_author = '{} by {}'.format(
            book['title'],
            book['author__name']
        )
        result[book['library_id']].append(title_and_author)
    
    return result
    
@profile()
def get_books_by_author_select_related_values_list():
    from optimize.models import Book
    from collections import defaultdict
    books = (
        Book.objects
         .all()
         .select_related('author')
         .values_list('title', 'library_id', 'author__name')
    )
    result = defaultdict(list)
    for book in books.iterator():
        title_and_author = '{} by {}'.format(
            book[0],
            book[2]
        )
        result[book[1]].append(title_and_author)
    
    return result