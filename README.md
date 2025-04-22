# 🧠 Knowledge Graph Generator from Natural Language Text

![Uploading image.png…]()


## 📌 Project Overview

The **Knowledge Graph Generator** is a Natural Language Processing (NLP) application that extracts meaningful relationships from plain English text and visualizes them as a **knowledge graph**. It uses syntactic parsing to identify subject–verb–object triples and creates a graphical representation of this data for better understanding, insight generation, and knowledge discovery.

This project bridges NLP with graph databases by also allowing the **storage of extracted entities and relationships into a Neo4j graph database**, enabling large-scale querying and analysis.

---

## 🎯 Objective

To help users:
- Understand the semantic structure of natural language text.
- Visualize how entities relate through actions.
- Store and manage this relational data in a graph database for later querying or integration into larger knowledge systems.

---

## ✨ Key Features

- ✅ **Text Parsing** using `spaCy` to extract subject, verb, and object entities.
- 📊 **Graph Visualization** with NetworkX and Matplotlib, embedded in Streamlit.
- 🔗 **Neo4j Integration** for persistent graph storage.
- 🧠 **TF-IDF Filtering** to highlight and prioritize meaningful triples.
- 🖥️ **Interactive UI** built with Streamlit for ease of use.

---

## 🧰 Tech Stack

- **Python**
- **spaCy** – NLP processing
- **NetworkX & Matplotlib** – Graph construction and rendering
- **Streamlit** – Frontend UI
- **Neo4j** – Graph database
- **scikit-learn** – TF-IDF vectorization

---

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/knowledge-graph-generator.git
   cd knowledge-graph-generator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## 🗃️ Example Use Case

Paste in any paragraph from an article, report, or essay. The app will output:
- Extracted triples
- A visual knowledge graph
- (Optionally) store these in Neo4j for graph querying

---

## 🔮 Future Enhancements

- Coreference resolution (e.g., resolving pronouns like "he", "it")
- Support for multi-language input
- Integration with Hugging Face Transformers for deeper NLP insights
- Web deployment via Hugging Face Spaces or Dockerized container

---
