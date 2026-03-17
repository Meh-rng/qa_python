from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_with_long_name_not_added(self):
        collector = BooksCollector()
        long_name = 'А' * 41
        collector.add_new_book(long_name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_with_empty_name_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_new_book('Книга')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre(self):
        collector = BooksCollector()
        book_name = 'Книга'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Ужасы')
        assert collector.get_book_genre(book_name) == 'Ужасы'

    def test_set_book_genre_for_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_set_book_genre_with_invalid_genre(self):
        collector = BooksCollector()
        book_name = 'Книга'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Неверный жанр')
        assert collector.get_book_genre(book_name) == ''

    def test_get_book_genre_for_nonexistent_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 1', 'Ужасы')
        collector.set_book_genre('Книга 2', 'Ужасы')
        collector.set_book_genre('Книга 3', 'Комедии')
        
        horror_books = collector.get_books_with_specific_genre('Ужасы')
        assert len(horror_books) == 2
        assert 'Книга 1' in horror_books
        assert 'Книга 2' in horror_books
        assert 'Книга 3' not in horror_books

    def test_get_books_with_specific_genre_no_books(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre('Ужасы') == []

    def test_get_books_with_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Ужасы')
        assert collector.get_books_with_specific_genre('Неверный жанр') == []

    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        books = collector.get_books_genre()
        assert isinstance(books, dict)
        assert len(books) == 2

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Детская книга')
        collector.add_new_book('Ужастик')
        collector.add_new_book('Детектив')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        collector.set_book_genre('Ужастик', 'Ужасы')
        collector.set_book_genre('Детектив', 'Детективы')
        
        children_books = collector.get_books_for_children()
        assert len(children_books) == 1
        assert 'Детская книга' in children_books
        assert 'Ужастик' not in children_books
        assert 'Детектив' not in children_books

    def test_get_books_for_children_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга без жанра')
        children_books = collector.get_books_for_children()
        assert 'Книга без жанра' not in children_books

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert 'Книга' in collector.get_list_of_favorites_books()

    def test_add_nonexistent_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_duplicate_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.add_book_in_favorites('Книга')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.get_list_of_favorites_books()

    def test_delete_nonexistent_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_list(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')
        favorites = collector.get_list_of_favorites_books()
        assert isinstance(favorites, list)
        assert len(favorites) == 2
def test_add_new_book_with_max_length_name(self):
    collector = BooksCollector()
    name = 'А' * 40
    collector.add_new_book(name)
    assert len(collector.get_books_genre()) == 1

def test_book_names_are_case_sensitive(self):
    collector = BooksCollector()
    collector.add_new_book('Книга')
    collector.add_new_book('книга')
    assert len(collector.get_books_genre()) == 2

def test_set_genre_for_book_without_genre(self):
    collector = BooksCollector()
    collector.add_new_book('Книга')
    collector.set_book_genre('Книга', 'Фантастика')
    assert collector.get_book_genre('Книга') == 'Фантастика'

def test_get_books_for_children_empty(self):
    collector = BooksCollector()
    assert collector.get_books_for_children() == []

def test_genre_age_rating_initialized_correctly(self):
    collector = BooksCollector()
    assert collector.genre_age_rating == ['Ужасы', 'Детективы']

def test_get_books_with_specific_genre_empty_books(self):
    collector = BooksCollector()
    result = collector.get_books_with_specific_genre('Фантастика')
    assert result == []

def test_delete_book_from_favorites_not_in_favorites(self):
    collector = BooksCollector()
    collector.add_new_book('Книга')
    collector.delete_book_from_favorites('Книга')  # книга не в избранном
    assert len(collector.get_list_of_favorites_books()) == 0
            