import openai
import click

openai.api_key = "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"

@click.command()
@click.option('--input', '-i', prompt='Enter some text', help='Input text for ChatGPT')
def chat(input):
    response = openai.Completion.create(
        engine="davinci",
        prompt=input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    click.echo(response.choices[0].text.strip())

if __name__ == '__main__':
    chat()
