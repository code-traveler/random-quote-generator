import random

quotes = [
    "Keep going. Everything you need will come to you.",
    "Dream big. Start small. Act now.",
    "Success is not for the lazy.",
    "Push yourself, because no one else is going to do it for you.",
    "Don't watch the clock; do what it does. Keep going.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Believe you can and you're halfway there.",
    "Your limitation—it's only your imagination.",
    "Sometimes later becomes never. Do it now.",
    "Great things never come from comfort zones.",
]

def show_random_quote():
    if quotes:
        print("\n✨ Quote of the Day ✨")
        print(random.choice(quotes))
    else:
        print("\nNo quotes available. Add one!")

def view_all_quotes():
    if quotes:
        print("\n📚 All Quotes:")
        for i, quote in enumerate(quotes, 1):
            print(f"{i}. {quote}")
    else:
        print("\nNo quotes to show.")

def add_quote():
    new_quote = input("\nEnter a new quote: ").strip()
    if new_quote:
        quotes.append(new_quote)
        print("✅ Quote added!")
    else:
        print("⚠️ Empty quote not added.")

def delete_quote():
    if not quotes:
        print("\nNo quotes to delete.")
        return
    view_all_quotes()
    try:
        index = int(input("\nEnter quote number to delete: ")) - 1
        if 0 <= index < len(quotes):
            removed = quotes.pop(index)
            print(f"❌ Deleted: {removed}")
        else:
            print("⚠️ Invalid number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    while True:
        print("\n=== Random Quote Generator ===")
        print("1. Show Random Quote")
        print("2. Add Quote")
        print("3. View All Quotes")
        print("4. Delete Quote")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_random_quote()
        elif choice == "2":
            add_quote()
        elif choice == "3":
            view_all_quotes()
        elif choice == "4":
            delete_quote()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice.")

if __name__ == "__main__":
    main()
