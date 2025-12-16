import socket
import threading
import random
from collections import Counter

HOST = '0.0.0.0'
PORT = 9999
MIN_PLAYERS = 5

clients = []
names = []
roles = {}
alive = []

def broadcast(msg):
    for client in clients:
        client.sendall(msg.encode())

def send(client, msg):
    client.sendall(msg.encode())

def recv(client):
    return client.recv(1024).decode().strip()

def handle_client(client, addr):
    name = recv(client)
    names.append(name)
    alive.append(name)
    print(f"[+] {name} joined from {addr}")
    if len(clients) >= MIN_PLAYERS:
        start_game()

def assign_roles():
    base_roles = ['Mafia', 'Doctor', 'Detective']
    remaining = len(names) - len(base_roles)
    all_roles = base_roles + ['Villager'] * remaining
    random.shuffle(all_roles)
    return dict(zip(names, all_roles))

def get_player_index(name):
    return names.index(name)

def start_game():
    global roles
    roles = assign_roles()

    # Notify roles
    for i, client in enumerate(clients):
        send(client, f"ROLE:{roles[names[i]]}")

    round_num = 1
    while True:
        print(f"\n[Round {round_num}]")

        # NIGHT PHASE
        mafia_target = doctor_save = detective_target = None

        # Get inputs
        for i, name in enumerate(names):
            if name not in alive:
                continue

            role = roles[name]
            if role == 'Mafia':
                send(clients[i], "\nNight: Who to KILL?")
                mafia_target = recv(clients[i])
            elif role == 'Doctor':
                send(clients[i], "\nNight: Who to SAVE?")
                doctor_save = recv(clients[i])
            elif role == 'Detective':
                send(clients[i], "\nNight: Who to INVESTIGATE?")
                detective_target = recv(clients[i])
                if roles[detective_target] == 'Mafia':
                    send(clients[i], f"{detective_target} IS Mafia.")
                else:
                    send(clients[i], f"{detective_target} is NOT Mafia.")

        # Resolve
        if mafia_target != doctor_save:
            alive.remove(mafia_target)
            broadcast(f"\n💀 {mafia_target} was killed at night.")
        else:
            broadcast(f"\n💉 {mafia_target} was saved by the Doctor!")

        # CHECK WIN
        if check_win():
            return

        # DAY PHASE
        votes = {}
        for i, name in enumerate(names):
            if name in alive:
                send(clients[i], f"\nDay: Vote to eliminate:")
                vote = recv(clients[i])
                votes[vote] = votes.get(vote, 0) + 1

        if votes:
            eliminated = Counter(votes).most_common(1)[0][0]
            if eliminated in alive:
                alive.remove(eliminated)
                broadcast(f"\n🗳️ {eliminated} was voted out.")

        if check_win():
            return

        round_num += 1

def check_win():
    mafia = [p for p in alive if roles[p] == 'Mafia']
    villagers = [p for p in alive if roles[p] != 'Mafia']

    if not mafia:
        broadcast("\n🎉 Villagers win!")
        return True
    if len(mafia) >= len(villagers):
        broadcast("\n💀 Mafia wins!")
        return True
    return False

def main():
    print(f"[Server] Starting on {HOST}:{PORT}...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[Server] Waiting for {MIN_PLAYERS} players...")

    while True:
        client, addr = server.accept()
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()

if __name__ == "__main__":
    main()
