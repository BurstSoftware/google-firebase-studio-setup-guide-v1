import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json
import os

# Initialize Firebase only if credentials are available
db = None
if not firebase_admin._apps:
    try:
        if "FIREBASE_CREDENTIALS" in st.secrets:
            # Use Streamlit Secrets for cloud deployment
            cred = credentials.Certificate(json.loads(st.secrets["FIREBASE_CREDENTIALS"]))
        else:
            # Fallback to local firestore-key.json
            if not os.path.exists("firestore-key.json"):
                raise FileNotFoundError("firestore-key.json not found in the project directory.")
            cred = credentials.Certificate("firestore-key.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()
    except Exception as e:
        st.warning(f"Firebase Firestore is not available: {str(e)}")
        st.markdown("""
        **Note**: The note-saving feature requires Firebase setup. To enable it:
        - **Local**: Place `firestore-key.json` in the project root (download from [Firebase Console > Project Settings > Service Accounts](https://console.firebase.google.com)).
        - **Streamlit Cloud**: Add `FIREBASE_CREDENTIALS` to secrets with the JSON content of `firestore-key.json`.
        See [Firebase Setup Guide](https://firebase.google.com/docs/admin/setup) for details.
        """)

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

For detailed pricing, visit [firebase.google.com](https://firebase.google.com) or see the pricing section below.
""")

# Pricing Section
st.subheader("Firebase Studio Pricing (April 2025)")
st.markdown("""
Firebase Studio is in preview as of April 2025, offering a generous no-cost tier for developers. Below is a detailed breakdown of pricing and related costs.[](https://firebase.google.com/docs/studio)

### Workspace Pricing
- **No-Cost Tier**:
  - **Three Workspaces**: Free for all users, supporting prototyping, coding, and deployment.
  - **Google Developer Program**:
    - **Standard (Free)**: Join the [Google Developer Program](https://developers.google.com/community/gdsc) to increase to 10 workspaces.
    - **Premium**: Subscribe to the Google Developer Premium plan for 30 workspaces.
- **Note**: Workspaces are collaborative environments with AI assistance from Gemini in Firebase.

### Integrations Requiring a Billing Account
- **Firebase App Hosting**:
  - Requires a Cloud Billing account.
  - **Pricing** (effective June 14, 2025):
    - **Uncached Bandwidth**: $0.20/GiB after 10 GiB/month free.
    - **Cached Bandwidth**: $0.15/GiB after 10 GiB/month free.
    - **Storage**: $0.10/GB after 5 GB free.
  - Upgrades your project to the **Blaze Plan** (pay-as-you-go) for usage beyond free quotas.[](https://firebase.google.com/pricing/)
- **Gemini API**:
  - Paid tier applies if a billing account is linked.
  - Charges based on [Gemini Developer API pricing](https://cloud.google.com/vertex-ai/pricing).
- **Other Google Cloud Services**:
  - Services like Cloud Run, Cloud Build, and Cloud Logging may incur costs. Use the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator).[](https://firebase.google.com/pricing/)

### Gemini in Firebase
- **No-Cost Access**: Free for non-Google Workspace users.
- **Google Workspace Users**: Require a [Gemini Code Assist subscription](https://firebase.google.com/docs/studio/pricing) to access AI features in the Firebase console.[](https://firebase.google.com/pricing/)
- **Features**: Code completion, generation, testing, and documentation.

### Blaze Plan
- **Automatic Upgrade**: Linking a billing account upgrades to the Blaze Plan.
- **No-Cost Quotas**:
  - **Cloud Firestore**: 1 GiB stored, 50K reads/day, 20K writes/day, 20K deletes/day.
  - **Cloud Functions**: 2M invocations/month, 400K GB-seconds, 200K CPU-seconds.
  - **Cloud Storage**: 5 GB stored, 1 GB/day downloaded (legacy buckets).
- **Paid Usage** (examples):
  - **Cloud Firestore**: $0.18/100K reads, $0.06/100K writes, $0.02/100K deletes.[](https://tekpon.com/software/firebase/pricing/)
  - **Cloud Functions**: $0.40/million invocations.
  - **Cloud Storage**: $0.026/GB stored, $0.12/GB downloaded.[](https://www.capterra.com/p/160941/Firebase/)
- **Monitoring**: Use the Firebase Console’s Usage and Billing dashboard and set budget alerts.[](https://support.google.com/firebase/answer/9628313?hl=en)

### Spark Plan
- **No-Cost Tier**: Ideal for prototyping, with free quotas (e.g., 10 GiB Realtime Database downloads/month) but caps usage.[](https://tekpon.com/software/firebase/pricing/)
- **Firebase Studio**: Supports three free workspaces without needing a billing account.

### Additional Notes
- **Preview Status**: No SLA or deprecation policy applies during preview. Pricing may change.[](https://firebase.google.com/docs/studio)
- **Generative AI Terms**: Governed by the [Generative AI Prohibited Use Policy](https://policies.google.com/terms/generative-ai) and [Gemini API Additional Terms](https://cloud.google.com/terms/gemini-api).[](https://firebase.google.com/docs/studio)
- **Cost Management**:
  - Use the [Blaze Plan Calculator](https://firebase.google.com/pricing#blaze-calculator).
  - Review quotas in the [Firebase Documentation](https://firebase.google.com/docs).[](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans)
  - Contact [Firebase Support](https://firebase.google.com/support) for quota adjustments.[](https://firebase.google.com/docs/test-lab/usage-quotas-pricing)

This pricing structure makes Firebase Studio accessible for beginners and scalable for advanced projects. For detailed costs, visit [firebase.google.com/pricing](https://firebase.google.com/pricing).
""")

# Firestore Integration: Save and Display Notes (Optional)
if db:
    st.subheader("Save Notes to Firestore")
    note = st.text_area("Add a note about Firebase Studio setup:")
    if st.button("Save Note"):
        if note:
            try:
                db.collection("setup_notes").add({"note": note, "timestamp": firestore.SERVER_TIMESTAMP})
                st.success("Note saved to Firestore!")
            except Exception as e:
                st.error(f"Failed to save note: {str(e)}")
        else:
            st.error("Please enter a note.")

    st.subheader("Saved Notes")
    try:
        notes = db.collection("setup_notes").order_by("timestamp", direction=firestore.Query.DESCENDING).stream()
        for doc in notes:
            data = doc.to_dict()
            st.write(f"- {data['note']} (Saved: {data['timestamp']})")
    except Exception as e:
        st.error(f"Failed to load notes: {str(e)}")
else:
    st.info("Note-saving feature is disabled due to missing Firebase credentials. Follow the instructions above to enable it.")

# Footer
st.markdown("""
---
*Last updated: April 17, 2025. Pricing and features subject to change. Check [firebase.google.com](https://firebase.google.com) for the latest information.*
""")
