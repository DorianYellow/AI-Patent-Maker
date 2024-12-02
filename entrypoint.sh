#!/bin/bash

# Ollama 서버 실행
ollama serve > ollama.log 2>&1 &

# 서버 준비 대기
sleep 5

# 모델 등록
ollama create Q5_K_M -f Modelfile

# Streamlit 앱 실행
exec streamlit run PatentMaker.py --server.port=8501 --server.address=0.0.0.0
