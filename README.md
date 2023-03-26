# ChatGPT-CLI

ChatGPT-CLI is a command-line interface (CLI) tool for ChatGPT, a large language model trained by OpenAI based on the GPT-3.5 architecture. The tool allows users to generate text responses based on user input, using the OpenAI API.

## Installation

To use ChatGPT-CLI, you will need to have Python 3.x installed on your system. You can then install the necessary dependencies using pip:

```pip install -r requirements.txt```


## Usage

To use ChatGPT-CLI, simply run the following command in your terminal:

```python chatgpt.py --input "Hello, how are you?"```


Replace the input text with your own question or prompt. You can also specify an input file using the `--file` option:

`python chatgpt.py --file input.txt`


The output will be printed to the terminal.

## Options

- `--input` or `-i`: Specify the input text to generate a response for.
- `--file` or `-f`: Specify the path to an input file to generate a response for.
- `--max-length` or `-m`: Specify the maximum length of the generated response (default is 50).
- `--temperature` or `-t`: Specify the "temperature" to use when generating the response (default is 0.8).
- `--top-p` or `-p`: Specify the "top p" value to use when generating the response (default is 0.9).


## Notes

- This tool requires an OpenAI API key to function. Please refer to the OpenAI API documentation for more information on obtaining a key.

- The quality and coherence of the generated responses may vary depending on the input text and the settings used. Adjusting the `max-length`, `temperature`, and `top-p` values can help improve the quality of the responses.

- This tool is for educational purposes only and should not be used for any commercial or business purposes.
