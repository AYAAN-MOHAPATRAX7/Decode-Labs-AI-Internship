# Project 3 — AI Recommendation Logic

## DecodeLabs Artificial Intelligence Internship

This project implements the **Tech Stack Recommender** described in the DecodeLabs Project 3 Industrial Training Kit.

The application takes three user skills/interests and matches them against career-role skill profiles using **TF-IDF** and **cosine similarity**. It then sorts the similarity scores and returns the **Top 3** career recommendations.

## How It Works

```text
User enters 3 skills
        ↓
Load raw_skills.csv
        ↓
TF-IDF vectorization
        ↓
Cosine similarity
        ↓
Score career roles
        ↓
Sort by similarity
        ↓
Top 3 recommendations
```

## Project Structure

```text
Project-3/
├── main.py
├── raw_skills.csv
├── requirement.txt
└── README.md
```

## Requirements

- Python 3.10+
- scikit-learn

## Installation

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependency:

```bash
pip install -r requirement.txt
```

## Run

```bash
python main.py
```

Example:

```text
Skill 1: Python
Skill 2: Cloud Computing
Skill 3: Automation
```

The program returns the three highest-scoring career paths with their cosine-similarity scores.

## Core Concepts

- Content-based recommendation
- User preference matching
- TF-IDF feature extraction
- Cosine similarity
- Ranking
- Top-N filtering
- Pattern matching

## Dataset

`raw_skills.csv` contains a small sample set of career roles and associated skills so the capstone is runnable. The career roles act as recommendation items.

## Learning Outcome

This project demonstrates how user preferences can be represented as vectors and compared with item profiles to produce ranked recommendations.

## Internship

**Artificial Intelligence Internship — DecodeLabs**

**Project 3: AI Recommendation Logic**

## Author

**Pihu Verma**

GitHub: https://github.com/Pihu-v17/Decode-Labs-AI-Internship
