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
                    'name': 'lang_french',
                    'label': 'Search for VF',
                    'type': 'bool',
                    'default': 1,
                    'description': 'Search movies in true french audio',
                },
                {
                    'name': 'lang_quebec',
                    'label': 'Search for VFQ',
                    'type': 'bool',
                    'default': 1,
                    'description': 'Search movies in quebec french audio',
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
