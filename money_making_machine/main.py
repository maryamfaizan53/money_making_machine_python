import streamlit as st
import random
import time
import requests

st.title("💰 Money Making Machine 💰")

# Function to generate random money
def generate_money():
    return random.randint(1, 1000)

st.subheader("💸 Instant Cash Generator 💸")
if st.button("Generate Money"):
    st.write("Counting Your Money...")
    time.sleep(1)
    amount = generate_money()
    st.success(f"You have made: **${amount}** 🎉")


# Function to fetch side hustle ideas
def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustles"]
        else:
             return "Freelancing"
    except Exception as e:
        return "Something went wrong"

st.subheader("🚀 Side Hustle Ideas 🚀")
if st.button("Generate Idea"):
    idea = fetch_side_hustle()
    st.success(idea)


# Function to fetch money-related quotes
def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quote = response.json()
            return quote["money_quote"]
        else:
            return "Money is a tool"
    except:
        return "Something went wrong"

st.subheader("💡 Money Making Motivation 💡")
if st.button("Get Inspired"):
    quote = fetch_money_quotes()
    st.info(quote)
