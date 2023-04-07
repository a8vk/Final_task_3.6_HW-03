import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# Список нежелательных слов
BAD_WORDS = ['редиска', 'фуфло толкать', 'кардан', 'бельмондо', 'заёб', 'распиздяй', 'веблюди', 'гунявый', 'кака',
             'кончитта', 'вомитнул', 'вомиторий', 'кусороклиш', 'мохуяр', 'обсерватория', 'пулька', 'сиська',
             'трухлявый', 'туба', 'щайсе', 'невротъебательского', 'ахтунг', 'пиздатый', 'опездол ', 'пиздопротивный',
             'яйца',  'шлёпалово', 'черепа ', 'фуфломицин', 'хлесиво']


@register.filter(name='censor')
def censor(text):
    # Проход по списку нежелательных слов и замена букв на * со второй буквы
    for word in BAD_WORDS:
        censored_word = word[0] + '*'*(len(word)-1)
        regex = r'(?i)\b({})\b'.format(word)
        text = re.sub(regex, censored_word, text)
    return mark_safe(text)
