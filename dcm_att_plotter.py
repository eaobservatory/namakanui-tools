#!/local/python3/bin/python3
"""
ACSIS DCM Attenuation Plotter
"""
from lib.parser import dcm_att
from lib.util import fancy_title
from argparse import ArgumentParser
from itertools import product
from math import ceil
from os import remove
from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd


def y_label_maker(col:str):
    label = col
    if 'att' in col:
        return 'Attenuation (?)'
    elif 'p' in col:
        return 'Power (V?)'
    return label

if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__)
    parser = dcm_att(parser)

    args = parser.parse_args()
    path = args.data_file
    xcol = args.x
    dpi = args.dpi
    clean_up = args.noCleanUp
    head_size = args.header
    foot_size = args.footer
    plot_dir = args.plots
    quiet = args.quiet
    y_max = args.ymax
    y_min = args.ymin
    y_inc = args.yinc
    x_inc = args.xinc
    sep = args.sep
    csv = args.csv
    padw = args.padw
    padh = args.padh

    RX = path.parent.parent.stem
    DATA_SET = f'{RX}_{path.stem.split("_")[-1]}'

    df = pd.read_csv(path, sep=sep, skiprows=head_size, skipfooter=foot_size, engine='python')
    x_min = int(df[xcol][0])
    x_max = int(df[xcol][df[xcol].size - 1])

    # if plot_dir is not there, create it
    if not plot_dir.exists():
        plot_dir.mkdir()

    if csv:
        fname = f'dcm_att_{RX}_{DATA_SET}.csv'
        df.to_csv(fname,index=False)
        print(f'produced: {fname}')
    upper = ['0U', '1U']
    lower = ['0L', '1L']
    polarizations = {}
    plots = []  # hold the names of the generate plots
    columns = set(df.columns) - set([xcol])
    for col in columns:
        name = Path(f'{plot_dir}/dcm_att_{RX}__{col}_{DATA_SET}.png')
        plots.append(name)
        Y = df[col]
        plt.scatter(df[xcol], Y, label=col)
        plt.legend()
        plt.xlim((x_min, x_max))
        plt.xticks(range(x_min, x_max + 1, x_inc))
        plt.ylim((y_min, y_max))
        plt.yticks(range(y_min, y_max, y_inc))
        plt.title(f'{col} {fancy_title(RX)}')
        plt.ylabel('Attenuation (?)')
        plt.ylabel(y_label_maker(col))
        plt.xlabel('LO (GHz)')
        plt.savefig(name, dpi=dpi)
        plt.clf()

    width, height = Image.open(plots[0]).size
    rows = ceil(len(plots) // args.column)  # row is a function of columns

    collage = Image.new('RGB', (width * args.column + padw, height * rows + padh), color='white') 
    for plot, (y, x) in zip(plots, product(range(rows), range(args.column))):
        img = Image.open(plot)
        collage.paste(img, box=(x * width + padw // 2, y * height + padh // 2))

    plot_name = f'dcm_att_{RX}_{DATA_SET}.png'
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

