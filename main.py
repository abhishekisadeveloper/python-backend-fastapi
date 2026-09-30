from fastapi import FastAPI

app = FastAPI()

ai_models: list[dict] = [
    {
        "id": 1,
        "name": "GPT-5.6",
        "company": "OpenAI",
        "features": ["reasoning", "coding", "multimodal"],
    },
    {
        "id": 2,
        "name": "Claude Opus",
        "company": "Anthropic",
        "features": ["reasoning", "coding", "long-context"],
    },
    {
        "id": 3,
        "name": "Gemini 3",
        "company": "Google",
        "features": ["multimodal", "reasoning", "search"],
    },
    {
        "id": 4,
        "name": "Llama 4",
        "company": "Meta",
        "features": ["open-source", "coding", "multimodal"],
    },
    {
        "id": 5,
        "name": "DeepSeek V3",
        "company": "DeepSeek",
        "features": ["reasoning", "coding", "math"],
    },
    {
        "id": 6,
        "name": "Qwen 3",
        "company": "Alibaba",
        "features": ["reasoning", "coding", "multilingual"],
    },
    {
        "id": 7,
        "name": "Mistral Large",
        "company": "Mistral AI",
        "features": ["coding", "reasoning", "multilingual"],
    },
    {
        "id": 8,
        "name": "Grok",
        "company": "xAI",
        "features": ["reasoning", "coding", "real-time information"],
    },
]


@app.get("/")
def home():
    return {"message": "hello ji kaise ho saare"}


@app.get("/posts")
def posts_list():
    return ai_models


@app.get('/api/posts/{ai_id}')
def modals(ai_id: int):
    for modal in ai_models:
        if modal['id'] == ai_id:  # modal.get('id') == ai_id also aplicable here.
            return modal
    return {'error': 'item not found :('}
