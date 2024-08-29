# Problem 1

# Write a program to create a dictionary of English words with values as their Urdu translation.
# Provide user with an option to look it up!

word_meaning = {
    "Chair" : "Kursi",
    "Table" : "Maiz",
    "Fan" : "Pankha",
    "Light" : "Roshni"
}

meaning = input("Enter the word you want to see the meaning: ")
print(word_meaning[meaning])