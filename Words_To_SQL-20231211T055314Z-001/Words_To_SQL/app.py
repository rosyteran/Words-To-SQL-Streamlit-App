import openai
import gradio as gr
import os


# OpenAi call
def gpt3(texts):
    openai.api_key = os.environ["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"]
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=texts,
        temperature=0,
        max_tokens=750,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=(";", "/*", "</code>")
    )
    x = response.choices[0].text

    return x


# Function to elicit sql response from model
def greet(prompt):
    txt = (f'''/*Prompt: {prompt}*/ \n —-SQL Code:\n''')
    sql = gpt3(txt)
    return sql


# Code to set up Gradio UI
iface = gr.Interface(greet, inputs=["text"], outputs="text", title="Natural Language to SQL",
                     description="Enter any prompt and get a SQL statement back! For better results, give it more context")
iface.launch()
