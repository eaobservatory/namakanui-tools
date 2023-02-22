#!/local/python3/bin/python3
"""
Trx or Power (hot, cold) as a function of IF
"""
from lib.parser import ifp
from lib.extras import fancy_title
from argparse import ArgumentParser
from itertools import product
from math import ceil
from os import remove
from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
from collections import defaultdict
import numpy as np


def y_label(ys: str):
    if ys == 'trx':
        return 'Trx (K)'
    elif ys in ['hot_']:
        return 'Hot Power (dB)'
    elif ys in ['cold', 'sky']:
        return 'Cold Power (dB)'
    elif ys in ['atten']:
        return 'Attenuation (byte counts)'

if __name__ == '__main__':

    parser = ArgumentParser(description=__doc__)
    parser = ifp(parser)

    args = parser.parse_args()
    path = args.data_file
    # Y = args.y
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

    RX = path.parent.parent.stem
    DATA_SET = f'{RX}_{path.stem.split("_")[-1]}'
    df = pd.read_csv(path, sep=sep, skiprows=head_size, skipfooter=foot_size, engine='python')

    ys = 'atten'
    Y = df.filter(regex=ys)
    Y['lo_ghz'] = df['#lo_ghz']
    # Y['if_ghz'] = df['if_ghz']
    Y['if_ghz'] = pd.DataFrame(df, columns=['if_ghz'])

    # df_out = df.filter(regex='if_ghz|lo_ghz|hot_|sky|trx')
    # df_out.to_csv(f'b7_trx_and_power_20230215.csv', index=False)
    # exit()

    los = defaultdict(dict)
    for lo in Y.lo_ghz.unique():
        los_ = Y[Y.lo_ghz == lo]
        los[lo]['0U'] = los_.filter(regex='0U|if_ghz')
        los[lo]['1U'] = los_.filter(regex='1U|if_ghz')
        los[lo]['0L'] = los_.filter(regex='0L|if_ghz')
        los[lo]['1L'] = los_.filter(regex='1L|if_ghz')

    p0U = [] 
    p1U = [] 
    p0L = [] 
    p1L = [] 

    for lo in los:
        cur = los[lo]
        # (lo - if, 1L)
        cur['1L']['x'] = lo - cur['1L'].if_ghz
        # (lo + if, 0U)
        cur['0U']['x'] = lo + cur['0U'].if_ghz
        # (lo + if, 1U)
        cur['1U']['x'] = lo + cur['1U'].if_ghz
        # (lo - if, 0L)
        cur['0L']['x'] = lo - cur['0L'].if_ghz

        p0U.append((cur['0U'].x, cur['0U'].filter(regex=f'{ys}').sum(axis=1) / 4))
        p1U.append((cur['1U'].x, cur['1U'].filter(regex=f'{ys}').sum(axis=1) / 4))
        p0L.append((cur['0U'].x, cur['0L'].filter(regex=f'{ys}').sum(axis=1) / 4))
        p1L.append((cur['1L'].x, cur['1L'].filter(regex=f'{ys}').sum(axis=1) / 4))

    # p0U = [a for b in p0U for a in b]
    # p1U = [a for b in p1U for a in b]
    # p0L = [a for b in p0L for a in b]
    # p1L = [a for b in p1L for a in b]

    color = {
            '0U': 'orange',
            '1U': 'blue',
            '0L': 'green',
            '1L': 'purple'
            }

    p = '1U'
    left_limit = 0
    right_limit = 0
    if p == '0U':
        left_limit = 290 
        right_limit = 375 
    elif p == '1U':
        left_limit = 290 
        right_limit = 380 
    elif p == '0L':
        left_limit = 290
        right_limit = 380 
    elif p == '1L':
        left_limit = 280
        right_limit = 370 

    for lo in range(left_limit, right_limit - 5, 5):
        plt.axvline(x=lo, c='grey', linestyle='--')

    flag = True
    label = None
    if p == '0U':
        for x, y in p0U:
            label = None
            if flag:
                label = '0U'
            flag = False
            plt.plot(x, y, c=color['0U'], label=label)
            plt.xticks(range(left_limit, right_limit, 10))
            # plt.scatter(x, y, s=2, c=color['0U'], label=label)
    elif p == '1U':
        for x, y in p1U:
            label = None
            if flag:
                label = '1U'
            flag = False
            plt.xticks(range(left_limit, right_limit, 10))
            plt.plot(x, y, c=color['1U'], label=label)
    elif p == '0L':
        for x, y in p0L:
            lable = None
            if flag:
                label = '0L'
            flag = False
            plt.xticks(range(left_limit, right_limit, 10))
            plt.plot(x, y, c=color['0L'], label=label)
    elif p == '1L':
        for x, y in p1L:
            label = None
            if flag:
                label = '1L'
            flag = False
            plt.xticks(range(left_limit, right_limit, 10))
            plt.plot(x, y, c=color['1L'], label=label)

    plt.title(f'{ys} {p}')
    plt.xlabel(f'LO (GHz) + IF (GHz)')
    plt.ylabel(y_label(ys))
    plt.legend()
    plt.savefig(f'{ys}_{p}.png', dpi=250)
    plt.clf()

    # if plot_dir is not there, create it
    if not plot_dir.exists():
        plot_dir.mkdir()

    for lo in los:
        for p in ['0U', '1U' , '0L', '1L']:
            df_cur = los[lo][p]
            cur = df_cur.filter(regex=ys)
            for col in cur.columns:
                dcm = df_cur.columns[0][7:]
                plt.plot(df_cur.if_ghz, df_cur[col], label=f'{col.split("_")[-1]}')
            plt.title(f'{ys.title()}, LO {lo} GHz, Polarization {p}')
            plt.xlabel('IF (GHz)')
            plt.ylabel(y_label(ys))
            # plt.xticks(np.arange(df_cur.x), labels=np.arange(4, 7.5, 0.1))
            plt.legend()
            plt.savefig(plot_dir / f'{ys}_{lo}_{p}.png')
            plt.clf()

    # x_min = int(df[xcol][0])
    # x_max = int(df[xcol][df[xcol].size - 1])


    # df_trx = df.filter(regex='^trx', axis=1)
    # if csv:
    #     df_trx.insert(0, 'lo_ghz', df[xcol], True)  # add lo_ghz column if emitting csv
    #     fname = f'trx_{DATA_SET}.csv'
    #     df_trx.to_csv(fname, index=False)
    #     print(fname)
    #     exit()

    """

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
        data_set = DATA_SET.split('_')[1]
        plt.title(f'Trx {fancy_title(RX)} {p}\n{data_set}')
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
        print(plot_name)

    # clean up the sub plots
    if clean_up:
        for plot in plots:
            if plot.exists():
                remove(plot)
        # if plot_dir is empty after, remove it too.
        if len(list(plot_dir.iterdir())) == 0:
            plot_dir.rmdir()
            """
