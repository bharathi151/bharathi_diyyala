from django.db import models

class ReactionTypes(models.TextChoices):
    WOW = "WOW"
    LIT = "LIT"
    LOVE = "LOVE"
    HAHA = "HAHA"
    THUMBS_UP = "THUMBS-UP"
    THUMBS_DOWN = "THUMBS-DOWN"
    ANGRY = "ANGRY"
    SAD = "SAD"

class PositiveReactions(models.TextChoices):
    WOW = "WOW"
    LIT = "LIT"
    LOVE = "LOVE"
    HAHA = "HAHA"
    THUMBS_UP = "THUMBS-UP"

class NegativeReactions(models.TextChoices):
    THUMBS_DOWN = "THUMBS-DOWN"
    ANGRY = "ANGRY"
    SAD = "SAD"

def convert_date_time_into_strf_format(date_time):
    converted_date_time = date_time.strftime("%Y-%m-%d %H:%M:%S.%f")
    return converted_date_time
