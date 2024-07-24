import re
from bs4 import BeautifulSoup
from markdown import markdown

def clean_markdown_from_json(data, key=None):
    keys_to_clean = {"name", "title", "description", "guidance", "examples"}

    if isinstance(data, dict):
        return {k: clean_markdown_from_json(v, k) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_markdown_from_json(v, key) for v in data]
    elif isinstance(data, str) and key in keys_to_clean: 
        html = markdown(data)
        text = "".join(BeautifulSoup(html, features='html.parser').findAll(text=True))
        nl_clean = re.sub(r'(\r\n|\r|\n|\\n)', '', text)
        return nl_clean
    else:
        return data

def replace_new_lines_with_breaks(data, key=None):
    if isinstance(data, dict):
        return {k: replace_new_lines_with_breaks(v, k) for k, v in data.items()}
    elif isinstance(data, list):
        return [replace_new_lines_with_breaks(v, key) for v in data]
    elif isinstance(data, str): 
        return re.sub(r'(\r\n|\r|\n|\\n)', '<br>', data)
    else:
        return data