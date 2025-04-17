import streamlit as st

st.title("Tips for Vibe Coding with Firebase Studio")

st.markdown("""
## Tips for Vibe Coding with Firebase Studio

Maximize your Firebase Studio experience with these best practices:

- **Start Simple**: Use the App Prototyping agent for quick ideas, then switch to Code view for customization.
- **Be Specific with Prompts**: Clearly describe issues or features, e.g., *"The eraser doesn’t remove lines. Fix it."*
- **Iterate Freely**: Roll back changes easily to experiment without fear.
- **Leverage Gemini’s Reasoning**: Gemini 2.5 Pro debugs and optimizes without needing step-by-step instructions.
- **Explore Templates**: Use 60+ templates for dashboards, chat apps, and more to jumpstart projects.
- **Customize with Nix**: Configure workspaces for specific frameworks (React, Flutter, Node.js).

**Privacy Tip**: To prevent prompts/code from being used for model training, disable the App Prototyping agent, Gemini in Firebase, and code completion/indexing in settings. Always validate AI-generated code before production.
""")
