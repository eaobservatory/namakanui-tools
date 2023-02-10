#!/local/python3/bin/python3
"""
Trx Plotter
"""
from lib.parser import trx, fancy_title
from argparse import ArgumentParser
from itertools import product
from math import ceil
from os import remove
from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd


if __name__ == '__main__':

    parser = ArgumentParser(description=__doc__)
    parser = trx(parser)

    args = parser.parse_args()
    path = args.data_file
    xcol = args.x
    dpi = args.dpi
    clean_up = args.noCleanUp
    columns = args.column
    head_size = args.header
    foot_size = args.footer
    plot_dir = args.plots
    quiet = args.quiet
    y_max = args.ymax
    y_min = args.ymin
    y_inc = args.yinc
    x_inc = args.xinc
    sep = args.sep
    usb = args.usb
    lsb = args.lsb
    csv = args.csv
    padw = args.padw
    padh = args.padh

    RECEIVER = path.parent.parent.stem
    DATA_SET = f'{RECEIVER}_{path.stem.split("_")[-1]}'

    df = pd.read_csv(path, sep=sep, skiprows=head_size, skipfooter=foot_size, engine='python')
    x_min = int(df[xcol][0])
    x_max = int(df[xcol][df[xcol].size - 1])

    # if plot_dir is not there, create it
    if not plot_dir.exists():
        plot_dir.mkdir()

    df_trx = df.filter(regex='^trx', axis=1)
    if csv:
        df_trx.insert(0, 'lo_ghz', df[xcol], True)  # add lo_ghz column if emitting csv
        fname = f'trx_{DATA_SET}.csv'
        df_trx.to_csv(fname)
        print(f'produced: {fname}')
    upper = ['0U', '1U']
    lower = ['0L', '1L']
    polarizations = {}
    if usb:
        for b in upper:
            polarizations[b] = df_trx.filter(regex=b)
    if lsb:
        for b in lower:
            polarizations[b] = df_trx.filter(regex=b)

    columns = columns if columns <= len(df_trx.columns) else len(df_trx.columns)
    plots = []  # hold the names of the generate plots
    for p in polarizations:
        name = Path(f'{plot_dir}/trx_{DATA_SET}_{p}.png')
        plots.append(name)
        for i, col in enumerate(polarizations[p].columns):
            Y = df_trx[col]
            plt.plot(df[xcol], Y, label=col)
            plt.legend()
            plt.xlim((x_min, x_max))
            plt.xticks(range(x_min, x_max + 1, x_inc))
            plt.ylim((y_min, y_max))
            plt.yticks(range(y_min, y_max, y_inc))
        # plt.title(f'{HAWAIIAN_NAMES[RECEIVER]} ({ALMA_BAND[RECEIVER]}) {p}')
        plt.title(f'Trx {fancy_title(RECEIVER)} {p}')
        plt.ylabel('Trx (K)')
        plt.xlabel('LO (GHz)')
        plt.savefig(name, dpi=dpi)
        plt.clf()

    width, height = Image.open(plots[0]).size
    rows = ceil(len(plots) // columns)  # row is a function of columns

    collage = Image.new('RGB', (width * columns + padw, height * rows + padh), color='white') 
    for plot, (y, x) in zip(plots, product(range(rows), range(columns))):
        img = Image.open(plot)
        collage.paste(img, box=(x * width + padw // 2, y * height + padh // 2))

    plot_name = f'trx_{DATA_SET}.png'
    collage.save(plot_name)
    if not quiet:
        print(f'produced: {plot_name}')

    # clean up the sub plots
    if clean_up:
        for plot in plots:
            if plot.exists():
                remove(plot)
        # if plot_dir is empty after, remove it too.
        if len(list(plot_dir.iterdir())) == 0:
            plot_dir.rmdir()
