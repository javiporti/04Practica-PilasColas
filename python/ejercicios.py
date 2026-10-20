from collections import deque



def equilibrados(texto: str) -> bool:
    parejas = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }

    pila = deque()
    for c in texto:
        if c in "([{":
            pila.append(c)         #es igual que la cola empiece por la izq que por la drch
        elif c in ")]}":
            if not pila or pila.pop() != parejas[c]:
                return False
    return not pila

# ([]) -> [ , (,      ]

def procesar_turnos(ordenes: list[tuple[str, str]]) -> list[str]:
    cola = deque()
    for tupla in ordenes:
        for orden, persona in tupla:
            if orden == "atiende":
                cola.popleft()
            elif orden == "siguiente":
                cola.append(cola[0] if len(cola) != 0 else: "VACIA")

            elif orden == "llega":
                cola.append(persona)
            else:
                raise ValueError("orden desconocida")

            #y si esta vacia??
    return cola
def probar_ejercicios() -> None:
    casos_parentesis = [
        ('', True),
        ('texto sin símbolos', True),
        ('a*(b+[c])', True),
        ('{[()]}', True),
        ('([)]', False),
        ('((', False),
        (']', False),
        ('(]', False),
    ]
    for texto, esperado in casos_parentesis:
        obtenido = equilibrados(texto)
        assert obtenido == esperado, (
            f'equilibrados({texto!r}): esperado {esperado}, obtenido {obtenido}'
        )

    casos_turnos = [
        ([], []),
        ([('siguiente', ''), ('atiende', '')], ['VACIA', 'VACIA']),
        ([('llega', 'Ana'), ('llega', 'Luis'), ('siguiente', ''),
          ('atiende', ''), ('atiende', ''), ('atiende', '')],
         ['Ana', 'Ana', 'Luis', 'VACIA']),
        ([('llega', 'Ana'), ('llega', 'Luis'), ('siguiente', ''),
          ('llega', 'Eva'), ('atiende', ''), ('siguiente', ''),
          ('atiende', ''), ('llega', 'Paco'), ('atiende', ''),
          ('atiende', ''), ('atiende', '')],
         ['Ana', 'Ana', 'Luis', 'Luis', 'Eva', 'Paco', 'VACIA']),
    ]
    for ordenes, esperado in casos_turnos:
        obtenido = procesar_turnos(ordenes)
        assert obtenido == esperado, (
            f'procesar_turnos({ordenes!r}): esperado {esperado}, obtenido {obtenido}'
        )
    print('12 casos superados')


if __name__ == '__main__':
    probar_ejercicios()
