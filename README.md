# Chemistry API
## Introduction
This project aims to develop an advanced chatbot system by combining the power of Large Language Models (LLM) with the field of chemistry. The goal is to create a highly interactive and intelligent assistant that can answer complex queries, provide explanations, and assist in solving problems related to chemistry. By leveraging LLM's ability to process and generate human-like text, the chatbot will be able to understand scientific terminology, interpret chemical formulas, and engage in meaningful conversations about various topics such as organic chemistry, molecular biology, and chemical reactions. This fusion of cutting-edge AI technology with the sciences promises to deliver an innovative tool for both students and professionals in the field of chemistry.



## Architecture
<img src="./assets/RAG-dagram.png">

## Setup

Create your file ```.env```:
```
PORT= # PORT
VECTORDB_PORT= # vectordb port
VECTORDB_URL= # url vectordb:vectordb port
MODEL_NAME= #model name
LLM_API_KEY= #key llm
EMBEDDING_MODEL_NAME= #name embedding model
```
### Docker

To running project by docker:
```bash
git clone https://github.com/Luke-lab2002/MistralChemistryChatBot.git

cd MistralChemistryChatBot

docker-compose up
```

### Script
To running project by script:

#### Step 1: Install Qdrant vector database:

reference: https://qdrant.tech/documentation/guides/installation/

#### Step 2: Setup Projects
```bash
git clone https://github.com/Luke-lab2002/MistralChemistryChatBot.git

cd MistralChemistryChatBot

pip install -r requirements.txt

python app.py
```

## Add data to vector database
give your data to ```datasets``` in ```vectorDB``` and running ```add_datasets.py```
