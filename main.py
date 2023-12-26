from src import Tripadvisor

locations = [
  "Chicago",
]

locations = Tripadvisor.Cities.UnitedStates5()[0:10]

Tripadvisor.search(locations, type=Tripadvisor.HOTEL, max=35)

