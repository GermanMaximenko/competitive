import itertools
"""
Различные формы декартового произведения
"""

phrases = {
    'one': ['Товарищи!',
            'C другой стороны',
            'Равным образом',
            'Не следует однако забывать',
            'Таким образом',
            'Повседневная практика показывает, что'],

    'two': ['реализация намеченных планов!',
            'рамки и место обучения кадров',
            'постоянный колличественный рост и сфера нашей активности'],

    'three': ['играет важную роль в формировании',
              'требует от нас анализа',
              'постоянный колличественный рост и сфера нашей активности'],

    'four': ['существенных финансовых и административных условий',
             'дальнейших направлений развития',
             'системы массового участия']
}

# --------------- first ---------------
# cartesian = []
# for el1 in phrases['one']:
#     for el2 in phrases['two']:
#         for el3 in phrases['three']:
#             for el4 in phrases['four']:
#                 cartesian.append([el1, el2, el3, el4])

# for el in cartesian:
#     print(*el)

# cartesian = []
# for el1 in phrases['one']:
#     for el2 in phrases['two']:
#         for el3 in phrases['three']:
#             for el4 in phrases['four']:
#                 cartesian.append({
#                     'one': el1,
#                     'two': el2,
#                     'three': el3,
#                     'four': el4,
#                 })
# for el in cartesian:
#     print(*el)

# --------------- second ---------------
# for el in itertools.product(*phrases.values()):
#     print(el)
#
# for el in itertools.product(*phrases.values()):
#     print(dict(zip(phrases.keys(), el)))

# somelists = [
#    [1, 2, 3],
#    ['a', 'b'],
#    [4, 5]
# ]
#
# print(*itertools.product(*somelists))