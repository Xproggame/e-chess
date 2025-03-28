class Board:

    def __init__(self):

        self.position = {
            '11': 'tb1',
            '12': 'pb1',
            '13': '',
            '14': '',
            '15': '',
            '16': '',
            '17': 'pn1',
            '18': 'tn1',
            '21': 'cb1',
            '22': 'pb2',
            '23': '',
            '24': '',
            '25': '',
            '26': '',
            '27': 'pn2',
            '28': 'cn1',
            '31': 'fb1',
            '32': 'pb3',
            '33': '',
            '34': '',
            '35': '',
            '36': '',
            '37': 'pn3',
            '38': 'fn1',
            '41': 'rb',
            '42': 'pb4',
            '43': '',
            '44': '',
            '45': '',
            '46': '',
            '47': 'pn4',
            '48': 'rn',
            '51': 'Rb',
            '52': '',
            '53': '',
            '54': 'pb5',
            '55': '',
            '56': '',
            '57': 'pn5',
            '58': 'Rn',
            '61': 'fb2',
            '62': 'pb6',
            '63': '',
            '64': '',
            '65': '',
            '66': '',
            '67': 'pn6',
            '68': 'fn2',
            '71': 'cb2',
            '72': 'pb7',
            '73': '',
            '74': '',
            '75': '',
            '76': '',
            '77': 'pn7',
            '78': 'cn2',
            '81': 'tb2',
            '82': 'pb8',
            '83': '',
            '84': '',
            '85': '',
            '86': '',
            '87': 'pn8',
            '88': 'tn2'
        }
        self.case = {
            'tb1': [1, 1],
            'cb1': [2, 1],
            'fb1': [3, 1],
            'rb': [4, 1],
            'Rb': [5, 1],
            'fb2': [6, 1],
            'cb2': [7, 1],
            'tb2': [8, 1],
            'pb1': [1, 2],
            'pb2': [2, 2],
            'pb3': [3, 2],
            'pb4': [4, 2],
            'pb5': [5, 4],
            'pb6': [6, 2],
            'pb7': [7, 2],
            'pb8': [8, 2],
            'pn1': [1, 7],
            'pn2': [2, 7],
            'pn3': [3, 7],
            'pn4': [4, 7],
            'pn5': [5, 7],
            'pn6': [6, 7],
            'pn7': [7, 7],
            'pn8': [8, 7],
            'tn1': [1, 8],
            'cn1': [2, 8],
            'fn1': [3, 8],
            'rn': [4, 8],
            'Rn': [5, 8],
            'fn2': [6, 8],
            'cn2': [7, 8],
            'tn2': [8, 8]
        }