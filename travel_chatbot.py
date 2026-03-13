import random

def suggest_destination():
    destinations = ["Japan", "Italy", "Canada", "Australia", "South Korea"]
    suggestion = random.choice(destinations)
    print(f"I recommend visiting {suggestion}! It’s a great place to explore.")

def packing_list():
    print("Here are some basic things you should pack:")
    items = ["Clothes", "Toothbrush", "Passport", "Phone Charger", "Money"]
    for item in items:
        print("- " + item)

def travel_tip():
    tips = [
        "Always keep a copy of your passport.",
        "Learn a few local phrases before traveling.",
        "Keep your valuables secure.",
        "Check the weather before packing.",
        "Try local food and explore the culture!"
    ]
    print(random.choice(tips))

def chatbot():
    print("Welcome to the Travel Assistant Chatbot!")
    print("I can help with destinations, packing lists, and travel tips.")
    
    while True:
        print("\nWhat would you like help with?")
        print("1. Destination suggestion")
        print("2. Packing checklist")
        print("3. Travel tip")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                suggest_destination()
            elif choice == 2:
                packing_list()
            elif choice == 3:
                travel_tip()
            elif choice == 4:
                print("Thanks for using the Travel Assistant Chatbot. Safe travels!")
                break
            else:
                print("Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")

chatbot()
