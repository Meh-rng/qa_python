import pytest
from main import BooksCollector

class TestBooksCollector:

    # Тесты добавления книг
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('invalid_name', [
        '',
        'А' * 41,
        'А' * 100,
    ])
    def test_add_new_book_with_invalid_length_not_added(self, collector, invalid_name):
        collector.add_new_book(invalid_name)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('valid_name', [
        'А',
        'А' * 20,
        'А' * 40,
        'Книга с пробелами и знаками препинания!',
    ])
    def test_add_new_book_with_valid_length_added(self, collector, valid_name):
        collector.add_new_book(valid_name)
        assert len(collector.get_books_genre()) == 1
        assert valid_name in collector.get_books_genre()

    def test_add_new_book_duplicate_not_added(self, collector):
        collector.add_new_book('Книга')
        collector.add_new_book('Книга')
        assert len(collector.get_books_genre()) == 1

    # Тесты установки и получения жанра
    def test_set_book_genre(self, collector):
        book_name = 'Книга'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Ужасы')
        assert collector.get_book_genre(book_name) == 'Ужасы'

    def test_set_book_genre_for_nonexistent_book(self, collector):
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_set_book_genre_with_invalid_genre(self, collector):
        book_name = 'Книга'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Неверный жанр')
        assert collector.get_book_genre(book_name) == ''

    def test_get_book_genre_for_nonexistent_book(self, collector):
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_get_book_genre_for_existing_book(self, collector):
        book_name = 'Книга'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Фантастика')
        assert collector.get_book_genre(book_name) == 'Фантастика'

    def test_get_book_genre_for_book_without_genre(self, collector):
        book_name = 'Книга без жанра'
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ''

    # Тесты получения книг по жанрам
    def test_get_books_with_specific_genre(self, collector_with_genres):
        horror_books = collector_with_genres.get_books_with_specific_genre('Ужасы')
        assert len(horror_books) == 1
        assert 'Книга 2' in horror_books

    def test_get_books_with_specific_genre_no_books(self, collector):
        assert collector.get_books_with_specific_genre('Ужасы') == []

    def test_get_books_with_specific_genre_empty_collection(self, collector):
        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == []

    def test_get_books_with_invalid_genre(self, collector_with_genres):
        assert collector_with_genres.get_books_with_specific_genre('Неверный жанр') == []

    # Тесты метода get_books_genre
    def test_get_books_genre_returns_dict(self, collector):
        result = collector.get_books_genre()
        assert isinstance(result, dict)

    def test_get_books_genre_empty_dict(self, collector):
        assert collector.get_books_genre() == {}

    def test_get_books_genre_with_one_book(self, collector):
        collector.add_new_book('Книга 1')
        books = collector.get_books_genre()
        assert len(books) == 1
        assert 'Книга 1' in books
        assert books['Книга 1'] == ''

    def test_get_books_genre_with_multiple_books(self, collector_with_genres):
        books = collector_with_genres.get_books_genre()
        assert len(books) == 3
        assert books['Книга 1'] == 'Фантастика'
        assert books['Книга 2'] == 'Ужасы'
        assert books['Книга 3'] == 'Детективы'

    # Тесты книг для детей
    def test_get_books_for_children(self, collector_with_genres):
        children_books = collector_with_genres.get_books_for_children()
        assert len(children_books) == 1
        assert 'Книга 1' in children_books  # Фантастика - для детей
        assert 'Книга 2' not in children_books  # Ужасы - не для детей
        assert 'Книга 3' not in children_books  # Детективы - не для детей

    def test_get_books_for_children_without_genre(self, collector):
        collector.add_new_book('Книга без жанра')
        children_books = collector.get_books_for_children()
        assert 'Книга без жанра' not in children_books

    def test_get_books_for_children_empty(self, collector):
        assert collector.get_books_for_children() == []

    # Тесты избранного
    def test_add_book_in_favorites(self, collector_with_books):
        collector_with_books.add_book_in_favorites('Книга 1')
        assert 'Книга 1' in collector_with_books.get_list_of_favorites_books()

    def test_add_nonexistent_book_to_favorites(self, collector):
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_duplicate_book_to_favorites(self, collector_with_books):
        collector_with_books.add_book_in_favorites('Книга 1')
        collector_with_books.add_book_in_favorites('Книга 1')
        assert len(collector_with_books.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self, collector_with_favorites):
        collector_with_favorites.delete_book_from_favorites('Книга 1')
        assert 'Книга 1' not in collector_with_favorites.get_list_of_favorites_books()
        assert 'Книга 2' in collector_with_favorites.get_list_of_favorites_books()

    def test_delete_nonexistent_book_from_favorites(self, collector_with_favorites):
        collector_with_favorites.delete_book_from_favorites('Несуществующая книга')
        assert len(collector_with_favorites.get_list_of_favorites_books()) == 2

    def test_get_list_of_favorites_books_empty(self, collector):
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_list(self, collector):
        favorites = collector.get_list_of_favorites_books()
        assert isinstance(favorites, list)

    def test_get_list_of_favorites_books_with_one_book(self, collector_with_books):
        collector_with_books.add_book_in_favorites('Книга 1')
        favorites = collector_with_books.get_list_of_favorites_books()
        assert len(favorites) == 1
        assert 'Книга 1' in favorites

    def test_get_list_of_favorites_books_with_multiple_books(self, collector_with_favorites):
        favorites = collector_with_favorites.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert 'Книга 1' in favorites
        assert 'Книга 2' in favorites

    # Тесты инициализации
    def test_genre_age_rating_initialized_correctly(self, collector):
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_genre_list_initialized_correctly(self, collector):
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
            