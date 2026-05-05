import random

# ================
# CONSTANTS
# ================
COST_SINGLE = 100
COST_MULTI = 900
TOTAL_EPICS = 3

# ===============
# DATA CREATION
# ===============
def build_players(names, ptype):
  return [{'name' : n, 'type' : ptype} for n in names]
  # ️🔹️ players (misol uchun)
  
def create_players():
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
  
  players.extend(build_players(epic,('epic'))
  players.extend(build_players(highlight,('highlight'))
  players.extend(build_players(normal,('normal'))
  return players
  
def get_player_type():
  types = ['epic', 'highlight', 'normal']
  weights = [5, 25, 70]
  return random.choices(types, weights=weights)[0]
  
  # ==============
  # CORE LOGIC
  # ==============
def pick_player(players):
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
  if len(players) < 10:
    print("⚠️ Not enough players!")
    return
  
  pulled = []
  
  for _ range(10):
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
  players = create_players()
  collected_epics = set()
  
  coins = int(input("💰 Enter your coins: "))
  
  while True:
    print(f"\n💰 Coins: {coins}
    ")
    
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
      
      open_multi(players, collected_epics)
      
# ===================
# ENTRY
# ===================
if __name__ == '__main__':
  run_game()