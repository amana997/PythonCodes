import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext

PORT = 9999
BROADCAST_PORT = 50000

def discover_server_ip():
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp_sock.settimeout(5)
    udp_sock.bind(('', BROADCAST_PORT))
    try:
        while True:
            msg, addr = udp_sock.recvfrom(1024)
            if msg == b'MAFIA_SERVER':
                return addr[0]
    except socket.timeout:
        return None

class MafiaClientGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Mafia Game Client")

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_ip = discover_server_ip()
        if not self.server_ip:
            messagebox.showerror("Error", "Server not found.")
            exit()
        self.sock.connect((self.server_ip, PORT))

        # Player name
        self.name = simpledialog.askstring("Name", "Enter your name:", parent=master)
        if self.name:
            self.sock.sendall(self.name.encode())

        # Chat area
        self.chat_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, state='disabled', width=50, height=15)
        self.chat_area.pack(padx=10, pady=(10, 5))

        # Player list
        self.player_list_label = tk.Label(master, text="Players Alive:")
        self.player_list_label.pack()
        self.player_list = tk.Listbox(master, height=6)
        self.player_list.pack(pady=(0, 5))

        # Action button
        self.action_button = tk.Button(master, text="Choose", command=self.send_selection)
        self.action_button.pack(pady=(0, 10))
        self.action_button.config(state='disabled')

        # Fallback entry
        self.entry_field = tk.Entry(master, width=40)
        self.entry_field.pack(pady=(0, 10))
        self.entry_field.bind("<Return>", self.send_fallback)

        self.current_action = None

        # Start receiving
        self.receive_thread = threading.Thread(target=self.receive)
        self.receive_thread.daemon = True
        self.receive_thread.start()

    def receive(self):
        while True:
            try:
                msg = self.sock.recv(1024).decode()
                if msg.startswith("ROLE:"):
                    role = msg.split(":")[1]
                    messagebox.showinfo("Your Role", f"Your role is: {role}")
                elif msg.startswith("PLAYERS:"):
                    players = msg.split(":")[1].split(",")
                    self.update_player_list(players)
                elif msg.startswith("VOTE_REQUEST:") or msg.startswith("NIGHT_ACTION:"):
                    self.chat(msg)
                    self.current_action = msg.split(":")[1]
                    self.action_button.config(state='normal')
                else:
                    self.chat(msg)
            except:
                self.chat("Disconnected from server.")
                self.sock.close()
                break

    def update_player_list(self, players):
        self.player_list.delete(0, tk.END)
        for p in players:
            self.player_list.insert(tk.END, p)

    def send_selection(self):
        try:
            selected = self.player_list.get(self.player_list.curselection())
            self.sock.sendall(selected.encode())
            self.action_button.config(state='disabled')
            self.chat(f"You selected: {selected} ({self.current_action})")
        except:
            messagebox.showwarning("No Selection", "Please select a player.")

    def send_fallback(self, event=None):
        msg = self.entry_field.get()
        if msg:
            self.sock.sendall(msg.encode())
            self.entry_field.delete(0, tk.END)

    def chat(self, msg):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, msg + '\n')
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MafiaClientGUI(root)
    root.mainloop()
