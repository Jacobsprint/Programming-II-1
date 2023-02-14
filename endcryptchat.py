import threading
import socket
import rsa  # pip install rsa

public_key, private_key = rsa.newkeys(1024) # 1024 bits
DEFAULT_IP_PORT = ("127.0.0.1", 9999)
choice = input("Do you want to be the server or client? (s/c): ")

if choice == "s":
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(DEFAULT_IP_PORT) # Open TCP Connection
  server .listen()
  print("Waiting for connection...")
  client, addr = server.accept()
  print("Connected to", addr)
  client.send(public_key.save_pkcs1())
  public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
  print("Use 'Crtl+C' to disconnect.")
elif choice == "C":
  print("Connecting to server...", end="")
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect(DEFAULT_IP_PORT)
  print("Sucess! Connect to " + str(client.getpeername()))
  public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
  client.send(public_key.save_pkcs1())
  print("Use 'Crtl+C' to disconnect.")
else: 
  exit()

def sendMsg(c):
  while True:
    try:
      msg = input()
      print('\033[1A' + '\033[k', end='') 
      c.send(rsa.encrypt(msg.encoder(), public_partner))
      print("\033[91mYou: \033[0m" + msg)
    except: 
      exit()

def recvMsg(c):
  while True:
    try:
      msg = rsa.decrypt(c.recv(1024), private_key)
      print("\033[94mPartner: \033[0m" + msg.decode())
    except:
      print("Partner has disconnected. Press enter to exit.")
      exit()

try:
  send_thread = threading.Thread(target=sendMsg, args=(client,)).start()
  recv_thread = threading.Thread(target=recvMsg, args=(client,)).start()
except:
  pass