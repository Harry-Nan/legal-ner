## These are the regular expressions used (based on the PDF above) to select relevant sentences.

For more details, [view the PDF here](https://github.com/Harry-Nan/legal-ner/blob/main/sentence%20selection/Legal%20action%20object%20patterns%20%5BDUTCH%5D.pdf).

### Legal objects:
```python
rechtsobjecten = ['vergunning', 'boete', 'dwangsom', 'ontheffing', 
                  #'besluit', 'aanvraag', # Not used
                  'subsidie', 'concessie', 'aanwijzing', 'bestuursdwang']
```
            
### Legal actions + regular expressions
```python
rechtshandelingen = {
    'verlenen': (
        r'\bverle(?:e)n(?!d)(?:en|t)?\d*\b'                         # Active: verleen, verlenen, verleent (≠ verleend)
        r'|\bverlenen\b'                                            # Explicit infinitive match
        r'|\bwordt\d*(?:\s+\w+)*?\s+verleend\b'                     # Passive: wordt … verleend
        r'|\bverleend\b(?:\s+\w+)*?\s+wordt\d*\b'                   # Passive: verleend … wordt
    ),
    'intrekken': (
        r'\bintrek(?!\w*ing)\w*\d*'                                 # intrekken, intrekt… (≠ intrekking)
        r'|\btrek(?:t)?\b(?:\s+\w+)*?\s+in\d*\b'                    # trekt … in87
        r'|\bin\d*(?:\s+\w+)*?\s+(?:trek(?:t)?\w*\d*)\b'            # in … trekt87
        r'|\bin\s+te\s+trekken\b'                                   # in te trekken
        r'|\bword(?:t)\d*(?:\s+\w+)*?\s+ingetrok'
    ),
    'wijzigen': (
        r'\bwijzig(?!\w*ing)\w*\d*'
        r'|\bword(?:t)?(?:\s+\w+)*?\s+gewijzigd\b'
    ),
    'opleggen': (
        r'\bopleg(?!\w*ing)\w*\d*'
        r'|\bleg(?:t)?\b(?:\s+\w+)*?\s+op\d*\b'
        r'|\bop\s+te\s+leggen\d*\b'
        r'|\bword(?:t)\d*(?:\s+\w+)*?\s+opgelegd\b' # wordt ... opgelegd
    ),
    'afwijzen': (
        r'\bafwijzen\d*\b'
        r'|\bwijs(?:t)\b(?:\s+\w+){*?\s+af\d*\b'
        r'|\baf\s+te\s+wijzen\d*\b'
    ),
    'goedkeuren': (
        r'\bgoedkeur(?!\w*ing)\w*\d*'                                # goedkeuren, goedkeurt…
        r'|\bkeur(?:t)?\b(?:\s+\w+)*?\s+goed\d*\b'                   # keurt … goed87
        r'|\bword(?:t)\d*(?:\s+\w+)*?\s+goed gekeurd\b'              # wordt … gekeurd
    ),
    'toekennen': (
        r'\btoeken(?!\w*ning)\w*\d*'                                 # toekennen, toekent (≠ toekenning)
        r'|\bken(?:t)?\b(?:\s+\w+)*?\s+toe\d*\b'                     # kent … toe87
        r'|\btoe\d*(?:\s+\w+)*?\s+ken(?:t)?\w*\d*\b'                 # toe … kent87
        r'|\btoe\s+te\s+kennen\b'                                    # toe te kennen
        r'|\bword(?:t)(?:\s+\w+)*?\stoegeken'
    ),
    'verstrekken': (
        r'\bverstrekken\b'
        r'|\bverstrek(?:t)?\b(?!e)'      
    ),
    'weigeren': (
        r'\bweiger(?!\w*ing)\w*\d*'                                   # weigeren, weigert, geweigerd, etc. (≠ weigering)
        r'|\bte\s+weigeren\b'                                         # te weigeren
    ),
    'verhogen': (
        r'\bverhoog(?!\w*ing)\w*\d*'                                  # verhogen, verhoogt, verhoogde, verhoogd (≠ verhoging)
        r'|\bverhogen\d*\b'
    ),
    'verlagen': (
        r'\bverla(?:a)g(?!\w*ing)\w*\d*'                              # verlagen, verlaagt, verlaagde, verlaagd (≠ verlaging)
        r'|\bverlagen\d*\b'
    ),
    'verlengen': (
        r'\bverleng(?!\w*ing)\w*\d*' 
        r'|\bverlengen\d*\b'
    ),
    'verkorten': (
        r'\bverkort(?!\w*ing)\w*\d*' 
        r'|\bverkorten\d*\b'
    ),
    'vervallen': (
        r'\bvervalt\d*\b' 
        r'|\bvervallen\d*\b'
    ),
    'beeindigen': (
        r'\bbeëindig(?:d)\d*\b' 
        r'|\bbeëindig(?:t)\d*\b'
        r'|\bbeëindigen\d*\b'
        r'|\bbeeindig(?:d)\d*\b' 
        r'|\bbeeindig(?:t)\d*\b'
        r'|\bbeeindigen\d*\b'
    ),
    'vaststellen': (
        r'\bvaststel(?!\w*ling)\w*\d*'                                  # vaststellen, vaststelt (≠ vaststelling)
        r'|\bstel(?:t)?\b(?:\s+\w+)*?\s+vast\d*\b'                      # stel(t) … vast
        r'|\bvast\d*(?:\s+\w+)*?\s+stel(?:t)?\w*\d*\b'                  # vast … stelt87
        r'|\bvast\s+te\s+kennen\b'                                      # vast te stellen
        r'|\bword(?:t)(?:\s+\w+)*?\svastgestel'                         # word(t) vastgestel(d)
    ),
    'afzien': (
        r'\bafzien\w*\d*'                                               # vaststellen, vaststelt (≠ vaststelling)
        r'|\bziet\b(?:\s+\w+)*?\s+af\d*\b'                              # stel(t) … vast
        r'|\bword(?:t)(?:\s+\w+)*?\safgezien'                           # word(t) vastgestel(d)
    ),
    'opheffen': (
        r'\bophef(?!\w*fing)\w*\d*'
        r'|\bhef(?:t)?\b(?:\s+\w+)*?\s+op\d*\b'
        r'|\bop\s+te\s+heffen\d*\b'
        r'|\bword(?:t)\d*(?:\s+\w+)*?\s+opgehev'                        # wordt ... opgehev
    ),
    'opschorten': (
        r'\schort\b(?:\s+\w+)*?\s+op\d*\b'
        r'|\bop\s+te\s+schorten\d*\b'
        r'|\bword(?:t)\d*(?:\s+\w+)*?\s+opgeschor'                      # wordt ... opgeschor
    ),
    'verminderen': (
        r'\bverminderd\d*\b' 
        r'|\bvermindert\d*\b'
        r'|\bverminderen\d*\b'
    ),
    'invorderen': (
        r'\bvorderd\b(?:\s+\w+)*?\s+in\d*\b'
        r'|\bvordert\b(?:\s+\w+)*?\s+in\d*\b'
        r'|\bin\s+te\s+vorderen\d*\b'
        r'|\bword(?:t)\d*(?:\s+\w+)*?\s+ingevorder' 
    ),
    'geven': (
        r'\bgeef(?:t)\b'
        r'|\bgeven\b'
        r'|\bword(?:t)\d*(?:\s+\w+)*?\s+gegeven'
    ),
    'bindend_verklaren': (
        r'\bverklaar(?:t)\b(?:\s+\w+)*?\s+bindend\d*\b'
        r'|\bverklaar(?:d)\b(?:\s+\w+)*?\s+bindend\d*\b'
        r'|\bword(?:t)\d*(?:\s+\w+)*?\s+bindend\b(?:\s+\w+)*?\s+verklaa'
    )
}
```

### Pair mapping: Legal Abject - Legal Action
``` python
object_action_map = {
    'vergunning':       ['verlenen', 'intrekken', 'wijzigen',
                         'verlengen', 'vervallen', 'beeindigen'],
    'boete'     :       ['opleggen', 'intrekken', 'wijzigen',
                         'vaststellen', 'afzien', 'verhogen',
                         'verlagen'],
    'dwangsom'  :       ['opleggen', 'intrekken', 'wijzigen',
                         'opheffen', 'verlengen', 'verkorten',
                         'verlagen', 'verhogen', 'opschorten',
                         'verminderen', 'invorderen'],
    'ontheffing':       ['verlenen', 'intrekken', 'wijzigen'],
 #   'besluit'   :       ['intrekken'],
 #   'aanvraag'  :       ['afwijzen', 'intrekken'],
    'subsidie'  :       ['verlenen', 'toekennen', 'verstrekken', 
                         'intrekken', 'wijzigen', 'weigeren',
                         'verhogen', 'verlagen', 'verstrekken'],
    'concessie' :       ['verlenen', 'intrekken'],
    'aanwijzing':       ['opleggen', 'intrekken', 'geven',
                         'opheffen', 'bindend_verklaren'],
    'bestuursdwang':    ['opleggen', 'intrekken', 'wijzigen',
                         'opheffen'],
    'goedkeuring':      ['verlenen', 'goedkeuren']
}
```

### Anti-sentence selection: If modal verbs are found in close proximity to legal object
``` python
modal_verbs = {'kunnen', 'zullen', 'mogen'}
``
