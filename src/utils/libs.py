import datetime
import math
import re

from django.utils.html import strip_tags



def count_words(html_string):
    # html_string = """
    # <h1>This is a title</h1>
    # """
    word_string = strip_tags(html_string)
    matching_words = re.findall(r'\w+', word_string)
    count = len(matching_words) #joincfe.com/projects/
    return count

def get_read_time(html_string):
    count = count_words(html_string)
    read_time_min = math.ceil(count/200.0) #assuming 200wpm reading
    # read_time_sec = read_time_min * 60
    # read_time = str(datetime.timedelta(seconds=read_time_sec))
    # read_time = str(datetime.timedelta(minutes=read_time_min))
    return int(read_time_min)

def upload_location(instance, filename, *args, **kwargs):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because 
    the model is defined below.
    Then create a queryset ordered by the "id"s of each object, 
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(new_id, filename)