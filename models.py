class Book():
    def __init__(self, id, title, date, author_id, author = None) -> None:
        self.id = id
        self.title = title
        self.date = date
        self.author_id = author_id
        self.author = author
    
        
    def __str__(self) -> str:
        if self.author == None:
            return self.get_by_id()
        else:
            return self.get_by_author_id()
        
    def get_by_id(self):
        return f'Id - {self.id},Название - {self.title}, Дата публикации - {self.date}, Id автора - {self.author_id}'
    
    def get_by_author_id(self):
        return f'Id - {self.id},Название - {self.title}, Дата публикации - {self.date}, автора - {self.author[1]}'
    
    
    