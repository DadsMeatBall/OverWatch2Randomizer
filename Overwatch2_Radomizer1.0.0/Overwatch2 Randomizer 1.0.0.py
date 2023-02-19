import random

# Open the input file for reading
with open("input_file.txt", "r") as input_file:
    # Read the contents of the file into a string
    input_text = input_file.read()

# Split the input text into a list of lines
lines = input_text.splitlines()

# Loop through each line in the list
for i in range(len(lines)):
    # Check if the line contains "@" or "*" or "&"
    if "@" in lines[i] or "*" in lines[i] or "&" in lines[i] or "`" in lines[i] or "$" in lines[i] or "!" in lines[i] or "#" in lines[i] or "|" in lines[i] or "?" in lines[i] or "+" in lines[i] or "~" in lines[i] or "=" in lines[i] or "^" in lines[i] or "_" in lines[i]:
        # Split the line into a list of words
        words = lines[i].split()
        # Loop through each word in the list
        for j in range(len(words)):
            # Check if the word contains "@" or "*"
            if "@" in words[j]:
                # Generate a random number between 0 and 500 Bulk
                random_number = random.randint(0, 500)
                # Replace "@" with the random number
                words[j] = words[j].replace("@", str(random_number))
            elif "*" in words[j]:
                # Generate a random number between 25 and 500 Ammo 
                random_number = random.randint(25, 500)
                # Replace "*" with the random number
                words[j] = words[j].replace("*", str(random_number))
            elif "&" in words[j]:
                # Generate a random number between 10 and 500 Damg
                random_number = random.randint(10, 500)
                # Replace "&" with the random number
                words[j] = words[j].replace("&", str(random_number))
            elif "`" in words[j]:
                # Generate a random number between 25 and 800 jump
                random_number = random.randint(25, 800)
                # Replace "`" with the random number
                words[j] = words[j].replace("`", str(random_number))
            elif "$" in words[j]:
                # Generate a random number between 25 and 400 move grav
                random_number = random.randint(25, 400)
                # Replace "$" with the random number
                words[j] = words[j].replace("$", str(random_number))
            elif "!" in words[j]:
                # Generate a random number between 50 and 300 move speed
                random_number = random.randint(50, 300)
                # Replace "!" with the random number
                words[j] = words[j].replace("!", str(random_number))
            elif "#" in words[j]:
                # Generate a random number between 0 and 300 ashe and maybe more
                random_number = random.randint(0, 300)
                # Replace "#" with the random number
                words[j] = words[j].replace("#", str(random_number))
            elif "?" in words[j]:
                # Generate a random number between 0 and 400 
                random_number = random.randint(0, 400)
                # Replace "?" with the random number
                words[j] = words[j].replace("?", str(random_number))
            elif "+" in words[j]:
                # Generate a random number between 0 and 200  DVA
                random_number = random.randint(0, 200)
                # Replace "+" with the random number
                words[j] = words[j].replace("+", str(random_number))
            elif "~" in words[j]:
                # Generate a random number between 33 and 500  DOOOOOOOOOOOOOOOOOOM FISTER
                random_number = random.randint(33, 500)
                # Replace "+" with the random number
                words[j] = words[j].replace("~", str(random_number))
            elif "=" in words[j]:
                # Generate a random number between 3 and 12  HASSSS NO BALLS
                random_number = random.randint(3, 12)
                # Replace "=" with the random number
                words[j] = words[j].replace("=", str(random_number))
            elif "|" in words[j]:
                # Generate a random number between 25 and 300 Lady torb
                random_number = random.randint(25, 300)
                # Replace "=" with the random number
                words[j] = words[j].replace("|", str(random_number))
            elif "^" in words[j]:
                # Generate a random number between 40 and 400 
                random_number = random.randint(40, 400)
                # Replace "^" with the random number
                words[j] = words[j].replace("^", str(random_number))
            elif "_" in words[j]:
                # Generate a random number between 0 and 100 MEEEEEEEEEEEEEEI
                random_number = random.randint(0, 100)
                # Replace "+" with the random number
                words[j] = words[j].replace("_", str(random_number))
        # Join the list of words back into a single line
        lines[i] = " ".join(words)
# Join the list of lines back into a single string
output_text = "\n".join(lines)

# Open the output file for writing
with open("output_file.txt", "w") as output_file:
    # Write the modified text to the output file
    output_file.write(output_text)
