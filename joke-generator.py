import streamlit as st
import requests
import random

# Function to fetch a random joke from an API
def fetch_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        data = response.json()
        return data["setup"], data["punchline"]
    else:
        return "Couldn't fetch the joke", ""

# Streamlit app
def main():
    st.title("Random Joke Generator")
    st.subheader("Click the button below to get a random joke!")

    if st.button("Generate Joke"):
        setup, punchline = fetch_joke()
        emojis = ["😁", "🤣", "😂"]
        emojiToPick = random.randint(0, 2)
        st.write(f"Q: {setup}")
        st.write(f"A: {punchline} {emojis[emojiToPick]}")

if __name__ == "__main__":
    main()
