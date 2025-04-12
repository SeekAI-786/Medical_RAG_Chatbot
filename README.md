🏏 CT RAG MODEL — AI-Powered Cricket Fan Engagement using RAG

This project is a **prototype Retrieval-Augmented Generation (RAG) solution**, designed to **empower AI models to learn from new data without the need for hours of retraining**. It was built **before the Champions Trophy**, with the goal of allowing fans to **explore and learn about previous editions** of the tournament.

## Purpose

Traditional language models cannot adapt quickly to new information. This project solves that by integrating the **RAG (Retrieval-Augmented Generation)** approach, where:

1. **New documents are ingested (e.g., PDFs)** and broken into smaller chunks.
2. The chunks are stored using **ChromaDB**, a powerful vector store.
3. When a user asks a question, the system retrieves **relevant chunks only**, significantly reducing noise.
4. A **free LLM from Hugging Face** is used to generate responses based on the retrieved content.
5. The final response is then **cleaned and refined through a powerful LLM** for better user experience.

## How RAG Based Model Works

RAG combines the **retrieval abilities of search engines** with the **generative power of language models**. Instead of asking the model to remember everything, we:
- Store data in vector format (embeddings)
- Use semantic similarity to **retrieve only relevant info**
- Feed this to a model for more accurate and up-to-date answers

This ensures:
- **Faster response times**
- **No model retraining required**
- **Up-to-date answers from the latest documents**

## Features

- Use any **PDF** as your data source
- Automatically chunk the document into smaller text segments
- Save and manage vector data using **ChromaDB**
- Ask questions and get accurate answers using **free Hugging Face models**
- Final answers are **cleaned via an LLM** for clarity
- Easily define **custom save paths** for managing data
- Fully customizable — use your own models or datasets

## Model Used

- **Embedding Model**: `all-MiniLM-L6-v2` (Hugging Face)
- **LLM for response generation**: `mistralai/Mistral-7B-Instruct-v0.1` (Hugging Face, free version used)

You can swap these with other models from Hugging Face based on your requirements.


## How to Use

1. **Install Dependencies**

```bash
pip install langchain chromadb sentence-transformers huggingface_hub pypdf
```

2. **Add your PDF**

Place your file in the `./data` folder or any path you define.

3. **Run the notebook**

Open `CT_RAG_MODEL.ipynb` and run step by step:
- PDF loading and chunking
- Embedding and saving to ChromaDB
- Query and get answer
- Clean final response using LLM

4. **Ask questions like:**
> “Who was the player of the match in the final of CT 2017?”


## Project Context

This was built **ahead of the Champions Trophy** to offer fans a **historical insight into past editions** using AI-powered tools. It’s not designed for real-time use with the current tournament data but can easily be extended with new documents.


## Let's Collaborate!

I'm looking forward to collaborating with developers, cricket fans, or AI enthusiasts who want to:
- Improve this RAG prototype
- Add multilingual support
- Build a frontend for casual fans
- Deploy this as an interactive web app

Drop your suggestions or feel free to fork and play with the code!


## Disclaimer

This is a prototype. It was built quickly for experimentation and idea validation during the **Champions Trophy hype**. Contributions are welcome to make it production-ready.
