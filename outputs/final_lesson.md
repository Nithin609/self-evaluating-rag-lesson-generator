# Introduction to RAG

# Introduction to RAG (Retrieval‑Augmented Generation)

---

## 1. What is RAG?

RAG stands for **Retrieval‑Augmented Generation**.  
It is a way for an AI system to **look up information** from external sources **and then write an answer** using that information.

- **Retrieval** = finding useful pieces of text that already exist.  
- **Generation** = the AI (a language model) creates a response, using the retrieved pieces as help.

---

## 2. Why is RAG useful? What problem does it solve?

A plain language model only knows what it learned during its training.  
If the model has never seen a fact, it may guess or give a wrong answer.

RAG solves this by:

1. **Bringing in up‑to‑date facts** from documents, web pages, PDFs, etc.  
2. **Reducing hallucinations** – the model is less likely to make things up because it can copy real text.  
3. **Answering niche questions** that are not covered in the model’s original training.

---

## 3. How does RAG work? (Step‑by‑step)

1. **Collect documents** – a set of text files, articles, manuals, etc.  
2. **Split documents into chunks** – small pieces (a few sentences each) that are easier to search.  
3. **Create embeddings** – turn each chunk into a short list of numbers that capture its meaning.  
4. **Search (retrieval)** – when a user asks a question, the system turns the question into an embedding and finds the chunks whose embeddings are most similar.  
5. **Retrieve context** – the top‑matching chunks are passed to the language model.  
6. **Generate answer** – the language model reads the retrieved context and writes a response that combines its own knowledge with the new information.  

**Flow diagram in words**

```
Documents → Chunks → Embeddings → Search → Retrieved context → Language model → Answer
```

---

## 4. Everyday example with a small story

*Rita lives in Mumbai and loves cooking. She wants a recipe for “pav bhaji without peanuts” because her brother is allergic.*

1. Rita types the request into a chat app that uses RAG.  
2. The system looks through a collection of Indian recipe PDFs (the **documents**).  
3. It finds short pieces that mention “pav bhaji” and “no peanuts” (the **chunks**).  
4. Those pieces are turned into **embeddings** and the most relevant ones are **retrieved**.  
5. The language model reads those pieces and writes a complete, safe recipe for Rita.  

Rita gets a correct, allergy‑friendly recipe instantly.

---

## 5. Simple AI‑related example

A student asks: *“What is the capital of Bhutan?”*  

- The RAG system has a small database of world‑facts.  
- It retrieves the sentence “Thimphu is the capital of Bhutan.”  
- The language model then answers: **“The capital of Bhutan is Thimphu.”**  

Even if the base model did not remember the fact, the retrieval step supplies it.

---

## 6. Key technical terms (explained simply)

| Term | Simple meaning |
|------|----------------|
| **Document** | Any piece of text: an article, a PDF, a web page. |
| **Chunk** | A small part of a document, like a paragraph or a few sentences. |
| **Embedding** | A short list of numbers that represents the meaning of a chunk or a question. |
| **Search / Retrieval** | Finding the chunks whose embeddings are closest to the question’s embedding. |
| **Language model** | An AI that can write text, like ChatGPT. |
| **Generation** | The act of the language model creating a response. |
| **Hallucination** | When an AI makes up information that is not true. |

---

## 7. What RAG does **NOT** do / common misunderstanding

- **RAG does not change the language model’s internal knowledge**.  
  The model’s weights (its learned parameters) stay the same during retrieval.  
- It does **not** automatically retrain or update the model when new documents are added.  
- It does **not** guarantee perfect answers; the retrieved chunks must be accurate, and the model must use them correctly.

---

## 8. Short recap

- RAG = Retrieval‑Augmented Generation.  
- Retrieval finds relevant external text; generation writes the answer using that text.  
- The process: documents → chunks → embeddings → search → retrieved context → language model → answer.  
- It helps AI give up‑to‑date, factual answers without changing its own knowledge.  
- It does not modify the model’s weights or learn new facts on its own.

---

## 9. Check your understanding – three simple questions

| # | Question | Answer |
|---|----------|--------|
| 1 | What are the two main parts of RAG? | Retrieval (finding text) and Generation (writing an answer). |
| 2 | Does RAG change the language model’s internal weights when it retrieves information? | No, the model’s weights stay the same. |
| 3 | In the flow “Documents → Chunks → Embeddings → Search → Retrieved context → Language model → Answer”, what step comes right after *Embeddings*? | Search (retrieval) – the system looks for the most similar chunks. |

---