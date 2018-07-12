from enum import Enum


class Genre(Enum):
    ACTION = 28
    ADVENTURE = 12
    ANIMATION = 16
    COMEDY = 35
    CRIME = 80
    DOCUMENTARY = 99
    DRAMA = 18
    FAMILY = 10751
    FANTASY = 14
    HISTORY = 36
    HORROR = 27
    MUSIC = 10402
    MYSTERY = 9648
    ROMANCE = 10749
    SCIENCE_FICTION = 878
    TV_MOVIE = 10770
    THRILLER = 53
    WAR = 10752
    WESTERN = 37


def genre_name(genre):
    names = {
        28: 'Action',
        12: 'Adventure',
        16: 'Animation',
        35: 'Comedy',
        80: 'Crime',
        99: 'Documentary',
        18: 'Drama',
        10751: 'Family',
        14: 'Fantasy',
        36: 'History',
        27: 'Horror',
        10402: 'Music',
        9648: 'Mystery',
        10749: 'Romance',
        878: 'Science Fiction',
        10770: 'TV Movie',
        53: 'Thriller',
        10752: 'War',
        37: 'Western'
    }
    return names.get(genre)
