"""Module."""

# ruff: noqa: T201

from config import settings
from openai import OpenAI


def run_agent():
    """Run the agent."""
    client = OpenAI(
        # This is the default and can be omitted
        api_key=settings.OPENAI_API_KEY,
    )

    response = client.responses.create(
        model='gpt-4o',
        instructions='You are a coding assistant that talks like a pirate.',
        input='How do I check if a Python object is an instance of a class?',
    )

    print(response.output_text)


if __name__ == '__main__':
    run_agent()
