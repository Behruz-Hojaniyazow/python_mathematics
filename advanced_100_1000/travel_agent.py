import travel_choice as tc

def main():
  print("\n--- Kryos Global Travle Agent ---")
  destinations = []
  for i in range(5):
    place = input(f"{i+1} Enter travel direction").strip().title()
    if place:
      destinations.append(place)
    else:
      print("⚠️ The route name must not be empty!")
      
  if destinations:
    chosen_one = tc.get_random_destination(destinations)
    sorted_list = tc.get_sorted_destinations(destinations)
    print("\n" + "=" * 40)
    print(f"✈️ Recommended destination for you is: {chosen_one}")
    print(f"📍 All directions (sorted): {', '.join(sorted_list)}")
    print("=" * 40)

if __name__ == '__main__':
  main()