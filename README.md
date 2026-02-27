### LLM Learning

Youtube vedios and course completed: 

* Completed 7 vedios in this playlist
   - https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0 
   - Got an overview. 
* Completed Part 1 Part 2
   - Gone through OOP style of coding  
   - https://www.youtube.com/playlist?list=PL9jefoqM2f-Pz2WNOffLvKgXwPsEGaLQc 
* Completed Prompt Engineering Course: 
   - Completed basic concepts and methods in prompt engineering
   - https://skillmasterlab.com/prompt-engineering-course-free-foundations/ 

Currently I am in learning phase to shift towards LLM tasks. 

My study project is not yet completed. Have uploaded only few sections in this repository. 
What has been done in the project so far: 
* Select dataset and preprocess it. 
* Add it to MySQL database and define primary key, foreign key constraints via python script. 
* Create a metadata which stores schema and definition of the database which will be stored in vector database. 
<pre>
Embedding
   ↓
Vector DB (schema search)
   ↓
Relevant schema snippets
   ↓
LLM prompt
   
</pre>
For the study project using Olist Dataset. 
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


