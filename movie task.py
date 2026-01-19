class Movie:
    def __init__(self, title, available_seats):
        self.title = title
        self.available_seats = available_seats

    def book_ticket(self, seats):
        if seats <= self.available_seats:
            self.available_seats -= seats
            print(f"{seats} ticket(s) booked for '{self.title}'")
            print(f"Remaining seats: {self.available_seats}")
        else:
            print("Not enough seats")



movie1 = Movie("Avengers: Endgame", 10)

movie1.book_ticket(3)
movie1.book_ticket(4)
movie1.book_ticket(5)
