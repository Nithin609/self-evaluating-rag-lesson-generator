from groq import (
    Groq,
    APIError,
    APIConnectionError,
    AuthenticationError,
    RateLimitError
)

from config import GROQ_API_KEY, MODEL_NAME


# Validate API key
if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. Check your .env file."
    )

client = Groq(api_key=GROQ_API_KEY)


def ask_groq(messages, temperature=0.3, json_mode=False):

    options = {}

    if json_mode:
        options["response_format"] = {
            "type": "json_object"
        }

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=temperature,
            timeout=30,
            **options
        )

        if not response.choices:
            raise RuntimeError(
                "Groq API returned an empty response."
            )

        content = response.choices[0].message.content

        if not content:
            raise RuntimeError(
                "Groq API returned empty content."
            )

        return content

    except AuthenticationError as e:
        raise RuntimeError(
            "Invalid Groq API key. Check your .env file."
        ) from e

    except RateLimitError as e:
        raise RuntimeError(
            "Groq API rate limit or quota exceeded. "
            "Please try again later."
        ) from e

    except APIConnectionError as e:
        raise RuntimeError(
            "Unable to connect to Groq. Check your internet connection."
        ) from e

    except APIError as e:
        raise RuntimeError(
            f"Groq API error: {e}"
        ) from e  
        