import random
from collections import Counter

def assign_roles(players):
    roles = ['Mafia', 'Doctor', 'Detective']
    villagers = len(players) - len(roles)
    roles += ['Villager'] * villagers
    random.shuffle(roles)
    return dict(zip(players, roles))

def get_valid_input(prompt, alive, exclude=[]):
    while True:
        choice = input(prompt).strip()
        if choice in alive and choice not in exclude:
            return choice
        print("Invalid choice. Try again.")

def night_phase(roles, alive):
    print("\n🌙 Night falls... Everyone closes their eyes.")

    # Mafia chooses target
    mafia_players = [p for p in alive if roles[p] == 'Mafia']
    print(f"\n[Mafia] ({', '.join(mafia_players)}), choose a player to eliminate.")
    victim = get_valid_input("Who do you want to eliminate? ", alive, mafia_players)

    # Doctor chooses who to save
    doctor_players = [p for p in alive if roles[p] == 'Doctor']
    if doctor_players:
        print(f"\n[Doctor] ({doctor_players[0]}), choose someone to save.")
        saved = get_valid_input("Who do you want to save? ", alive)
    else:
        saved = None

    # Detective investigates
    detective_players = [p for p in alive if roles[p] == 'Detective']
    if detective_players:
        print(f"\n[Detective] ({detective_players[0]}), choose someone to investigate.")
        investigated = get_valid_input("Who do you want to investigate? ", alive)
        if roles[investigated] == 'Mafia':
            print(f"🔍 {investigated} is Mafia.")
        else:
            print(f"🔍 {investigated} is NOT Mafia.")

    # Resolve kill
    if victim == saved:
        print(f"\n💉 Doctor saved {victim}! No one died tonight.")
    else:
        print(f"\n💀 {victim} was killed by the Mafia.")
        alive.remove(victim)

def day_phase(alive):
    print("\n☀️ Day has come. Time to discuss and vote.")
    votes = []
    for voter in alive:
        vote = get_valid_input(f"{voter}, who do you vote to eliminate? ", alive, [voter])
        votes.append(vote)

    voted_out = Counter(votes).most_common(1)[0][0]
    print(f"\n🗳️ {voted_out} was voted out by the village.")
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
        name = input(f"Enter name of player {i + 1}: ").strip()
        players.append(name)

    roles = assign_roles(players)
    print("\n🔐 Roles have been secretly assigned.")
    print("NOTE: Only the host should see roles below:")
    for player, role in roles.items():
        print(f"{player}: {role}")

    alive = players[:]
    mafia = [p for p in players if roles[p] == 'Mafia']

    round_num = 1
    while True:
        print(f"\n======= Round {round_num} =======")
        night_phase(roles, alive)
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
