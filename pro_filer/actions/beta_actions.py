"""Arquivo que estudantes devem editar"""
import os


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        # função os.path.split(path) divide o caminho (path) em duas partes e
        # retorna o tamanho/len da tupla contendo essas partes
        deepest_file = max(context["all_files"],
                           key=lambda path: len(os.path.split(path)))
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if not case_sensitive:
            # é necessário atribuir os valores ás variáveis
            file_name = file_name.lower()
            search_term = search_term.lower()

        if search_term in file_name:
            found_files.append(path)

    return found_files
