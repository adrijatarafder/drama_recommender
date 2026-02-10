from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
df = pd.read_csv("dramas.csv")

def compute_similarity(user_genres, selected_titles):
    results = []

    for _, row in df.iterrows():
        score = 0

        drama_genres = set(row["genres"].split(";"))
        drama_tropes = set(row["tropes"].split(";"))

        # Genre match
        genre_matches = len(user_genres & drama_genres)
        score += genre_matches * 10

        # Similar shows logic
        if row["title"] in selected_titles:
            score -= 100  # exclude already watched
        else:
            for title in selected_titles:
                base = df[df["title"] == title]
                if not base.empty:
                    base_tropes = set(base.iloc[0]["tropes"].split(";"))
                    score += len(base_tropes & drama_tropes) * 10

        similarity = min(100, max(0, score))

        if similarity > 0:
            results.append({
                "title": row["title"],
                "similarity": similarity,
                "synopsis": row["synopsis"],
                "tropes": row["tropes"]
            })

    results.sort(key=lambda x: x["similarity"], reverse=True)
    return results[:6]

@app.route("/")
def index():
    genres = sorted(set(
        g for row in df["genres"] for g in row.split(";")
    ))
    titles = df["title"].tolist()
    return render_template("index.html", genres=genres, titles=titles)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    user_genres = set(data["genres"])
    selected_titles = data["titles"]

    recommendations = compute_similarity(user_genres, selected_titles)
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
