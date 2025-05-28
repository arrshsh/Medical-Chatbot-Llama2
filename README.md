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
```bash
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```
and store it in model folder in the root folder 

Update your Pinecone credentials in the .env file 

Run the following command:
```bash 
python store_index.py
```

Finally, launch the Flask app:
```bash 
python app.py
```

Now, open the localhost on 5000 port 

Tech Stack used:
- Python 
- LangChain
- Flask
- Meta Llama2
- Pinecone