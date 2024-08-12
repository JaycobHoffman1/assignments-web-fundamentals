import requests as r
import json as j

# Task 1: Setting Up a Python Virtual Environment and Installing Packages -- Complete!

# Task 2: Fetching Data from the Pokémon API

print("Task 2: Fetching Data from the Pokémon API\n")

response = r.get("https://pokeapi.co/api/v2/pokemon/pikachu")
json_data = response.text
pikachu_data = j.loads(json_data)

print(f"Name: {pikachu_data["name"].capitalize()}\nAbilities:", end = " ")

for ability in pikachu_data["abilities"][:-1]:
    print(f"{ability['ability']['name'].capitalize()},", end = " ")

print(f"{pikachu_data["abilities"][-1]["ability"]["name"].capitalize()}\n")

# Task 3: Analyzing and Displaying Data

print("Task 3: Analyzing and Displaying Data\n")

def fetch_pokemon_data(pokemon_name):
    try:
        response = r.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.strip().lower()}")
        json_data = response.text
        pokemon_data = j.loads(json_data)

        print(f"Name: {pokemon_data["name"].capitalize()}\nAbilities:", end = " ")

        for ability in pokemon_data["abilities"][:-1]:
            print(f"{ability['ability']['name'].capitalize()},", end = " ")

        print(f"{pokemon_data["abilities"][-1]["ability"]["name"].capitalize()}\n")
    except Exception:
        print("Pokemon not found.\n")

def calculate_average_weight(pokemon_list):
    try:
        weights = [j.loads(r.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.strip().lower()}").text)["weight"]\
        for pokemon_name in pokemon_list]
    except Exception:
        print("One or more Pokémon not found.\n")
    else:
        average_weight = float(f"{sum(weights) / len(weights):.1f}")

        print(average_weight)

pokemon_list = ["Corviknight", "Dugtrio", "Pelipper"]

print("Fetch Pokémon data for Arcanine:")
fetch_pokemon_data("Arcanine")

print("Average weight for Corviknight, Dugtrio, and Pelipper:", end = " ")
calculate_average_weight(pokemon_list)