# Saturn is missing from the planet_list
# Insert it into the correct position

planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
# Expected output: "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"
planet_list[4:]="Jupiter","Saturn", "Uranus", "Neptune"
print(planet_list)
