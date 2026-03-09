import os
from google import genai
from google.genai import types
import shutil

# 1. Configurações Iniciais
# Insira a sua chave de API aqui

fileLoc = "C:\\Users\\andre.maia\\Documents\\GitHub\\open-neuroscience.github.io\\"
fileName = "gemini_api.txt"
with open(fileLoc+fileName) as fid:
    API_KEY = fid.readline()


# Inicializa o cliente com o novo SDK
client = genai.Client(api_key=API_KEY)

# Define as pastas base
ORIGIN_DIR = fileLoc+"content\\en\\post"
DEST_DIR = fileLoc+"content\\pt\\post1"

# Configura as instruções do sistema e a temperatura usando o novo formato 'types'
system_instruction = """
Você é um tradutor de inglês para português do Brasil com especialização em neurociências.
Traduza o texto fornecido mantendo rigorosamente a estrutura Markdown.
Regras críticas:
1. NUNCA altere, traduza ou modifique os links (tudo entre colchetes e parênteses como [texto](url)).
2. Use terminologia correta de neurociência em português brasileiro.
"""

# Configuração de geração no novo padrão
config = types.GenerateContentConfig(
    temperature=0.2,
    system_instruction=system_instruction,
)

# 2. File Processing Logic
def process_repository():
    for root, dirs, files in os.walk(ORIGIN_DIR):
        for file in files:
            source_path = os.path.join(root, file)
            
            # Calculate destination path
            relative_path = os.path.relpath(root, ORIGIN_DIR)
            dest_folder = os.path.join(DEST_DIR, relative_path)
            dest_path = os.path.join(dest_folder, file)

            # Create the subfolder in the destination if it doesn't exist
            os.makedirs(dest_folder, exist_ok=True)

            # Route the file: translate if index.md, copy otherwise
            if file == "index.md":
                print(f"Translating: {source_path}")
                translate_file(source_path, dest_path)
            else:
                print(f"Copying: {source_path}")
                # copy2 preserves file metadata like creation/modification times
                shutil.copy2(source_path, dest_path) 

def translate_file(source, dest):
    with open(source, 'r', encoding='utf-8') as f:
        content = f.read()

    # Separate front matter (---) from the actual content
    parts = content.split('---')
    
    if len(parts) >= 3:
        front_matter = parts[1]
        markdown_body = '---'.join(parts[2:])
        
        try:
            # Generate the translation using the Gemini API
            response = client.models.generate_content(
                model='gemini-2.1-flash',
                contents=markdown_body,
                config=config
            )
            translated_body = response.text
            
            # Reassemble the file
            final_content = f"---{front_matter}---{translated_body}"
            
            # Save to the destination file
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(final_content)
            print(f"✓ Saved translated file: {dest}")
            
        except Exception as e:
            print(f"Error translating {source}: {e}")
    else:
        print(f"Warning: Unexpected format in {source}. Copying as is.")
        shutil.copy2(source, dest)

if __name__ == "__main__":
    if os.path.exists(ORIGIN_DIR):
        process_repository()
    else:
        print(f"Error: Origin folder '{ORIGIN_DIR}' not found.")