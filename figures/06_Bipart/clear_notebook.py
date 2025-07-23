import nbformat

def clear_outputs(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    for cell in notebook['cells']:
        if 'outputs' in cell:
            cell['outputs'] = []
        if 'execution_count' in cell:
            cell['execution_count'] = None

    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)

# Remplacez ici les chemins vers vos fichiers
clear_outputs('bord_expansion_julia_2024-11-18.ipynb', 'bord_expansion_julia_2024-11-24.ipynb')
