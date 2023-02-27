from transformers import pipeline, set_seed


def exemplo1():
    # Configura o gerador de texto do GPT-2
    generator = pipeline('text-generation', model='gpt2')

    # Define a semente para o gerador de texto
    set_seed(42)

    # Gera texto com o GPT-2
    text = generator('Hello, world!', max_length=50, num_return_sequences=1)

    # Imprime o texto gerado
    print(text[0]['generated_text'])


def exemplo2():
    # Configura o gerador de texto do GPT-2
    generator = pipeline('text-generation', model='gpt2')

    # Define a semente para o gerador de texto
    generator("Hello", max_length=30, num_return_sequences=1)

    # Gera texto com o GPT-2
    text = generator('Hello', max_length=30, num_return_sequences=1)[0][
        'generated_text']

    # Imprime o texto gerado
    print(text)
