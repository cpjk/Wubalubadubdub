WEIGHT  = 1

# Returns a positive integer that will be multipled by weight and and the current score
# Return None if you do not want the snake to go in this direction

def run(data, direction):
    print data
    head = [x for x in data["snakes"] if x["id"] == data["our-snake-id"]][0]["coords"][0]
    if direction == "north":
        head[1] -= 1

    if direction == "south":
        head[1] += 1

    if direction == "west":
        head[0] -= 1

    if direction == "east":
        head[0] += 1

    print "\n head "
    print head
    print "\n"
