
# Simple Dictionary program

# Predefined dictionary with more words and their meanings
dictionary = {
    "python": "A high-level programming language used for general-purpose programming.",
    "algorithm": "A process or set of rules to be followed in calculations or problem-solving operations.",
    "data": "Facts and statistics collected together for reference or analysis.",
    "function": "A block of code which only runs when it is called, it can take parameters and return a value.",
    "variable": "A storage location in computer memory used to store data, that can change during the program execution.",
    "class": "A blueprint for creating objects, providing initial values for state (member variables), and implementations of behavior (member functions or methods).",
    "object": "An instance of a class, which holds data and methods that operate on that data.",
    "exception": "An event that occurs during the execution of a program that disrupts the normal flow of instructions.",
    "debug": "The process of finding and fixing defects or problems within a computer program.",
    "string": "A sequence of characters, typically used to represent text in a program.",
    "list": "A collection data type in Python that is ordered, mutable, and allows duplicates.",
    "tuple": "An ordered collection of elements which is immutable and cannot be changed after creation.",
    "dictionary": "A collection of key-value pairs in Python, where each key must be unique and is used to store data.",
    "set": "A collection of unique elements, unordered and mutable.",
    "boolean": "A data type that can have one of two values: `True` or `False`.",
    "loop": "A sequence of instructions that is continually repeated until a certain condition is met.",
    "iteration": "The process of repeating a set of operations, often used in loops.",
    "recursion": "A method where the solution to a problem depends on solutions to smaller instances of the same problem.",
    "parameter": "A variable used in a function to accept a value that will be used in the function.",
    "module": "A file containing Python definitions and statements, typically used to organize code into logical sections.",
    "package": "A collection of modules organized in directories and subdirectories for reuse in Python."
}

def search_word(word):
    """Function to search for a word in the dictionary."""
    word = word.lower()  # Convert the word to lowercase to make the search case-insensitive
    if word in dictionary:
        return dictionary[word]
    else:
        return "Sorry, the word is not found in the dictionary."

def main():
    print("Welcome to the Simple Python Dictionary!")
    
    while True:
        print("\nOptions:")
        print("1. Search for a word")
        print("2. Exit")
        
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            word = input("Enter the word you want to search for: ")
            definition = search_word(word)
            print(f"Definition of '{word}': {definition}")
        
        elif choice == "2":
            print("Exiting the dictionary. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
