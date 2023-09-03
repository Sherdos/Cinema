from django.test import TestCase

from film.models import Category, Genre, Movie

# Create your tests here.

movie = {
    'title': 'Riders of Berk',
    'description': 'Story about boy than train a Drakon.',
    'year': '2010',
    'poster': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0kylEqLF9BAOq_sT_250hBUBbA0X-OEMuBcy4mPfK1Rn6sDSq',
    'video': 'https://1ww.frkp.live/film/280172/',
    'url': 'Riders of Berk',
    'category_id': 1
}

category = {
    'name': 'multfilm',
    'url': 'multfilm',
}
genre = {
    'name': 'multfilm',
    'url': 'multfilm',
}


class MovieTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Movie.objects.create(**movie)
        Genre.objects.create(**genre)
        Category.objects.create(**category)

    def test_title_label(self):
        movie = Movie.objects.get(id=1)
        genre = Genre.objects.filter(id=1)
        movie.genres.set(genre)
        field_label = movie._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Название')
