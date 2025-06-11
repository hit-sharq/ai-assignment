# CryptoBuddy: A Rule-Based Cryptocurrency Advisor Chatbot

def crypto_advisor_chatbot():
    # Chatbot Personality
    bot_name = "CryptoBuddy"
    bot_tone = "Hey there! Let’s find you a green and growing crypto! 🌱\n(You can ask me things like 'Which crypto is trending up?', 'What’s the most sustainable coin?', or 'Which coin should I buy for long-term growth?')"

    # Predefined Crypto Data
    crypto_db = {
        "Bitcoin": {
            "price_trend": "rising",
            "market_cap": "high",
            "energy_use": "high",
            "sustainability_score": 3/10
        },
        "Ethereum": {
            "price_trend": "stable",
            "market_cap": "high",
            "energy_use": "medium",
            "sustainability_score": 6/10
        },
        "Cardano": {
            "price_trend": "rising",
            "market_cap": "medium",
            "energy_use": "low",
            "sustainability_score": 8/10
        }
    }

    print(f"{bot_name}: {bot_tone}")

    while True:
        user_query = input("You: ").lower()

        if user_query in ["exit", "quit", "bye"]:
            print(f"{bot_name}: Goodbye! Happy investing! 🚀")
            break

        # Logic for asking bot's name
        if "your name" in user_query or "who are you" in user_query:
            print(f"{bot_name}: I am {bot_name}, your friendly crypto advisor! Ask me about trending or sustainable cryptocurrencies!")

        # Logic for sustainability queries
        elif "sustainable" in user_query or "eco" in user_query or "green" in user_query:
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            print(f"{bot_name}: Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")

        # Logic for trending up queries
        elif "trending" in user_query or "rising" in user_query or "price" in user_query:
            # Prioritize coins with price_trend = "rising" and market_cap = "high"
            candidates = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising" and data["market_cap"] == "high"]
            if candidates:
                recommend = candidates[0]
                print(f"{bot_name}: {recommend} is trending up with a high market cap! 🚀")
            else:
                print(f"{bot_name}: No top trending coins with high market cap found right now.")

        # Logic for long-term growth queries
        elif "long-term" in user_query or "growth" in user_query or "buy" in user_query:
            # Prioritize coins with price_trend = "rising" and sustainability_score > 7/10
            candidates = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising" and data["sustainability_score"] > 7/10]
            if candidates:
                recommend = candidates[0]
                print(f"{bot_name}: {recommend} is trending up and has a top-tier sustainability score! 🚀")
            else:
                print(f"{bot_name}: No coins match the long-term growth criteria right now.")

        else:
            print(f"{bot_name}: Sorry, I didn’t understand that. Ask me about trending or sustainable cryptocurrencies!")

if __name__ == "__main__":
    crypto_advisor_chatbot()
