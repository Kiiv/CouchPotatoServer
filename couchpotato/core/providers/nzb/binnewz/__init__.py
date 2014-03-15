from .main import BinNewz

def start():
    return BinNewz()

config = [{
    'name': 'binnewz',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'nzb_providers',
            'name': 'binnewz',
            'description': 'Free provider, lots of french nzbs. See <a href="http://www.binnews.in/">binnewz</a>',
            'wizard': True,
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'lang',
                    'label': 'Language',
                    'default': 'VF,VFQ',
                    'description': 'Choose to search only VF, VFQ or both.',
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 0,
                    'description': 'Starting score for each release found via this provider.',
                }
            ],
        },
    ],
}]
