# --- Initial Setup ---
playlist = ["maara", "thoza", "kanna", "thalapathi", "varisu"]
food = ["idly", "dosa", "sambar", "rice"]
location = [ "tirupathur", "chennai","vellore", "bangalore"]

print("======== INITIAL LISTS ========")
print(f"Playlist: {playlist}")
print(f"Food:     {food}")
print(f"Location: {location}\n")


# --- Modifying the 'playlist' List ---
print("======== PLAYLIST MODIFICATIONS ========")
# append(): Adds 'maari' to the end.
playlist.append("maari")
print(f"After append('maari'):   {playlist}")

# insert(): Adds 'vaathi' at index 2.
playlist.insert(2, "vaathi")
print(f"After insert(2,'vaathi'): {playlist}")

# remove(): Removes the first 'thoza'.
playlist.remove("thoza")
print(f"After remove('thoza'):    {playlist}")

# clear(): Empties the list.
playlist.clear()
print(f"After clear():          {playlist}\n")


# --- Working with the 'food' List ---
print("======== FOOD LIST MODIFICATIONS ========")
# copy(): Creates a new, identical list.
food_copy = food.copy()
print(f"Copied food list:       {food_copy}")

# extend(): Adds multiple items to the end.
food.extend(["curd rice", "biryani", "pizza"])
print(f"After extend():         {food}")

# sort(): Sorts the list alphabetically.
food.sort()
print(f"After sort():           {food}\n")


# --- Working with the 'location' List ---
print("======== LOCATION LIST MODIFICATIONS ========")
# reverse(): Reverses the current order of the list.
location.reverse()
print(f"After reverse():        {location}")

# sort(): Sorts the list alphabetically.
location.sort()
print(f"After sort():           {location}")

# pop(): Removes the last item from the list, three times.
location.pop()
print(f"After first pop():      {location}")
location.pop()
print(f"After second pop():     {location}")
location.pop()
print(f"After third pop():      {location}\n")