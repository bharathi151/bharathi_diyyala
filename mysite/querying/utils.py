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
from querying.models import *
@profile()
def get_entry_id_5():
    e = Entry.objects.get(id=5)
    b=e.blog
    return b
@profile()
def get_entry_id_5_with_select_related():
    e = Entry.objects.select_related('blog').get(id=5)
    b=e.blog
    return b
    