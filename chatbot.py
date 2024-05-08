# Define a dictionary of questions and answers for the shopping mall chatbot
qa_pairs = {
    "stores": "Our shopping mall has a variety of stores including fashion, electronics, home goods, and more.",
    "events": "You can check our mall website or social media pages for information about upcoming events and promotions.",
    "restaurants": "Yes, we have a food court with a variety of restaurants offering different cuisines.",
    "hours": "Our mall hours are [insert mall hours here]. We look forward to your visit!",
    "parking": "We offer parking facilities with both indoor and outdoor options for your convenience.",
    "amenities": "Our mall has amenities such as restrooms, ATMs, and seating areas throughout the premises.",
}

# Define a function to handle queries and generate suggestive responses
def mall_chatbot(query):
    query = query.lower()
    if query in qa_pairs:
        return f"You might want to know: {qa_pairs[query]}"
    
    # Check if the query word is related to any sentence in the QA pairs
    related_pairs = {key: value for key, value in qa_pairs.items() if query in value.lower()}
    if related_pairs:
        related_key = list(related_pairs.keys())[0]  # Get the first related key
        return f"You might want to know: {related_pairs[related_key]}"
    
    return "I'm sorry, I don't have information on that specific topic. Can you ask another question?"

# Function to greet the user with their name
def greet_user():
    name = input("Welcome to the Shopping Mall Chatbot! May I know your name? ")
    print(f"Hello, {name}! How can I assist you today?")
    return name

# Main loop for interacting with the shopping mall chatbot
def main():
    name = greet_user()
    
    print("This chatbot responds to queries and suggests related responses if a word matches a sentence.")
    
    while True:
        user_input = input("Your Query: ")
        if user_input.lower() == 'exit':
            print(f"Goodbye, {name}! Have a great day.")
            break
        else:
            print("Chatbot:", mall_chatbot(user_input))

if __name__ == "__main__":
    main()

