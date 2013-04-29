SIGNS = ['Козирог', 'Водолей', 'Риби', 'Овен', 'Телец', 'Близнаци',
         'Рак', 'Лъв', 'Дева', 'Везни', 'Скорпион', 'Стрелец', 'Козирог']
DATES = [19, 18, 20, 20, 20, 20, 21, 22, 22, 22, 21, 21]


def what_is_my_sign(day, month):
    if day <= DATES[month - 1]:
        return SIGNS[month - 1]
    else:
        return SIGNS[month]
