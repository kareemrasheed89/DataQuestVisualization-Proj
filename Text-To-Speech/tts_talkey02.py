# tts_talkey02.py

import talkey

tts = talkey.Talkey(
preferred_languages = ['en', 'fr', 'tr'],
    engine_preference=['espeak'],
espeak = {
    'defaults': {
        'words_per_minute': 160,
        'variant': 'f5',
    },
    'languages': {
        'en': {
            'voice': 'english-mb-en1',
            'words_per_minute': 150,
        },
    }
})

tts.say('Good morning')
