### LLM Learning

Currently I am in learning phase to shift towards LLM tasks. 

Currently the project is not yet completed. Have uploaded only few sections. 

For the below project using Olist Dataset. 
Expected Structure: 
<pre>
text_to_sql/
├── db/
│   └── mysql_client.py          # executes SQL only
│
├── vector_store/
│   ├── client.py                # vector DB init (Chroma / FAISS / Pinecone)
│   ├── ingest_schema.py         # run once: JSON → embeddings
│   └── retriever.py             # query vector DB at runtime
│
├── llm/
│   ├── prompt.py                # prompt templates
│   └── sql_generator.py         # LLM call (no DB logic here)
│
├── evaluator/
│   └── sql_guardrails.py        # validate SQL
│
├── metadata/
│   └── schema_metadata.json     # source of truth
│
├── main.py                      # orchestrates flow
└── api.py    
</pre>
