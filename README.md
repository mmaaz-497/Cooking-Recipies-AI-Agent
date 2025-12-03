
# Recipes AI Agent

## Overview
An AI-powered agent built with OpenAI SDK that helps users discover, search, and manage recipes intelligently.

## Features
- 🤖 AI-powered recipe recommendations
- 🔍 Smart recipe search and filtering
- 📋 Recipe management and organization
- 💡 Ingredient-based suggestions
- 🎯 Dietary preference support

## Project Structure
```
recepies_ai_agent/
├── src/
│   ├── agent.py
│   ├── recipes.py
│   └── utils.py
├── requirements.txt
├── .env.example
└── README.md
```

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Add your OpenAI API key to .env
```

## Usage
```python
from src.agent import RecipeAgent

agent = RecipeAgent()
agent.run()
```

## Requirements
- Python 3.8+
- OpenAI API key
- See `requirements.txt` for dependencies