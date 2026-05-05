import random

# ================
# CONSTANTS
# ================
COST_SINGLE = 100
COST_MULTI = 900
TOTAL_EPICS = 3

def get_numbers(prompt):
  """
    Prompt the user for input and ensure that only an integer is accepted.

    This function repeatedly asks the user to enter a value until a valid
    integer is provided. If the user enters invalid input (e.g., text),
    an error message is displayed and the user is prompted again.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        int: A valid integer entered by the user.
  """
  
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("❌️ Enter your coins in integer format")
      
# ===============
# DATA CREATION
# ===============
def build_players(names, ptype):
  """
    Create a list of player dictionaries from given names and type.

    Each player is represented as a dictionary with 'name' and 'type'.

    Args:
        names (list): List of player names.
        ptype (str): Player type (e.g., 'epic', 'highlight', 'normal').

    Returns:
        list: List of player dictionaries.
    """
    
  return [{'name' : n, 'type' : ptype} for n in names]
  # ️🔹️ players (misol uchun)
  
def create_players():
  """
    Create the full list of players categorized by type.

    Includes EPIC, HIGHLIGHT, and NORMAL players.

    Returns:
        list: Combined list of all players.
    """
    
  players = []
  # 3 ta EPIC 
  epic = ['Cristiano Ronaldo', 'Lionel Messi', 'Neymar']
    
  # 10 ta HIGHLIGHT 
  highlight = ['Kylian Mbappe', 'Lamine Yamal', 'Jude Bellingham', 'Vinicius Junior', 'Robert Lewandowskiy', 'Pau Cubarsi', 'Federico Valverde', 'Mikel Oyarzabal', 'Alvaro Carreras', 'Eduardo Camavinga']
    
  # Qolgan NORMAL (150 yetkazamiz)
  normal = [
    "Antoine Griezmann", "Jan Oblak", "Rodrigo De Paul", "Julian Alvarez", "Marcos Llorente",
    "Koke", "Jose Maria Gimenez", "Robin Le Normand", "Conor Gallagher", "Alexander Sorloth",
    "Samuel Lino", "Axel Witsel", "Nico Williams", "Inaki Williams", "Oihan Sancet",
    "Gorka Guruzeta", "Dani Vivian", "Alex Berenguer", "Unai Simon", "Yeray Alvarez",
    "Takefusa Kubo", "Martin Zubimendi", "Brais Mendez", "Alex Remiro", "Nayef Aguerd",
    "Sheraldo Becker", "Luka Sucic", "Sergio Gomez", "Gerard Moreno", "Alex Baena",
    "Yeremy Pino", "Ayoze Perez", "Dani Parejo", "Pape Gueye", "Logan Costa",
    "Eric Bailly", "Viktor Tsygankov", "Bryan Gil", "Yaser Asprilla", "Arnau Martinez",
    "Daley Blind", "Miguel Gutierrez", "Ivan Martin", "Paulo Gazzaniga", "Giovani Lo Celso",
    "Isco", "Pablo Fornals", "Chimy Avila", "Marc Roca", "Diego Llorente",
    "Abde Ezzalzouli", "Rui Silva", "Isaac Romero", "Dodi Lukebakio", "Saul Niguez",
    "Loic Bade", "Djibril Sow", "Orjan Nyland", "Hugo Duro", "Pepelu",
    "Javi Guerra", "Jose Gaya", "Cristhian Mosquera", "Giorgi Mamardashvili", "Diego Lopez",
    "Ante Budimir", "Bryan Zaragoza", "Aimar Oroz", "Jon Moncayola", "Sergio Herrera",
    "Jesus Areso", "Borja Mayoral", "Bertug Yildirim", "Mauro Arambarri", "Djene Dakonam",
    "David Soria", "Luis Milla", "Iago Aspas", "Oscar Mingueza", "Fran Beltran",
    "Williot Swedberg", "Jonathan Bamba", "Vicente Guaita", "Vedat Muriqi", "Sergi Darder",
    "Dani Rodriguez", "Cyle Larin", "Dominik Greif", "Antonio Raillo", "Alberto Moleiro",
    "Kirian Rodriguez", "Oli McBurnie", "Mika Marmol", "Jasper Cillessen", "Sandro Ramirez",
    "Carlos Vicente", "Antonio Blanco", "Abdel Abqar", "Nahuel Tenaglia", "Jon Guridi",
    "Isi Palazon", "James Rodriguez", "Raul De Tomas", "Alvaro Garcia", "Abdul Mumin",
    "Augusto Batalla", "Javi Puado", "Leandro Cabrera", "Marash Kumbulla", "Alejo Veliz",
    "Omar El Hilali", "Gerard Valentin", "Jorge Pulido", "Sebastien Haller", "Munir El Haddadi",
    "Darko Brasanac", "Juan Cruz", "Marko Dmitrovic", "Matias Dituro", "Oscar Valentin",
    "Unai Lopez", "Pathe Ciss", "Florian Lejeune", "Ivan Villar", "Carl Starfelt",
    "Ilaix Moriba", "Tasos Douvikas", "Hugo Guillamon", "Sergi Canos", "Dimitri Foulquier",
    "Thierry Correia", "Andre Almeida", "Enzo Barrenechea", "Luis Rioja", "Samu Costa",
    "Johan Mojica", "Youssef En Nesyri"
  ]
  
  players.extend(build_players(epic,'epic'))
  players.extend(build_players(highlight,'highlight'))
  players.extend(build_players(normal,'normal'))
  return players
  
def get_player_type():
  """
    Randomly select a player type based on predefined probabilities.

    Probabilities:
        - EPIC: 5%
        - HIGHLIGHT: 25%
        - NORMAL: 70%

    Returns:
        str: Selected player type.
    """
    
  types = ['epic', 'highlight', 'normal']
  weights = [5, 25, 70]
  return random.choices(types, weights=weights)[0]
  
  # ==============
  # CORE LOGIC
  # ==============
def pick_player(players):
  """
    Select a random player from the list based on weighted type probability.

    Players are first grouped by type, then a type is selected using
    probability weights, and finally a random player is chosen from that group.

    Args:
        players (list): Available players.

    Returns:
        dict: Selected player.
    """
    
  # type boyicha ajratamiz
  epic = [p for p in players if p['type'] == 'epic']
  highlight = [p for p in players if p['type'] == 'highlight']
  normal = [p for p in players if p['type'] == 'normal']
  
  while True:
    ptype = get_player_type()
    if ptype == 'epic' and epic:
      return random.choice(epic)
      
    elif ptype == 'highlight' and highlight:
      return random.choice(highlight)
    elif ptype == 'normal' and normal:
      return random.choice(normal)
      
def open_single(players, collected_epics):
  """
    Open a single pack (1 player).

    Removes the selected player from the pool and updates EPIC collection.

    Args:
        players (list): Available players.
        collected_epics (set): Set of collected EPIC player names.
    """
    
  if not players:
    print("⚠️ No players left!")
    return
    
  p = pick_player(players)
  players.remove(p)
    
  print(f"\n📦 Remaining players: {len(players)}")
    
  if p['type'] == 'epic':
    collected_epics.add(p['name'])
    print(f"🔥 EPIC: {p['name']}")
    
  elif p['type'] == 'highlight':
    print(f"✨️ HIGHLIGHT: {p['name']}")
    
  else:
    print(f"🙂 NORMAL: {p['name']}")
      
def open_multi(players, collected_epics):
  """
    Open a multi-pack (10 players).

    Selects 10 players, removes them from the pool, and categorizes results.

    Args:
        players (list): Available players.
        collected_epics (set): Set of collected EPIC player names.
    """
    
  if len(players) < 10:
    print("⚠️ Not enough players!")
    return
  
  pulled = []
  
  for _ in range(10):
    p = pick_player(players)
    players.remove(p)
    pulled.append(p)
  
  print(f"\n📦 Remaining players: {len(players)}")
  
  epic, highlight, normal = [], [], []
  for p in pulled:
    if p['type'] == 'epic':
      epic.append(p)
      collected_epics.add(p['name'])
    elif p['type'] == 'highlight':
      highlight.append(p)
    else:
      normal.append(p)
      
  # animation
  if len(epic) >= 2:
    print("🖤 BLACK ANIMATION!")
  elif len(epic) == 1:
    print("🔥 EPIC ANIMATION!")
  elif highlight:
    print("✨️ HIGHLIGHT ANIMATION!")
    
  # result  
  if epic:
    print("EPIC:", ", ".join(p['name'] for p in epic))
  if highlight:
    print("HIGHLIGHT:", ", ".join(p['name'] for p in highlight))
  if normal:
    print("NORMAL:", ", ".join(p['name'] for p in normal))
    
# ===============
# GAME LOOP
# ===============
def run_game():
  """
    Main game loop.

    Handles user interaction, coin management, and pack opening logic.
    The game continues until:
        - Coins run out
        - All EPIC players are collected
        - Player pool becomes empty
        - User exits manually
    """
    
  players = create_players()
  collected_epics = set()
  
  coins = get_numbers("\n💰 Enter your coins:  ")
  
  while True:
    print(f"\n💰 Coins: {coins}")
    
    # stop conditions
    if coins < COST_SINGLE:
      print("❌️ Not enough coins!")
      break
    
    if len(collected_epics) == TOTAL_EPICS:
      print("🏆 All EPIC Players Collected!")
      break
    
    if not players:
      print("⚠️ Pack is empty!")
      break
    
    print("\n1 → 100 coins (1 player)")
    print("2 → 900 coins (10 players)")
    print("Type 'stop' to exit")
    
    choice = input("Choose an action: ").strip().lower()
    
    if choice == 'stop':
      break
    
    elif choice == '1':
      if coins < COST_SINGLE:
        print("❌️ Not enough coins!")
        continue
      
      coins -= COST_SINGLE
      open_single(players, collected_epics)
      
    elif choice == '2':
      if coins < COST_MULTI:
        print("❌️ Not enough coins!")
        continue
      
      coins -= COST_MULTI
      open_multi(players, collected_epics)
      
    else:
      print("❌️ Invalid choice!")
      
# ===================
# ENTRY
# ===================
if __name__ == '__main__':
  run_game()