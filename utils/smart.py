import random


def choose_weighted_playlist(playlists):
    total_weight = 0
    for item in playlists:
        total_weight += item["weight"]

    random_point = random.choice(range(1, total_weight + 1))

    for item in playlists:
        random_point -= item["weight"]
        if random_point <= 0:
            return item

    return playlists  [-1]
