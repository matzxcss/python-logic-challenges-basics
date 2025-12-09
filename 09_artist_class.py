class Artist:
    def __init__(self, name, genre, debut_year):
        self.name = name
        self.genre = genre
        self.debut_year = debut_year

    def get_info(self):
        return f"{self.name} is a {self.genre} artist who debuted in {self.debut_year}."
    def years_active(self, current_year):
        return current_year - self.debut_year
    def change_genre(self, new_genre):
        self.genre = new_genre
# Example usage:
# artist = Artist("Adele", "Pop", 2008)
# print(artist.get_info())
# print(f"Years active: {artist.years_active(2024)}")
