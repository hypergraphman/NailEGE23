g = {
    'А': 'БК',
    'Б': 'В',
    'В': 'Г',
    'Г': 'ДЕ',
    'Д': 'Е',
    'Е': 'ВЗЖ',
    'З': 'БВ',
    'Ж': 'БЗИМ',
    'И': 'АБК',
    'М': 'ИЛ',
    'Л': 'ИА',
    'К': '',
}


def f(s, p):
    if len(p) > 1 and p[0] == p[-1]:
        return 1
    if len(p) != len(set(p)):
        return 0
    return sum(f(x, p + x) for x in g[s])


print(f('И', 'И'))