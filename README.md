# Medical-Chatbot-Llama2
End to end medical chatbot using Meta Llama2

## Steps to run the project 

Clone this repository:
```bash
https://github.com/arrshsh/Medical-Chatbot-Llama2.git
```

```bash
conda create -n mchatbot python=3.8 -y
```

```bash
conda activate mchatbot
```

```bash
pip install -r requirements.txt
```

Create a .env file in the root directory and add your Pinecone credentials as follows:
```bash
PINECONE_API_KEY="cejknjrbv"
PINECONE_API_ENV="eevkj"
```

Download the Llama 2 Model:
```
llama-2-7b-chat.ggmlv3.q4_0.bin
```

From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main