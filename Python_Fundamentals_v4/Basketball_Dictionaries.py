# Challenge 1: Update the Constructor
players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]


class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team


team_players = Player(players[0]["name"], players[0]["age"], players[0]["position"], players[0]["team"])
print(f'{team_players.name} position is {team_players.position}')


# Challenge 2: Create instances using individual player dictionaries.
kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}

player1 = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
player2 = Player(jason["name"], jason["age"], jason["position"], jason["team"])
player3 = Player(kyrie["name"], kyrie["age"], kyrie["position"], kyrie["team"])
print(f'{player3.name} position is {player3.position}')
# Create your Player instances here!
# player_jason = ???


# Challenge 3: Make a list of Player instances from a list of dictionaries
# ... (class definition and large list of players here)
new_team = []
# Write your for loop here to populate the new_team variable with Player objects.
for index in players:
    for key in index:
        new_team.append(index[key])
print(new_team)