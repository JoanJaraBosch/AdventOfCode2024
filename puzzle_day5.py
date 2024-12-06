from collections import defaultdict, deque


def print_order():
    dictionary = {}
    result = 0
    with open("input/day5_part1.txt", 'r') as file:
        for line in file:
            seq = line.replace("\n", "").split("|")
            if seq[0] not in dictionary:
                dictionary[seq[0]] = []
            dictionary[seq[0]].append(seq[1])

    with open("input/day5_part2.txt", 'r') as file:
        for line in file:
            is_valid = True
            line = line.strip().split(",")  # Limpia la línea y separa por ","

            # Comprobar que el orden en la actualización cumple las reglas
            for x in dictionary:  # Por cada regla X en las claves del diccionario
                for y in dictionary[x]:  # Por cada Y asociado a X
                    if x in line and y in line:  # Solo si ambos están en la actualización
                        if line.index(x) > line.index(y):  # Si X no está antes que Y
                            is_valid = False  # La actualización no es válida
                            break
                if not is_valid:
                    break

            # Si la actualización es válida, calcular su página central
            if is_valid:
                middle_index = len(line) // 2  # Índice central
                result += int(line[middle_index])  # Sumar la página central al resultado

    return result


def print_order_and_fix():
    dictionary = defaultdict(list)
    incorrect_updates = []
    correct_sum = 0
    fixed_sum = 0

    # Leer las reglas de orden desde el archivo
    with open("input/day5_part1.txt", 'r') as file:
        for line in file:
            seq = line.strip().split("|")  # Limpia la línea y separa por "|"
            dictionary[seq[0]].append(seq[1])  # Relación X -> Y

    # Leer las actualizaciones y comprobar su validez
    with open("input/day5_part2.txt", 'r') as file:
        for line in file:
            is_valid = True
            update = line.strip().split(",")  # Limpia la línea y separa por ","

            # Comprobar que el orden en la actualización cumple las reglas
            for x in dictionary:  # Por cada regla X en las claves del diccionario
                for y in dictionary[x]:  # Por cada Y asociado a X
                    if x in update and y in update:  # Solo si ambos están en la actualización
                        if update.index(x) > update.index(y):  # Si X no está antes que Y
                            is_valid = False  # La actualización no es válida
                            break
                if not is_valid:
                    incorrect_updates.append(update)
                    break

    # Ordenar actualizaciones incorrectas
    def topological_sort(pages, rules):
        """Ordena las páginas en base a las reglas usando orden topológico."""
        in_degree = defaultdict(int)  # Contar dependencias entrantes
        graph = defaultdict(list)

        # Construir el grafo
        for x, dependencies in rules.items():
            for y in dependencies:
                graph[x].append(y)
                in_degree[y] += 1

        # Inicializar la cola con los nodos sin dependencias entrantes
        queue = deque([page for page in pages if in_degree[page] == 0])
        sorted_pages = []

        while queue:
            current = queue.popleft()
            sorted_pages.append(current)
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted_pages

    for update in incorrect_updates:
        # Filtrar las reglas relevantes para las páginas de esta actualización
        relevant_rules = {x: [y for y in ys if y in update] for x, ys in dictionary.items() if x in update}

        # Ordenar las páginas en base a las reglas relevantes
        ordered_update = topological_sort(update, relevant_rules)

        # Calcular la página central de la actualización ordenada
        middle_index = len(ordered_update) // 2
        fixed_sum += int(ordered_update[middle_index])

    return fixed_sum