friend = {
    "first_name" : "behruz",
    "last_name" : "hojaniyazow",
    "age" : 18,
    "city" : "dashoguz"
}
#name = friend.get("first_name", "No point value assigned")
#print(name.title())
print("\n---Info about my friend---\n")
for key, value in friend.items():
  print(f"{key} - {value}")