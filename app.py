# app.py
import streamlit as st
import spacy
import subprocess
from neo4j import GraphDatabase
import matplotlib.pyplot as plt
import networkx as nx

# === Ensure spaCy model is installed ===
def install_spacy_model():
    try:
        spacy.load("en_core_web_sm")
    except OSError:
        subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
install_spacy_model()

# Load the model after ensuring it's installed
nlp = spacy.load("en_core_web_sm")

# Neo4j credentials
uri = "neo4j+s://ff701b1c.databases.neo4j.io"
username = "neo4j"
password = "BfZM7YRKpFz1b_V7acAmOtaSQHPU9xK03rJlfPep88g"  

# Connect to Neo4j
driver = GraphDatabase.driver(uri, auth=(username, password))

# Triple extraction function
def extract_triples(text):
    doc = nlp(text)
    triples = []
    for sent in doc.sents:
        subjects = [tok for tok in sent if "subj" in tok.dep_]
        verbs = [tok for tok in sent if tok.pos_ == "VERB"]
        objects = [tok for tok in sent if "obj" in tok.dep_]
        for subj in subjects:
            for verb in verbs:
                for obj in objects:
                    triples.append((subj.text, verb.lemma_, obj.text))
    return triples

# Visualization function
def show_graph(triples):
    G = nx.DiGraph()
    for s, p, o in triples:
        G.add_node(s)
        G.add_node(o)
        G.add_edge(s, o, label=p)
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u,v):d['label'] for u,v,d in G.edges(data=True)})
    st.pyplot(plt)

# === Streamlit UI ===
st.title("🧠 Knowledge Graph Generator")

text_input = st.text_area("Paste your text here", height=200)

if st.button("Generate Graph"):
    if text_input:
        triples = extract_triples(text_input)
        st.write("### Extracted Triples")
        for t in triples:
            st.write("🔗", t)
        show_graph(triples)
    else:
        st.warning("Please enter some text.")
