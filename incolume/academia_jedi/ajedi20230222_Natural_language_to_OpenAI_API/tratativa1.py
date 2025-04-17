"""Module."""

import contextlib
import os
import sys

from icecream import ic
from incolume.academia_jedi import logger

if not ((3, 8) < sys.version_info < (3, 13)):
    with contextlib.suppress(SystemExit):
        sys.exit(
            'This implementation requires `openai module` with python equal'
            ' or greater than 3.8 and less than 3.13',
        )
else:
    import openai


def run():
    """Run it."""
    openai.api_key = os.getenv('ACADEMIA_JEDI_OPENAI_API_KEY')

    response = openai.Completion.create(
        model='code-davinci-002',
        prompt='"""\nUtil exposes the following:\n'
        'util.openai() -> authenticates & returns the openai module,'
        ' which has the following functions:\nopenai.Completion.create(\n'
        '    prompt="<my prompt>", # The prompt to start completing from\n'
        '    max_tokens=123, # The max number of tokens to generate\n'
        '    temperature=1.0 # A measure of randomness\n'
        '    echo=True, # Whether to return the prompt in addition'
        ' to the generated completion\n)\n"""\nimport util\n"""\n'
        'Create an OpenAI completion starting from the prompt'
        ' "Once upon an AI", no more than 5 tokens.'
        ' Does not include the prompt.\n"""\n',
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=['"""'],
    )
    logger.info(ic(response))
    return response
