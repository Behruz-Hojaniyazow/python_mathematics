music = ["song1", "song2", "song3", "song4"]
while True:
  print("\n---Menu---")
  print("press '1' to add song")
  print("press '2' to delete the last song")
  print("press '3' to delete by name")
  print("press '4' to stop the project")
  choice = input("Which action would you like to prefer? ")
  if choice == '1':
    song_name = input("which song do you want to add ? ") \
    .strip().lower()
    music.append(song_name)
    print("\n---Current playlist---")
    print(f"{music}")
  elif choice == '2':
    if music:
      removed_song = music.pop()
      print("The last song was deleted")
      print(f"Deleted song: {removed_song}")
      print(f"\n---Current playlist---")
      print(f"{music}")
    else:
      print("There is nothing to delete, Playlist is empty")
      print("\n---Current Playlist---")
      print(music)
  elif choice == '3':
    print("\nHere are the names of the songs")
    print(music)
    song_name = input("Which song do you wanna delete? ") \
    .strip().lower()


    if song_name in music:
      music.remove(song_name)
      print(f"{song_name} song was deleted successfully")
      print("---Current playlist")
      print(music)
    else:
      print("We don't have this song in our playlist")
      print("---Current playlist---")
      print(music)
  elif choice == '4':
    print("\n---Current playlist---")
    print(music)
    break
  else:
    print("you entered the wrong menu,please try again")
    
print(f"\nHere are the songs")
print(music)