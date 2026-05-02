from mix import get_mix_list

def mix_nums():
  print("\n" + "=" * 35)
  print("🃏 Kryos Data Mixer Tool")
  print("=" * 35)
  
  items = []
  
  print("Type 'stop' to finish\n")
  while True:
    item = input(f"{len(items) + 1}: Enter an item: ")
    
    if item.lower() == 'stop':
      break
    
    if item:
      items.append(item)
    else:
      print("⚠️ Do not enter a blank value")
      
  if len(items) > 1:
    mixed_list = get_mix_list(items)
    
    print("\n" + "=" * 30)
    print("\tMixed Items")
    print("-" * 30)
    print(f"{', '.join(mixed_list)}")
    print("=" * 30)
    
  else:
    print("\n❌️You need at least 2 things to mix")
  
if __name__ == '__main__':
  mix_nums()