# tts_talkey04.py

import talkey
tts = talkey.Talkey(
preferred_languages = ['fr', 'en'],
    engine_preference=['espeak'],
espeak = {
    'options': {
        'enabled': True
    },
    'defaults': {
        'language':'fr',
        'words_per_minute': 180,
        'variant': 'f5',
    },
    'languages': {
        'fr': {
            'voice': 'french-mb-fr5',
            'words_per_minute': 150,
        },
    }
})
tts.say('Bonjour. Parlez vous Français?','fr')
