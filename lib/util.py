__all__ = ['fancy_title', 'HAWAIIAN_NAMES', 'ALMA_BAND', 'ASCII_NAMES']

ASCII = ['alaihi', 'aweoweo', 'uu'] 
BANDS = ['3', '6', '7']
ABBR_BAND_NAMES = ['b3', 'b6', 'b7']
HAWAIIAN = ['‘Ala‘ihi', '‘Āweoweo', '‘Ū‘ū']

'''
b3     -> Ala'ihi
alaihi -> Ala'ihi
       ...
b7     -> U'u
uu     -> U'u
'''
HAWAIIAN_NAMES = {**dict(zip(ABBR_BAND_NAMES, HAWAIIAN)), **dict(zip(ASCII, HAWAIIAN))}
'''
3 -> Ala'ihi
  ...
7 -> U'u
'''
ALMA_BAND = {**dict(zip(ABBR_BAND_NAMES, BANDS)), **dict(zip(ASCII, BANDS))}
'''
b3     -> alaihi
       ...
b7     -> uu
'''
ASCII_NAMES = {**dict(zip(ABBR_BAND_NAMES, ASCII)), **dict(zip(BANDS, ASCII))}


def fancy_title(rx: str):
    if rx in ASCII or rx in ABBR_BAND_NAMES or rx in BANDS:
        return f'{HAWAIIAN_NAMES[rx]} (band {ALMA_BAND[rx]})'
