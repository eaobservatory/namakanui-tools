#!/local/python3/bin/python3
"""
IF Power Plotter
"""
from lib.parser import if_power, fancy_title
import pandas as pd
import matplotlib.pyplot as plt
from argparse import ArgumentParser


if __name__ == '__main__':

    parser = ArgumentParser(description=__doc__)
    parser = if_power(parser)

    args = parser.parse_args()
    path = args.data_file
    # title = args.title
    csv = args.csv

    rx = path.parent.parent.stem

    df = pd.read_csv(path, sep=',', engine='python')
    if csv:
        csv_name = f'if_power_rx_{path.stem}.csv'
        df.to_csv(csv_name, index=False)
        print(f'produced: {csv_name}')

    plt.scatter(df.lo_ghz, df.if_power)
    plt.xlabel('LO (GHz)')
    plt.ylabel('IF Power (V)')
    name = f'if_power_{rx}_{path.stem}{path.suffix}.png'
    title = f'IF Power {fancy_title(rx)}'
    plt.title(title)
    plt.savefig(name)
    print(f'produced: {name}')
