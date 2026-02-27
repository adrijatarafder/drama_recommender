🎬 Drama Recommender
A mood-based drama discovery web application that helps users find shows they will enjoy based on what they feel like watching right now, rather than long preference forms or generic popularity lists.
This project focuses on user-friendly interaction, explainable recommendations, and scalable system design, starting with a local prototype and evolving toward a globally accessible recommendation platform.


Inspiration:-
Many viewers struggle to decide what to watch because existing platforms rely heavily on:
Large databases with overwhelming filters
Generic popularity rankings
Static recommendation lists

This project explores a different approach:-
People often search by vibe, mood, or trope — not by database categories.
The Drama Recommender aims to provide quick, intuitive, and personalized suggestions using a guided discovery experience.

Features:-
Mood-Based Recommendation Flow
User selects the genre or mood they are interested in
Optionally chooses shows that feel similar
Receives ranked recommendations with similarity percentages
📊 Explainable Recommendations
Each result includes:
Match percentage
Short synopsis
Relevant tropes
Reasoning behind the recommendation
❄️ Cold-Start Friendly
Users can still receive recommendations even if they have never watched similar dramas before.
🖥️ Lightweight Local Prototype
Runs completely offline
Uses a curated dataset
No external APIs required

Tech Stack:-
Frontend
HTML
CSS
JavaScript
Backend
Python
Flask
Data
Local CSV dataset (curated metadata)


Project Structure
drama_recommender/
│
├── app.py          # Flask backend
├── dramas.csv      # Local dataset
├── index.html      # Frontend UI
└── styling.css     # UI styling

How It Works:-
The system uses a content-based recommendation approach:
User selections are converted into preference signals
Drama metadata (genres, tropes, tone) is compared
A weighted scoring system generates similarity percentages
Top matches are returned to the user

This approach prioritizes:
✅ Transparency
✅ Simplicity
✅ Scalability
▶️ Running Locally
1️⃣ Install dependencies
pip install flask pandas
(macOS users may need pip3 instead of pip)
2️⃣ Run the application
python app.py
or
python3 app.py
3️⃣ Open in browser
http://127.0.0.1:5000
📊 Dataset


The dataset used in this prototype is locally curated from publicly available information and manually annotated with:
Genres
Tropes
Tone
Pacing
Synopsis
This ensures ethical use and allows flexibility for experimentation.

Project Goals:-
Phase 1. Short-term:
Build an intuitive recommendation interface
Validate recommendation logic
Demonstrate explainable similarity scoring

Phase 2. Long-term:
Create a scalable, globally accessible drama discovery platform
🔮 Future Plans
This project is designed to evolve significantly beyond the prototype.
🧠 Machine Learning Integration
Content-based vector similarity models
Personalized user preference learning
Adaptive scoring based on feedback
👤 User Personalization
User accounts
Watch history tracking
Preference profiles
Feedback-driven recommendations
🌍 Global Deployment
Cloud hosting
API-based architecture
Performance optimization with caching
Multi-region accessibility
🔌 External Data Integration
If licensing allows:
Third-party drama metadata APIs
Real-time updates
Poster and rating synchronization
🎨 UX Improvements
Interactive UI components
Mood sliders and filters
Visual similarity indicators
Recommendation explanations with confidence metrics
📱 Mobile Expansion
Mobile-responsive design
Potential native app version
🧪 Research & Academic Scope
This project also explores concepts in:
Recommender systems
Human-centered AI
Cold-start problem handling
Explainable AI
User experience design for discovery systems
📌 Current Status
✅ Local prototype complete
✅ Recommendation logic implemented
🔄 Actively evolving toward advanced personalization

Author
Adrija
GitHub: https://github.com/adrija200524
