class Bookshelf:
    def __init__(self,name,author,price,publishing_year):
        self.name=name
        self.author=author
        self.price=price
        self.publishing_year=publishing_year
        
    def addBook(self):
        print("Name:" + self.name)
        print("Author:" + self.author)
        print("Price:" + str(self.price))
        print("Publishing Year:" + str(self.publishing_year))
        
    def publish(self):
        time = 2022 - self.publishing_year
        Published_Time = "This book was published " + str(time) + " years ago."
        print(Published_Time)
        
book1 = Bookshelf("Diary of a Wimpy Kid", "Jeff Kinney", 10, 2007)
book1.addBook()
book1.publish()

book2 = Bookshelf("Harry Potter and the Sorcerer", "J.K Rowling", 10, 1997)
book2.addBook()
book2.publish()