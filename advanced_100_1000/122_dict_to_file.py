def save_clients_data():
  """function that writes clients' names to the file as a dict"""
  filename = 'neoplan_clients.txt'
  clients = {}
  print("\n---Enter clients data---\n")
  count = 1
  print("Type 'exit' to finish")
  while True:
    name = input(f"{count}-Enter a client's name: ").strip()
    if name.lower() == 'exit':
      break
    if name:
      clients[count] = name
      count += 1
  try:
    with open(filename, 'w', encoding = 'utf-8') as f:
      for client_id in clients:
        client_name = clients[client_id]
        f.write(f"Client name: {client_name.title()}\n")
      print(f"Clients' data saved successfully to the '{filename}' file")
  except IOError as e:
    print(f"File error - {e}")
  except Exception as e:
    print(f"An error occured - {e}")
if __name__ == "__main__":
  save_clients_data()