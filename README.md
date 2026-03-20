# 📝 LinkedIn Post Generator

An AI-powered tool that generates realistic LinkedIn posts using **few-shot learning**. It analyzes real LinkedIn posts to learn writing styles, then generates new posts matching a chosen **topic**, **length**, and **language** — powered by **Groq's Llama 3.3 70B** model and served through a **Streamlit** web interface.

---

## ✨ Features

- **Topic-Based Generation** — Select from auto-detected topics (Job Search, Mental Health, Motivation, etc.)
- **Length Control** — Choose Short (1–5 lines), Medium (6–10 lines), or Long (11–15 lines)
- **Multilingual Support** — Generate posts in English or Hinglish (Hindi + English)
- **Few-Shot Learning** — Uses real LinkedIn post examples to match authentic writing styles
- **Smart Tag Unification** — LLM-powered preprocessing merges similar tags into unified categories
- **Metadata Extraction** — Automatically extracts language, line count, and tags from raw posts

---

## 🏗️ Architecture

```
linkedin-post-generator/
│
├── main.py                  # Streamlit app entry point
├── post_generator.py        # Prompt construction & LLM invocation
├── llm_helper.py            # Groq LLM client setup (Llama 3.3 70B)
├── few_shot.py              # Few-shot example filtering & retrieval
├── preprocess.py            # Raw post preprocessing & tag unification
│
├── data/
│   ├── raw_posts.json       # Original LinkedIn posts with engagement data
│   └── processed_posts.json # Enriched posts with metadata (tags, language, line count)
│
├── .env                     # Environment variables (GROQ_API_KEY)
├── requirements.txt         # Python dependencies
├── pyproject.toml           # Project configuration
└── .python-version          # Python version specification (3.14)
```

---

## 🔧 How It Works

### 1. Preprocessing Pipeline (`preprocess.py`)

The preprocessing step enriches raw LinkedIn posts with LLM-extracted metadata:

- **Metadata Extraction** — For each raw post, the LLM extracts `line_count`, `language` (English/Hinglish), and up to 2 `tags`.
- **Tag Unification** — All extracted tags are sent to the LLM for deduplication and normalization (e.g., "Jobseekers" + "Job Hunting" → "Job Search").
- **Output** — Produces `data/processed_posts.json` with enriched, standardized posts.

### 2. Few-Shot Example Retrieval (`few_shot.py`)

The `fewShotPosts` class loads processed posts and provides:

- **Tag Discovery** — Extracts unique tags from all posts for the UI dropdown.
- **Filtered Retrieval** — Returns posts matching the selected length, language, and tag for use as few-shot examples.

### 3. Post Generation (`post_generator.py`)

Builds a structured prompt containing:

1. The selected **topic**, **length**, and **language**
2. Up to **2 matching examples** from the few-shot pool as writing style references
3. Sends the prompt to the LLM and returns the generated post

### 4. Web Interface (`main.py`)

A Streamlit app with three dropdown selectors (Topic, Length, Language) and a "Generate" button that triggers post generation and displays the result.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.14+
- A [Groq API Key](https://console.groq.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/linkedin-post-generator.git
   cd linkedin-post-generator
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   # source .venv/bin/activate   # macOS/Linux
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **(Optional) Preprocess raw posts**

   If you want to re-generate metadata from raw posts:
   ```bash
   python preprocess.py
   ```

5. **Run the app**
   ```bash
   streamlit run main.py
   ```

---

## 📦 Tech Stack

| Component       | Technology                          |
| --------------- | ----------------------------------- |
| **Frontend**    | Streamlit                           |
| **LLM**        | Llama 3.3 70B (via Groq)           |
| **Framework**   | LangChain                           |
| **Data**        | Pandas, JSON                        |
| **Environment** | python-dotenv                       |

---

## 📁 Data Format

### Raw Posts (`data/raw_posts.json`)
```json
{
  "text": "Post content...",
  "engagement": 347
}
```

### Processed Posts (`data/processed_posts.json`)
```json
{
  "text": "Post content...",
  "engagement": 347,
  "line_count": 7,
  "language": "English",
  "tags": ["Mental Health", "Job Search"]
}
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
