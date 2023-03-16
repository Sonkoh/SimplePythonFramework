import re
import dotenv
import os

def get_env_value(key):
    return os.environ.get(key, '')
    
def render(file, data):
    with open(f'src/{file}.render.html', 'rb') as f:
        content = f.read().decode('utf-8')
        pattern = re.compile(r'\{%=[\s\S]*?%\}')
        for custom in pattern.findall(content):
            old = custom
            custom = re.sub(r"render\((.*?)\)", lambda match: str(data[match.group(1)]), custom)
            custom = re.sub(r"env\((.*?)\)", lambda match: {key: value for key, value in dotenv.dotenv_values().items()}[match.group(1)], custom)
            custom = re.sub(r'{%=(.*?)%}', r'\1', custom)
            content = content.replace(old, custom)
        return content
