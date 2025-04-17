import streamlit as st

st.set_page_config(page_title="Firebase Studio Guide App", layout="wide")

st.title("Welcome to the Firebase Studio Guide App")
st.write("""
This app provides a comprehensive guide to Google Firebase Studio, powered by Gemini 2.5 Pro, the world's leading AI model for coding. 
Navigate through the pages to:
- Learn how to set up Firebase Studio to build apps like a whiteboard.
- Explore example projects (Tetris, Mind Map, 3D Solar System) built with Firebase Studio.
- Understand why Firebase Studio is a game-changer for developers.
- Get tips for vibe coding with Firebase Studio’s AI-driven tools.
""")

st.subheader("Get Started")
st.write("Use the sidebar to explore the different sections of the guide. Save notes on the Setup Guide page using Firebase Firestore!")
