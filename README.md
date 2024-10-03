# 💡 AI Patent Maker !

AI Patent Maker is an LLM-based service that assists with the complex and challenging task of drafting patent documents. 

Simply write down your idea, and AI Patent Maker will help you bring it to life with detailed specifications.


<p align="center">
  <img src="https://github.com/user-attachments/assets/240e3985-02d0-41b5-94a1-ccbd39aa14ae" width="777px" alt="GIF description"/>
</p>


## Introduction
- The process of drafting patent documents can be overwhelming and time-consuming.
- `AI Patent Maker` simplifies this by allowing users to input their ideas in natural language.
- The service then utilizes a large language model (LLM) to automatically generate patent claims and invention names, helping users create well-structured patent documents with ease.
- `AI Patent Maker` service is being operated temporaily at the following address : https://o9ebd0ewxw0ehv-8501.proxy.runpod.net/



## Features
- Automatic Patent Claim Generation: Automatically generates patent claims based on your idea and invention description.
- Invention Name Generation: Provides a suitable invention name that reflects the technical features of your idea.
- Lightweight and Efficient: `AI Patent Maker` is based on the fine-tuned `Gemma2-2B-it model`, ensuring a lightweight and highly efficient performance without sacrificing the quality of the output. This makes the service fast and responsive even in resource-limited environments.

## Guide
1. install Ollama
- Visit Ollama's official website and follow the instructions to install Ollama on your machine.
2. Download the Model from Hugging Face (You can use either of the following two links)
- https://huggingface.co/ys-s/pat_name_claim
- https://huggingface.co/limecoding/gemma2-2b-it-finetuned-patent
- Make sure to download the model in GGUF format
3. Create the Modelfile
- Create a file named Modelfile and specify the path to the downloaded GGUF model in the FROM directive.
- Here is an example template:
```
TEMPLATE """<bos><start_of_turn>user
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
<start_of_turn>model"""

PARAMETER temperature 0
PARAMETER num_predict 700
PARAMETER num_ctx 4096
PARAMETER repeat_penalty 1.11
PARAMETER stop <s>
PARAMETER stop </s>
```
4. Register the Model with Ollama
- Use the following command to register the model with Ollama:
- ollama create [model name you wanted] -f Modelfile
5. Create a Python Virtual Environment
6. Activate the Virtual Environment and Install Dependencies : requirements
7. Update PatentMaker.py with the Registered Model Name
- response = ollama.generate(model='your_registered_model_name', prompt=prompt, stream=True)
8. Run the PatentMaker.py Script
- streamlit run PatentMaker.py

## Reference
1. Dataset Source
- AI Hub : https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=90
- Kipris : http://www.kipris.or.kr/khome/main.jsp
2. Inventions featured in this project
- The invention cited in the example is based on the patent invention: reg_no 1020240121955
- Two inventions cited as examples in the web service : reg_no 1020120000016, 1020220057166

## License
This project is licensed under the [Apache License 2.0](LICENSE).
