import requests as r
import json as j

# Task 1: Set up a Python Virtual Environment and Install Required Packages - Complete!

# Task 2: Fetch Data from a Space API

print("Task 2: Fetch Data from a Space API:")

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = r.get(url)
    planets = response.json()["bodies"]

    for planet in planets:
        if planet["isPlanet"]:
            name = planet["englishName"]
            mass = planet["mass"]["massValue"]
            orbit_period = planet["sideralOrbit"]

            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

    print("\n")

fetch_planet_data()

# Task 3: Data Presentation and Analysis

print("Task 3: Data Presentation and Analysis")

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = r.get(url)
    planets = response.json()["bodies"]
    planet_list = []

    for planet in planets:
        if planet["isPlanet"]:
            name = planet["englishName"]
            mass = planet["mass"]["massValue"]
            orbit_period = planet["sideralOrbit"]

            planet_list.append({"Name": name, "Mass": mass, "Orbit Period": orbit_period})

    return planet_list

def find_heaviest_planet(planet_list):
    mass = max([planet["Mass"] for planet in planet_list])
    
    for planet in planet_list:
        if planet["Mass"] == mass:
            return (planet["Name"], mass)

planet_list = fetch_planet_data()
name, mass = find_heaviest_planet(planet_list)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")