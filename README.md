# 🚀 AI Story Generator API

An AI-powered backend that generates **interactive, branching stories** using LLMs.
Built with **FastAPI**, **LangChain**, and **OpenRouter**, this project allows users to create dynamic stories where each choice leads to a new path.

---

## ✨ Features

* 🧠 AI-generated story content using LLMs
* 🌳 Tree-based story structure (nodes & branches)
* ⚡ FastAPI backend with async support
* 🗄️ PostgreSQL database with SQLAlchemy
* 🔌 LangChain integration for prompt handling
* 🔐 Environment-based configuration

---

## 🏗️ Tech Stack

* **Backend:** FastAPI
* **LLM Integration:** LangChain + OpenRouter
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Server:** Uvicorn

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=your_postgresql_url
OPENROUTER_API_KEY=your_api_key
```

---

## ▶️ Run the Server

```bash
uvicorn main:app --reload
```

App will run at:

```
http://127.0.0.1:8000
```

Interactive docs:

```
http://127.0.0.1:8000/docs
```

---

## 🔄 API Overview

### Create Story

* Generates a new story with a root node

### Expand Story Node

* Adds new branches based on user choice

### Get Full Story

* Returns complete story tree

---

## 🌳 Story Structure

Each story is stored as a tree:

* Root Node → Starting point
* Child Nodes → Choices
* Each node contains:

  * content
  * options
  * parent reference

---

## 🧪 Example Use Case

1. Start a story
2. Choose an option
3. AI generates next part
4. Continue branching infinitely

---

## 🚀 Future Improvements

* Frontend UI (React / Next.js)
* Story visualization graph
* User authentication
* Save & share stories
* Streaming responses

---

## 🤝 Contributing

Pull requests are welcome!
Feel free to open issues for suggestions or bugs.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Built with ❤️ by Darshna Raundal
