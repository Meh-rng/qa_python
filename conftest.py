import pytest
from books_collector import BooksCollector

@pytest.fixture
def collector():
    """Фикстура, возвращающая новый экземпляр BooksCollector для каждого теста"""
    return BooksCollector()

@pytest.fixture
def collector_with_books(collector):
    """Фикстура с предустановленными книгами"""
    books = ['Книга 1', 'Книга 2', 'Книга 3']
    for book in books:
        collector.add_new_book(book)
    return collector

@pytest.fixture
def collector_with_genres(collector_with_books):
    """Фикстура с книгами и жанрами"""
    collector = collector_with_books
    collector.set_book_genre('Книга 1', 'Фантастика')
    collector.set_book_genre('Книга 2', 'Ужасы')
    collector.set_book_genre('Книга 3', 'Детективы')
    return collector

@pytest.fixture
def collector_with_favorites(collector_with_genres):
    """Фикстура с книгами, жанрами и избранным"""
    collector = collector_with_genres
    collector.add_book_in_favorites('Книга 1')
    collector.add_book_in_favorites('Книга 2')
    return collector