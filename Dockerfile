# Python 베이스 이미지 사용
FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필수 패키지 설치 및 Ollama 다운로드
RUN apt-get update && apt-get install -y \
    curl \
    libssl-dev \
    libffi-dev \
    build-essential \
    && apt-get clean

# Ollama 설치
RUN curl -fsSL https://ollama.com/install.sh | sh

# 모델 다운로드 및 필요한 파일 복사
WORKDIR /models
RUN curl -L --retry 5 -o unsloth.Q5_K_M.gguf https://huggingface.co/ys-s/pat_name_claim/resolve/main/unsloth.Q5_K_M.gguf
COPY Modelfile /models/Modelfile

# Python 앱 환경 설정
WORKDIR /app
COPY requirements.txt requirements.txt
COPY . .

# Python 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 실행 스크립트 복사
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Entrypoint 설정
ENTRYPOINT ["/app/entrypoint.sh"]
