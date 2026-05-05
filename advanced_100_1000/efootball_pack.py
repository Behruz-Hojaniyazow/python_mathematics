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
  epic_names = ['Cristiano Ronaldo', 'Lionel Messi', 'Neymar']
    
  # 10 ta HIGHLIGHT 
  highlight_names = ['Kylian Mbappe', 'Lamine Yamal', 'Jude Bellingham', 'Vinicius Junior', 'Robert Lewandowskiy', 'Pau Cubarsi', 'Federico Valverde', 'Mikel Oyarzabal', 'Alvaro Carreras', 'Eduardo Camavinga']
  
  for name in highlight_names:
    players.append({'name' : name, 'type' : 'highlight'})
    
  # Qolgan NORMAL (150 yetkazamiz)
  normal_names = [
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
  players.extend(build_players(epic)
  
  # 🔹️ EPIC counter (global nazarot)
  total_epics_collected = set()
  
  while True:
    # STOP Agar hamma epic olingan bolsa
    if len(total_epics_collected) == 3:
      print("\n🔥You collected ALL EPIC players!")
      print("No need to open more packs ✅️")
      break
    if len(players) == 0:
      print("\n⚠️ Pack is empty")
      break
    try:
      user_coins = float(input("How many coins do you have? "))
    except ValueError:
      print("Please enter only numbers, try again")
      
    if user_coins < 900:
      print("\nYou don't have enough coins to open 10 players")
      
    
    choice = input("Choose (100/900): ")
    
    if choice.lower() == 'stop':
      break
    
    try:
      num = float(choice)
      coin = int(num) if num.is_integer() else num
    except ValueError:
      print("Please choose (100/900) actions or type 'stop' to exit")
    
    # =================
    # 🔹️ 900 COIN PACK
    # =================
    
    elif coin == 900:
      if len(players) < 10:
        print("⚠️ Not enough players left!")
        continue
      
      epic_players = []
      highlight_players = []
      normal_players = []
      
      random_players = random.sample(players, 10)
      
      # packdan ochirish
      for p in random_players:
        players.remove(p)
      print(f"\n📦 Remaining players: {len(players)}")
      for player in random_players:
        if player['type'] == 'epic':
          epic_players.append(player)
          total_epics_collected.add(player['name'])
            
        elif player['type'] == 'highlight':
          highlight_players.append(player)
          
        else:
          normal_players.append(player)
      # 🔥 Animation logic (loopdan tashqarida!)
      if len(epic_players) >= 2:
        print(f"\nBLACK ANIMATION!!! {len(epic_players)} EPIC players!")
      elif len(epic_players) == 1:
        print(f"\nEpic animation! You got: {epic_players[0] ['name']}")
      elif len(highlight_players) > 0:
        print("\n✨️ Highlight Animation!")
      else:
        print("\n🙂 Normal Pack")
      # 🔹️ Natijalar 
      if epic_players:
        print("EPIC:", ", ".join(p['name'] for p in epic_players))
      
      if highlight_players:
        print("HIGHLIGHT:", ", ".join(p['name'] for p in highlight_players))
        
      if normal_players:
        print("NORMAL:", ", ".join(p['name'] for p in normal_players))
        
    # ==================
    # 100 COIN PACK
    # ==================
        
    elif choice == 100:
      if len(players) < 1:
        print("⚠️ No players left")
        continue
      
      random_player = random.choice(players)
      players.remove(random_player)
      print(f"\n📦 Remaining players: {len(players)}")
      
      if random_player['type'] == 'epic':
        total_epics_collected.add(random_player['name'])
        print(f"\nEPIC!!! You Got {random_player['name']}")
        
      elif random_player['type'] == 'highlight':
        print(f"\n✨️HIGHLIGHT PLAYER!!! You Got {random_player['name']}")
        
      else:
        print(f"\n🙂NORMAL PLAYER: You Got {random_player['name']}")
        
    else:
      print("❌️ Invalid Choice!")
        
if __name__ == '__main__':
  pack_opening()