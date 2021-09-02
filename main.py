import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "name": "Zork",
  "passages": [
    {
      "name": "West of House",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North of House",
        }
      ],
      "cleanText": "This is an open field west of a white house, with a boarded front door."
    },
    {
      "name": "North of House",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "West of House",
        }
      ],
      "cleanText": "You are facing the north side of a white house. There is no door here, and all the windows are barred."
    }
  ]
}

current = "West of House"
response = ""
while True:
    if response == "quit":
        break

    
    current_location = {}

    # Find passage (update)
    for passages in world["passages"]:
      if passages["name"] == current:
        current_location = passages

    # Display passage (render the world)

    print(current_location["name"])
    print(current_location["cleanText"])

    for Link in current_location["links"]:
      print(Link["linkText"])


    # Ask for response (get input)
    response = input("Where do you want to go? ")

    for link in current_location["links"]:
      if response == link["linkText"]:
        current = link["passageName"]
