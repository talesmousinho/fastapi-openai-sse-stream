import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from sse_starlette.sse import ServerSentEvent, EventSourceResponse
from openai import OpenAI

load_dotenv()

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def stream_completion(request: Request, messages: list):
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        stream=True
    )
    for chunk in stream:
        # If client closes connection, stop sending events
        if await request.is_disconnected():
            break
        # Send the chunk to the client
        yield ServerSentEvent(chunk.model_dump_json())
        # Send [DONE] event if the chunk is the last one
        if chunk.choices[0].delta.content is None:
            yield ServerSentEvent('[DONE]')

@app.get('/')
def message_stream(request: Request):
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say this is a test."}
    ]
    return EventSourceResponse(stream_completion(request, messages), media_type="text/event-stream")