from src import Tripadvisor

locations = [
  "Chicago",
]

Tripadvisor.search(locations, type=Tripadvisor.HOTEL, max=100)
