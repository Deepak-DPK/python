# ============================================
# 1. Case Conversion
# ============================================
print("--- 1. Case Conversion ---")
name = "deepAk R"
print(f"Original: '{name}'")
print(f"UPPERCASE: {name.upper()}")
print(f"lowercase: {name.lower()}")
print(f"Capitalized: {name.capitalize()}") # Capitalizes only the first character
print("\n")


# ============================================
# 2. String Masking
# ============================================
print("--- 2. String Masking ---")
mobile_number = "82148121857"
# Slicing: get the first 2 and last 2 characters
masked_number = mobile_number[:2] + "******" + mobile_number[-2:]
print(f"Your masked number: {masked_number}")
print("\n")


# ============================================
# 3. String Formatting
# ============================================
print("--- 3. String Formatting ---")
movie_name = "mangatha"
hero_cast = "Ajith kumar"
director = "venkat prabhu"
# Using an f-string with the .title() method to capitalize each word
movie_description = f"{movie_name.title()} - {hero_cast.title()} - {director.title()}"
print(movie_description)
print("\n")


# ============================================
# 4. Cleaning and Extracting Data (split & strip)
# ============================================
print("--- 4. Cleaning and Extracting ---")
message = "hi your otp is :2212234 , dont share to any one"
# Method chaining: split by ':', take the second part, split by ',', take the first, and strip whitespace
otp = message.split(":")[1].split(",")[0].strip()
print(f"Extracted OTP: {otp}")
print("\n")


# ============================================
# 5. Searching in Strings
# ============================================
print("--- 5. Searching in Strings ---")
# Using the 'in' keyword to check for existence (returns True/False)
locker_message = "all your data is stored in 232323 number locker"
if "232323" in locker_message:
    print("Locker ID is present in the message.")

# Using .find() to get the starting position (index) of a substring
text = "the hasty of the nasty to the custy of the lasty"
position = text.find("nasty") # Returns -1 if not found
print(f"The word 'nasty' starts at position: {position}")
print("\n")


# ============================================
# 6. Advanced Operations
# ============================================
print("--- 6. Advanced Operations ---")
# Create initials from a comma-separated string
full_name = "deepak,ramesh"
initials = ". ".join([word[0].upper() for word in full_name.split(",")]) + "."
print(f"Initials for '{full_name}': {initials}")

# Clean leading/trailing whitespace
spaced_name = "    deepak ramesh palani     "
cleaned_name = spaced_name.strip()
print(f"Cleaned name: '{cleaned_name}'")

# Count words in a string
story = "mana is the largest animal of the era in the current world"
word_count = len(story.split())
print(f"The story has {word_count} words.")

# Count parts of a string when split by a word
# Splitting by "animal" creates a list of the parts before and after it.
parts = story.split("animal")
print(f"Splitting the story by 'animal' results in {len(parts)} parts.")