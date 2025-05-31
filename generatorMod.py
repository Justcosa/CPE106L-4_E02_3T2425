import random

articles = ("A", "THE")

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase using nouns from a file if available."""
    try:
        with open("nouns.txt", "r") as file:
            nouns_from_file = [line.strip().upper() for line in file if line.strip()]
        if nouns_from_file:
            noun = random.choice(nouns_from_file)
        else:
            noun = "THING"  # Default noun if file is empty
    except FileNotFoundError:
        noun = "THING"  # Default noun if file is missing
    return random.choice(articles) + " " + noun

def verbPhrase():
    """Builds and returns a verb phrase using verbs from a file if available."""
    try:
        with open("verbs.txt", "r") as file:
            verbs_from_file = [line.strip().upper() for line in file if line.strip()]
        if verbs_from_file:
            verb = random.choice(verbs_from_file)
        else:
            verb = "DOES"  # Default verb if file is empty
    except FileNotFoundError:
        verb = "DOES"  # Default verb if file is missing
    return verb + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase using prepositions from a file if available."""
    try:
        with open("prepositions.txt", "r") as file:
            prepositions_from_file = [line.strip().upper() for line in file if line.strip()]
        if prepositions_from_file:
            preposition = random.choice(prepositions_from_file)
        else:
            preposition = "WITH"  # Default preposition if file is empty
    except FileNotFoundError:
        preposition = "WITH"  # Default preposition if file is missing
    return preposition + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main()