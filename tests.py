from main import BooksCollector


class TestBooksCollector: 
    
    def test_add_new_book_add_two_books(self):        
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')                
        assert len(collector.get_books_rating()) == 2


    def test_add_new_book_validation_40_char_limit(self):
        collector = BooksCollector()
        books_with_long_name = 'Бабушка велела кланяться и передать, что просит прощения'
        collector.add_new_book(books_with_long_name)
        assert books_with_long_name not in collector.books_genre

    def test_set_book_genre_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Пикник на обочине')
        collector.set_book_genre('Пикник на обочине', 'Фантастика')
        assert collector.books_genre['Пикник на обочине'] == 'Фантастика'

    def test_get_book_genre_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Токийский Зодиак')
        collector.set_book_genre('Токийский Зодиак', 'Детективы')
        assert collector.get_books_genre['Токийский Зодиак'] == 'Детективы'

    def test_get_books_with_specific_genre_successfully(self):
        collector = BooksCollector()
        books = ['Черная орхидея', 'Секреты Лос-Анджелеса', 'Девушка с татуировкой дракона']
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Черная орхидея', 'Секреты Лос-Анджелеса', 
                                                                       'Девушка с татуировкой дракона']
        
    def test_get_books_genre_empty(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}
    
    def test_get_books_genre_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Улитка на склоне')
        collector.set_book_genre('Улитка на склоне', 'Фантастика')
        assert collector.get_books_genre() == {'Улитка на склоне': 'Фантастика'}

    def test_get_books_for_children_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Телепузики')
        collector.add_new_book('Адвокат дьявола')
        collector.set_book_genre('Телепузики', 'Мультфильмы')
        collector.set_book_genre('Адвокат дьявола', 'Ужасы')
        assert collector.get_books_for_children() == ['Телепузики']

    def test_add_book_to_favorites_successfully(self):
        collector = BooksCollector()
        favorites_book = 'Аист Марабу'
        collector.add_new_book(favorites_book)
        collector.add_book_in_favorites(favorites_book)
        assert favorites_book in collector.favorites

    def test_delete_book_from_favorites_successfully(self):
        collector = BooksCollector()
        favorites_book = 'Аист Марабу'
        collector.add_new_book(favorites_book)
        collector.add_book_in_favorites(favorites_book)
        collector.delete_book_from_favorites(favorites_book)
        assert favorites_book not in collector.favorites


    def test_get_list_of_favorites(self):
        collector = BooksCollector()
        books = ['Улитка на склоне', 'Аист Марабу', 'Пикник на обочине']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == books
                    