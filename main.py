from src import Tripadvisor

def main():
    locations = [
        "Chicago",
        # Add more cities as needed
    ]

    # Call the search method from the Tripadvisor class for things to do
    results = Tripadvisor.search(locations, type="attraction", max=100)

    # Process the results as needed
    print(results)  # Example: Print the results

if __name__ == "__main__":
    main()

