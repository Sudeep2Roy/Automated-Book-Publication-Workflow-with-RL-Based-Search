 RL-Based Searching and Automated Book Publication Workflow

This project uses artificial intelligence (AI) and learning by reinforcement to automate the creation and distribution of book chapters.


Characteristics

- Web Scraping: Retrieves screen shots and the chapter materials from Wikisource.
- AI Writer & Reviewer: Spins and refines chapters using LLMs.
- Human-in-the-Loop: After examine, the last edit is saved.
-RL-Based Search: Q-Learning chooses the optimal version based on user queries such as "formal" or "vivid."
Version Control: ChromaDB is used for storing and retrieving all versions.
 How to Run
 Install requirements:
   pip install streamlit playwright chromadb google-generativeai
   playwright install
  
