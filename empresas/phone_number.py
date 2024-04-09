import re


def padronize_phone(telefone):

    result = []

    remove_caracteres = re.sub(r'[^\w]|\s', '', telefone)

    busca_correto = re.search(r'^(55\d{2}\d{9})$', remove_caracteres)

    if busca_correto:
        result.append(busca_correto.group(1))

    busca_falta_9 = re.search(r'^(55)(\d{2})(\d{8})$', remove_caracteres)

    if busca_falta_9:
        result.append(f'{busca_falta_9.group(1)}{
                      busca_falta_9.group(2)}9{busca_falta_9.group(3)}')
    busca_falta_55 = re.search(r'^(?!55)(\d{11})$', remove_caracteres)

    if busca_falta_55:
        result.append(f'55{busca_falta_55.group(1)}')
    busca_falta_55_e_9 = re.search('^(\d{2})(\d{8})$', remove_caracteres)

    if busca_falta_55_e_9:
        result.append(f'55{busca_falta_55_e_9.group(1)}9{
                      busca_falta_55_e_9.group(2)}')

    return result[0] if result else None
