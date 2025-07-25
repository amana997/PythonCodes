import random
from collections import Counter

def assign_roles(players):
    roles = ['Mafia', 'Doctor', 'Detective']
    villagers = len(players) - len(roles)
    roles += ['Villager'] * villagers
    random.shuffle(roles)
    return dict(zip(players, roles))

def night_phase(players, roles, alive, mafia):
    print("\nNight falls...")
    victim = random.choice([p for p in alive if p not in mafia])
    saved = random.choice(alive)
    investigated = random.choice(alive)

    print("Mafia has chosen their target.")
    print("Doctor has chosen someone to save.")
    print("Detective has investigated someone.")

    if victim == saved:
        print("Doctor saved the victim! No one died.")
    else:
        print(f"{victim} was killed by the Mafia!")
        alive.remove(victim)

    if roles[investigated] == 'Mafia':
        print(f"Detective discovered that {investigated} is Mafia.")
    else:
        print(f"Detective discovered that {investigated} is not Mafia.")

def day_phase(alive):
    print("\nDay has come. Players discuss and vote.")
    votes = []
    for voter in alive:
        choice = random.choice([p for p in alive if p != voter])
        print(f"{voter} voted to eliminate {choice}")
        votes.append(choice)

    voted_out = Counter(votes).most_common(1)[0][0]
    print(f"{voted_out} has been voted out by the village.")
    alive.remove(voted_out)
    return voted_out

def check_win(roles, alive):
    mafia_alive = [p for p in alive if roles[p] == 'Mafia']
    others_alive = [p for p in alive if roles[p] != 'Mafia']

    if not mafia_alive:
        print("\n🎉 Villagers win! All Mafia are dead.")
        return True
    elif len(mafia_alive) >= len(others_alive):
        print("\n💀 Mafia wins! They outnumber the rest.")
        return True
    return False

def play_game():
    print("🎲 Welcome to Mafia Party Game!")
    num_players = int(input("Enter number of players (min 5): "))
    while num_players < 5:
        num_players = int(input("Need at least 5 players. Try again: "))

    players = []
    for i in range(num_players):
        name = input(f"Enter name of player {i + 1}: ")
        players.append(name)

    roles = assign_roles(players)
    print("\nRoles have been assigned. (Secret!)")

    alive = players[:]
    mafia = [p for p in players if roles[p] == 'Mafia']

    round_num = 1
    while True:
        print(f"\n======= Round {round_num} =======")
        night_phase(players, roles, alive, mafia)
        if check_win(roles, alive):
            break

        voted_out = day_phase(alive)
        if roles[voted_out] == 'Mafia':
            mafia.remove(voted_out)

        if check_win(roles, alive):
            break

        round_num += 1

    print("\n🧾 Final roles:")
    for player, role in roles.items():
        print(f"{player}: {role}")

if __name__ == "__main__":
    play_game()