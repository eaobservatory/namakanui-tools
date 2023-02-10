__all__ = ['fancy_title']

RX_NAMES = ['alaihi', 'aweoweo', 'uu'] 
HAWAIIAN_NAMES = dict(zip(RX_NAMES, ['‘Ala‘ihi', '‘Āweoweo', '‘Ū‘ū']))
# HAWAIIAN_NAMES = {'alaihi': '‘Ala‘ihi', 'aweoweo': '‘Āweoweo', 'uu': '‘Ū‘ū'}
ALMA_BAND = dict(zip(RX_NAMES, ['3', '6', '7']))
# ALMA_BAND = {'alaihi': 'band 3', 'aweoweo': 'band 6', 'uu': 'band 7'}


def fancy_title(rx: str):
    if rx in RX_NAMES:
        return f'{HAWAIIAN_NAMES[rx]} (band {ALMA_BAND[rx]})'
