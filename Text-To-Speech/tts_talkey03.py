# tts_talkey03.py

import talkey
tts = talkey.Talkey(
preferred_languages = ['tr', 'fr', 'en'],
    engine_preference=['espeak'],
espeak = {
    'options': {
        'enabled': True
    },
    'defaults': {
        'language':'tr',
        'words_per_minute': 160,
        'variant': 'f3',  # m1,m2,m3,f1,f2,f3,...
    },
})
tts.say('GünaydIn. Merhaba.','tr')
