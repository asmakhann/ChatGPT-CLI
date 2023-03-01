import os
import openai
import click

openai.api_key = "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"


@click.command()
@click.option('--input', '-i', prompt='Enter some text', help='Input text for ChatGPT')
def chat(input):
    response = openai.Completion.create(
        engine="davinci",
        prompt=input,
        max_tokens=150000,
        n=1,
        stop=None,
        temperature=0.1,
    )

    click.echo(response.choices[0].text.strip())

if __name__ == '__main__':
    chat()
