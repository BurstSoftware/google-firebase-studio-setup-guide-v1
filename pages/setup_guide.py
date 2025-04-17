import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import os

# Initialize Firebase (only once)
if not firebase_admin._apps:
    cred = credentials.Certificate("firestore-key.json")
    firebase_admin.initialize_app(cred)
db = firestore.client()

st.title("Firebase Studio Setup Guide")

st.markdown("""
## Google Firebase Studio Setup Guide

Firebase Studio is a cloud-based development environment powered by Gemini 2.5 Pro, enabling you to build full-stack AI apps. Follow these steps to set up and create a whiteboard app like Miro or Tldraw.

### 1. Get Started with Firebase Studio
- Navigate to [firebase.studio](https://firebase.studio).
- Check the terms box and click **Get Started**.
- You'll land on the Firebase Studio dashboard.

### 2. Prototype Your App
- Describe your app idea, e.g., *"Create a simple whiteboard web app with drawing, shape tools, and text."*
- Optionally, upload a UI sketch (<3MiB).
- Click **Prototype with AI** to generate an app blueprint with features, style guidelines, and more.
- Edit the blueprint via prompts (e.g., *"Change color scheme to blue."*) and click **Prototype this App**.

### 3. Preview and Test
- View the generated app in the preview pane.
- Test features like drawing, shapes, and text. Note any issues (e.g., drawing not rendering).

### 4. Connect Gemini 2.5 Pro
- Click **Switch to Code** in the top right.
- In the Gemini chat pane, select **Gemini 2.5 Pro Experimental (0.325)**.
- Add a Gemini API key:
  - Click the **Gemini API key** link to open Google AI Studio.
  - Select/create a Google Cloud project, then **Create API Key**.
  - Copy the key, paste it into Firebase Studio’s **AI: Gemini API Key** field in User Settings.
  - **Important**: Treat the key like a password.
- Ensure Gemini 2.5 Pro is selected.

### 5. Debug and Enhance
- Drag the Gemini chat pane to view the app preview.
- Report issues, e.g., *"Drawing icon doesn’t draw. Fix it."*
- Gemini suggests fixes (e.g., update `page.tsx`). Apply changes via **Update File**.
- Reload the preview to test (e.g., drawing with color picker should work).
- Fix other issues, e.g., *"Eraser doesn’t work. Fix it."*

### 6. Add Shapes and Polish
- Test shape tools (circle, square, triangle). Fix issues via prompts, e.g., *"Fix circle rendering."*
- Enhance with prompts like *"Add a customizable text tool."*

### 7. Publish and Share
- Click **Publish** to deploy via Firebase App Hosting (requires a Cloud Billing account).
- Generate a public URL or QR code to share.
- Monitor performance in the Firebase Console.

For detailed pricing, visit [firebase.google.com](https://firebase.google.com).
""")

# Firestore Integration: Save and Display Notes
st.subheader("Save Notes to Firestore")
note = st.text_area("Add a note about Firebase Studio setup:")
if st.button("Save Note"):
    if note:
        db.collection("setup_notes").add({"note": note, "timestamp": firestore.SERVER_TIMESTAMP})
        st.success("Note saved to Firestore!")
    else:
        st.error("Please enter a note.")

st.subheader("Saved Notes")
notes = db.collection("setup_notes").order_by("timestamp", direction=firestore.Query.DESCENDING).stream()
for doc in notes:
    data = doc.to_dict()
    st.write(f"- {data['note']} (Saved: {data['timestamp']})")
