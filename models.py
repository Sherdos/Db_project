class Book():
    def __init__(self, id, title, date, author_id) -> None:
        self.id = id
        self.title = title
        self.date = date
        self.author_id = author_id
        
    def __str__(self) -> str:
        return f'Id - {self.id},Название - {self.title}, Дата публикации - {self.date}, Id автора - {self.author_id}'