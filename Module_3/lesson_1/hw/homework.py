class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author

    def __str__(self):
        return f"{self.author}: '{self.text}'"


class Book:
    def __init__(self, author: str, name: str, year: int, genre: str):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
        self.comments: list[Comment] = []

    def __str__(self):
        book_display = f"{self.name} by {self.author} ({self.year})"
        for comment in self.comments:
            book_display += f"\n\t{comment}"
        return book_display

    def __repr__(self):
        return f"Name: {self.name}, Author: {self.author}, Year: {self.year}, Genre: {self.genre}"

    def add_comments(self, *args):
        self.comments.extend(args)

    def add_comment(self, comment: Comment):
        self.comments.append(comment)


book_1 = Book("Vlad", "Python book", 2024, "Science")
book_2 = Book("Vlad2", "Python book 2", 2025, "Science")
book_3 = Book("Vlad3", "Python book 3", 2026, "Science")

print(book_1)
# print(book_2)
# print(book_3)

comment_1 = Comment("Comment 1", "Not Vlad")
comment_2 = Comment("Comment 2", "Bot Vlad")
comment_3 = Comment("Comment 3", "Bot Vlad 2")

book_1.add_comment(comment_1, comment_2, comment_3)
# book_1.add_comment(comment_2)
# book_1.add_comment(comment_3)
print(book_1)
