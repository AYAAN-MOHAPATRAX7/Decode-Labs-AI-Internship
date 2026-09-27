# 🤖 DecodeLabs Rule-Based AI Chatbot

## 📌 Project Overview

This project is a deterministic, rule-based AI chatbot developed as part of Project 1 of the DecodeLabs Artificial Intelligence Internship.

The chatbot uses predefined rules stored in a Python dictionary to identify user inputs and generate appropriate responses.

It demonstrates fundamental Artificial Intelligence concepts such as control flow, decision-making, input processing, and rule-based response generation.

---

## 🎯 Objective

The objective of this project is to build a simple chatbot that can:

- Handle greetings
- Answer predefined questions
- Process and sanitize user input
- Run continuously in a conversation loop
- Provide fallback responses for unknown inputs
- Exit the conversation using predefined commands

---

## ✨ Features

- Rule-based conversation
- Dictionary-based knowledge base
- 10+ predefined responses
- Input normalization using `lower()` and `strip()`
- Continuous conversation loop
- Empty input handling
- Multiple exit commands
- Fallback response for unknown questions
- Simple and user-friendly command-line interface

---

## 🛠️ Technologies Used

- Python
- Python Dictionaries
- Conditional Statements
- While Loop
- String Methods

---

## ⚙️ How It Works

The chatbot follows a simple workflow:

```text
User Input
    ↓
Input Sanitization
    ↓
Check Exit Command
    ↓
Search Knowledge Base
    ↓
Match Found?
   /     \
 Yes      No
  ↓        ↓
Response  Fallback
   \       /
    ↓     ↓
 Continue Conversation