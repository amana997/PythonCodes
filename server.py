import socket
import threading
import time
import random
from collections import Counter

HOST = '0.0.0.0'
PORT = 9999
BROADCAST_PORT = 50000
MIN_PLAYERS = 5

clients = []
names = []
roles = {}
alive = []

def broadcast_server_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    while True:
        try:
            msg = b'MAFIA_SERVER'
            sock.sendto(msg, ('<broadcast>', BROADCAST_PORT))
            time.sleep(1)
        except:
            break

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
    villagers = len(names) - len(base_roles)
    all_roles = base_roles + ['Villager'] * villagers
    random.shuffle(all_roles)
    return dict(zip(names, all_roles))

def start_game():
    global roles
    roles = assign_roles()

    for i, client in enumerate(clients):
        send(client, f"ROLE:{roles[names[i]]}")

    round_num = 1
    while True:
        print(f"\n[Round {round_num}]")

        broadcast("PLAYERS:" + ",".join(alive))

        # NIGHT PHASE
        mafia_target = doctor_save = detective_target = None

        for i, name in enumerate(names):
            if name not in alive:
                continue
            role = roles[name]
            if role == 'Mafia':
                send(clients[i], "NIGHT_ACTION:kill")
                mafia_target = recv(clients[i])
            elif role == 'Doctor':
                send(clients[i], "NIGHT_ACTION:save")
                doctor_save = recv(clients[i])
            elif role == 'Detective':
                send(clients[i], "NIGHT_ACTION:investigate")
                detective_target = recv(clients[i])
                if roles.get(detective_target) == 'Mafia':
                    send(clients[i], f"{detective_target} IS Mafia.")
                else:
                    send(clients[i], f"{detective_target} is NOT Mafia.")

        if mafia_target != doctor_save and mafia_target in alive:
            alive.remove(mafia_target)
            broadcast(f"\n💀 {mafia_target} was killed during the night.")
        else:
            broadcast(f"\n💉 No one died. Doctor saved {doctor_save}!")

        if check_win():
            return

        # DAY PHASE
        broadcast("PLAYERS:" + ",".join(alive))
        votes = {}
        for i, name in enumerate(names):
            if name in alive:
                send(clients[i], "VOTE_REQUEST:Who do you vote to eliminate?")
                vote = recv(clients[i])
                if vote in alive:
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
    mafia = [p for p in alive if roles.get(p) == 'Mafia']
    villagers = [p for p in alive if roles.get(p) != 'Mafia']
    if not mafia:
        broadcast("\n🎉 Villagers win!")
        return True
    elif len(mafia) >= len(villagers):
        broadcast("\n💀 Mafia wins!")
        return True
    return False

def main():
    print("[Server] Starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[Server] Listening on port {PORT}...")

    while True:
        client, addr = server.accept()
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()

if __name__ == "__main__":
    threading.Thread(target=broadcast_server_ip, daemon=True).start()
    main()
