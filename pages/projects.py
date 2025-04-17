import streamlit as st

st.title("Firebase Studio Example Projects")

st.markdown("""
## Projects Built with Firebase Studio

Firebase Studio, powered by Gemini 2.5 Pro, enables rapid app development. Here are three impressive projects:

### 1. Tetris Game
- **Description**: A fully functional Tetris game built using just two natural language prompts.
- **Why Impressive**: Demonstrates Gemini 2.5 Pro’s ability to generate complex game logic quickly, a task that took days with older AI models.
- **Details**: Includes classic Tetris mechanics (block movement, rotation, scoring) with a clean UI.

### 2. Mind Map App
- **Description**: A web app that generates a mind map from a theme or topic, built in seconds.
- **Why Impressive**: Initially showed JSON data instead of rendering the map. A single follow-up prompt (*"Render the mind map, not JSON"*) fixed it, showcasing Gemini’s debugging prowess.
- **Details**: Supports dynamic node creation and visualization, ideal for brainstorming.

### 3. 3D Solar System
- **Description**: A 3D interactive app showing planet orbits and facts, created with minimal prompts.
- **Why Impressive**: Combines 3D rendering with educational content, built in minutes, highlighting Firebase Studio’s versatility.
- **Details**: Users can view each planet’s POV and access facts, all hosted on Firebase.

These projects show the power of Firebase Studio’s AI-driven development, enabling anyone to build sophisticated apps with minimal coding.
""")
