# Project 3: AI Recommendation Logic
# DecodeLabs Artificial Intelligence Internship
# Capstone: Tech Stack Recommender
# Method: TF-IDF + Cosine Similarity

import csv
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_FILE = Path(__file__).parent / "raw_skills.csv"
TOP_N = 3


def load_items():
    roles, skills = [], []
    with DATA_FILE.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            role = row["role"].strip()
            skill_text = row["skills"].strip()
            if role and skill_text:
                roles.append(role)
                skills.append(skill_text)
    if not roles:
        raise ValueError("The dataset does not contain valid recommendation items.")
    return roles, skills


def recommend(user_skills, top_n=TOP_N):
    roles, item_skills = load_items()
    user_profile = " ".join(skill.strip() for skill in user_skills if skill.strip())
    if not user_profile:
        raise ValueError("At least one skill is required.")

    documents = item_skills + [user_profile]
    vectorizer = TfidfVectorizer(lowercase=True, stop_words="english")
    vectors = vectorizer.fit_transform(documents)

    item_vectors = vectors[:-1]
    user_vector = vectors[-1]
    scores = cosine_similarity(user_vector, item_vectors).flatten()

    ranked = sorted(zip(roles, scores), key=lambda item: item[1], reverse=True)
    return ranked[:top_n]


def get_user_skills():
    print("Enter 3 skills/interests.")
    print("Example: Python, Cloud Computing, Automation\n")
    skills = []
    while len(skills) < 3:
        value = input(f"Skill {len(skills) + 1}: ").strip()
        if value:
            skills.append(value)
        else:
            print("Please enter a skill.")
    return skills


def main():
    print("=" * 60)
    print("        DECODELABS - PROJECT 3")
    print("        TECH STACK RECOMMENDER")
    print("=" * 60)

    user_skills = get_user_skills()
    recommendations = recommend(user_skills)

    print("\nYour skills:")
    for skill in user_skills:
        print(f"- {skill}")

    print("\nTop 3 Recommended Career Paths")
    print("-" * 60)
    for index, (role, score) in enumerate(recommendations, start=1):
        print(f"{index}. {role}  |  Similarity: {score:.2f}")
    print("=" * 60)


if __name__ == "__main__":
    main()
