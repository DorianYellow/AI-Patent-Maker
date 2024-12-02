import ollama


def response_generator(prompt):
    """응답을 스트림 형태로 생성"""
    response = ollama.generate(model="Q5_K_M", prompt=prompt, stream=True)
    for chunk in response:
        if chunk["response"] == "\n":
            chunk["response"] = "\n\n"
        yield chunk["response"]
