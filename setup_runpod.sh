#!/bin/bash

cd ~

# 시스템 패키지 업데이트
apt-get update

# Vim 설치
apt-get install -y vim

# Hugging Face에서 모델 다운로드
curl -L -O https://huggingface.co/ys-s/pat_name_claim/resolve/main/unsloth.Q5_K_M.gguf

# Modelfile 생성
echo "FROM unsloth.Q5_K_M.gguf

TEMPLATE \"\"\"<bos><start_of_turn>user
Your role :
- 당신은 특허 문서 작성을 도와주는 patent attorney 입니다.
Instructions :
- 특허 문서는 간결하고 명확하게 작성해야 합니다.
- 청구항 작성시 발명의 구성 요소및 특징만을 논리적 순서로 나열해야 합니다.
- 청구항의 마지막 부분은 명사(noun)로 끝나야 합니다.
- 동일하거나 구조적으로 유사한 문장은 반복하지 말고 한 번만 명시해야 합니다.
Work :
- 아래의 발명에 관한 설명을 바탕으로 '발명의 명칭'과 '청구항'을 특허 문서의 형식으로 작성해주세요.:
{{.Prompt}}<end_of_turn>
<start_of_turn>model\"\"\"

PARAMETER temperature 0
PARAMETER num_predict 700
PARAMETER num_ctx 4096
PARAMETER repeat_penalty 1.11
PARAMETER stop <s>
PARAMETER stop </s>
" > Modelfile

# Ollama 모델 생성
ollama create model_v0 -f Modelfile
ollama list

# 레포지토리 디렉토리로 이동
cd AI-Patent-Maker

mkdir .streamlit
cd .streamlit
echo "[ server ]
enableCORS = false" > config.toml

# 가상 환경 생성 및 활성화
cd ..
VENV_NAME="pat"
python3 -m venv $VENV_NAME

# 필요한 패키지 설치
# source $VENV_NAME/bin/activate
# pip install streamlit ollama


# # Ollama 서버 실행 (백그라운드 실행)
# (ollama serve > ollama.log 2>&1) &
# ollama ps

# # Streamlit 애플리케이션 실행 (백그라운드 실행)
# (streamlit run app.py > app.log 2>&1) &
