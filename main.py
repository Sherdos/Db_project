import psycopg2
import utils 

class App():
    
    def run(self):
        while True:
            print('the app run')
            print('1 - Get all books, 2 - exit, 3 - get book by id, 4 - get book by author_id ')
            com = input('Enter command - ')
            if com == '1':
                utils.all_books()
            elif com == '2':
                print('You are exitting')
                break
            elif com == '3':
                id = input('Enter id - ')
                utils.get_book_by_id(id)
            elif com == '4':
                author_id = input('Enter author_id - ')
                utils.get_book_by_author_id(author_id)
                
if __name__ == '__main__':
    app = App()
    app.run()


