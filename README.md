---
title: Rag Chatbot Pocky
emoji: 🚀
colorFrom: red
colorTo: red
sdk: docker
app_port: 8501
tags:
- streamlit
pinned: false
short_description: Chatbot for Q/A from docs using RAG, Multi agents
license: mit
---

# Welcome to Streamlit!

Edit `/src/streamlit_app.py` to customize this app to your heart's desire. :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
# Pocky_Chatbot
Chatbot for Q/A from docs using RAG, Multi agents

1) First create a groq acccount, get PAT
2) Create hugging face account and get PAT
3) Create a git repo and pull the code and update it and push to github
4)Push to hugging face using - git push space main
Linked huggingface and github code using :
git remote set-url space https://hugging face id:hugging_face_token@huggingface.co/spaces/spaceName

Merge the file contents if any merge issues occur

then run git push space main 

sequence while setting up for first time,
1. git clone repo_https/ssh link
2. get remote add space https://hfid:hf token@huggingface.co/spaces/hfid/spacename
3. git config pull.rebase false #pull hf files to avoid conflict
4. git pull space main --allow-unrelated-histories #pull hf files to avoid conflict
5. git add . # if readme conflicts occur merge the contents in vscode
6. git commit -m "message"  

After set up is done, sequence for everyday routine,
1. git add .
2. git commit -m "msg"
3. git push origin main
4. git push space main



What i did 
- python -m venv.venv
- .\.venv\Scripts\activate or  .\.venv\Scripts\Activate.ps1 (recommended)
- created project structure for pdf, docx, txt in mind (embeddings, chubking, pipeline etc fokders in src)
- pip install -r requirements.txt 
- Added loader, document_extractor, text_chunker, test_text_chunker
- pytest -q -s tests/unit/test_text_chunker.py
- 

