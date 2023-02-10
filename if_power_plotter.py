#!/local/python3/bin/python3
"""
IF Power Plotter
"""
from lib.parser import if_power
from lib.util import fancy_title, ASCII_NAMES
import pandas as pd
import matplotlib.pyplot as plt
from argparse import ArgumentParser


if __name__ == '__main__':

    parser = ArgumentParser(description=__doc__)
    parser = if_power(parser)

    args = parser.parse_args()
    path = args.data_file
    diff = args.diff
    csv = args.csv


    if diff:
        # do the difference
        data_set_a = '.'.join(path.stem.split('.')[1:])
        data_set_b = '.'.join(diff.stem.split('.')[1:])
        data_name = f'{data_set_b}->{data_set_a}'
        rx = path.stem.split('_')[0]
        fname = f'att_change_{ASCII_NAMES[rx]}_{data_name}'
        df = pd.read_csv(path, sep=' ', skipfooter=1, engine='python')
        df_diff = pd.read_csv(diff, sep=' ', skipfooter=1, engine='python')
        df_out = pd.DataFrame()
        df_out['lo_ghz'] = df['#lo_ghz']
        df_out['change'] = df.att - df_diff.att
        if csv:
            # difference CSV
            fname += '.csv'
            df_out.rename(inplace=True, columns={'lo_ghz': 'LO (GHz)', 'change': 'Attenuation Change (8bit counts)'})
            df_out.to_csv(fname, index=False)
            print(fname)
            exit()

        positive = df_out[df_out.change > 0]  # attenuation decreased
        negative = df_out[df_out.change < 0]  # attenuation decreased
        plt.scatter(positive.lo_ghz, positive.change, s=2, color='g')
        plt.scatter(negative.lo_ghz, negative.change, s=2, color='r')
        plt.axhline(color='black')
        plt.title(f'{fancy_title(rx)} New_Att - Old_Att\n{data_name}')
        plt.ylabel('Attenuation Change (8bit counts)')
        plt.xlabel('LO (GHz)')
        fname += '.png'
        plt.savefig(fname)
        print(fname)
        exit()

    else:
        # normal plotting
        lower, upper = (-2.5, -0.5)  # acceptable IF power range
        df = pd.read_csv(path, sep=',', engine='python')
        df = df.dropna()
        data_set = f'{path.stem}{path.suffix}'
        rx = path.parent.parent.stem
        title = f'IF Power {fancy_title(rx)}\n{data_set}'
        fname = f'if_power_{rx}_{data_set}' 

        if csv:
            fname += '.csv'
            df.to_csv(fname, index=False)
            print(fname)
            exit()

        U = df.if_power <= upper
        L = df.if_power >= lower
        good = df[L & U]
        U = df.if_power > upper
        L = df.if_power < lower
        bad = df[L | U]
        plt.scatter(good.lo_ghz, good.if_power, s=2, color='g')
        plt.scatter(bad.lo_ghz, bad.if_power, s=2, color='r')
        plt.axhline(lower, color='black', linestyle='--')
        plt.axhline(upper, color='black', linestyle='--')
        plt.xlabel('LO (GHz)')
        plt.ylabel('IF Power (V)')
        plt.title(title)
        fname += '.png'
        plt.savefig(fname)
        print(fname)
        exit()
