"""
    Simple openai api support
"""

import os
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)
from openai import OpenAI, APIConnectionError, RateLimitError, Timeout


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10),
    retry=retry_if_exception_type((APIConnectionError, RateLimitError, Timeout)),
)
def openai_completion(
    model, 
    user_prompt,
    system_prompt=None, 
    history=[],
    base_url=None,
    api_key=None,
    **kwargs,
):
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    
    if base_url:
        os.environ["OPENAI_BASE_URL"] = base_url

    openai = OpenAI()

    messages = []
    if system_prompt:
        messages.append({
            "role": "system",
            "content": system_prompt,
        })

    messages.extend(history)

    messages.append({
        "role": "user",
        "content": user_prompt,
    })

    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        **kwargs,
    )

    return response.choices[0].message.content