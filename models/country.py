# Model for the country class
class Country:
    def __init__(self, id, name, area, population, continent_id, language_id):
        self.id = id
        self.name = name
        self.area = area
        self.population = population
        self.continent_id = continent_id
        self.language_id = language_id
