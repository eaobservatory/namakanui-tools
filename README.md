# namakanui-tools

Software tools used by the engineering groups to analyze the engineering data products from the Namakanui instrument.

- if_power_plotter.py:
    - plots the data files produced by if_power.py
    - data files usually found in /jac_logs/hetLogs/{RX}/if_power/
- trx_plotter.py:
    - plots the data files produced by trx_fast.py (and trx_sweep_b3.py)
    - data files usually found in /jac_logs/hetLogs/{RX}/trx/
- dcm_att_plotter.py:
    - plots the data files produced by dcm_att.py
    - data files usually found in /jac_logs/hetLogs/{RX}/att/

## if_power_plotter.py

Used to plot the data products of if_power.py

- create scatter plot
- create csv data file

TODO:

- Create difference plots if given a pair of attenuation tables
- Create difference csv file

### Usage

Plots are always created, a csv data file can optionally be created.

Make plot

```bash
$ ./if_power_plotter.py data_file
```

Emit CSV

```bash
$ ./if_power_plotter.py data_file --csv
```

## trx_plotter.py

Used to plot the data products of trx_fast.py (and trx_sweep_b3.py).

TODO:

- allow plotted columns to be increased selectively
- allow emitted csv columns to be paired selectively
- automatically compute header/footer:
    - remove parameter

### Usage

Plots are always created, a csv data file can optionally be created.

```bash
$ ./trx_plotter.py data_file
```

Emit CSV

```bash
$ ./trx_plotter.py data_file --csv
```

Change minimum Y value

```bash
$ ./trx_plotter.py data_file --ymin VAL
```

Change maximum Y value

```bash
$ ./trx_plotter.py data_file --ymax VAL
```

Change X increment value

```bash
$ ./trx_plotter.py data_file --xinc VAL

```
Change Y increment value

```bash
$ ./trx_plotter.py data_file --yinc VAL
```

Disable upper side band output

```bash
$ ./trx_plotter.py data_file --usb
```

Enable lower side band output

```bash
$ ./trx_plotter.py data_file --lsb
```

Define width padding

```bash
$ ./trx_plotter.py data_file --padw VAL
```

Define height padding

```bash
$ ./trx_plotter.py data_file --padh VAL
```

Define number of columns in collage output

```bash
$ ./trx_plotter.py data_file --column VAL
```

## dcm_att_plotter.py

Used to plot the data products of dcm_att.py.

TODO:

- allow plotted columns to be increased selectively
- allow emitted csv columns to be paired selectively
- automatically compute header/footer:
    - remove parameter

### Usage 

Plots are always created, a csv data file can optionally be created.

```bash
$ ./dcm_att_plotter.py data_file
```

Specify the column to use as X

```bash
$ ./dcm_att_plotter.py data_file --x VAL
```

Change minimum Y value

```bash
$ ./dcm_att.plotter.py data_file --ymin VAL
```

Change maximum Y value

```bash
$ ./dcm_att.plotter.py data_file --ymax VAL
```

Change X increment value

```bash
$ ./dcm_att.plotter.py data_file --xinc VAL

```
Change Y increment value

```bash
$ ./dcm_att.plotter.py data_file --yinc VAL
```

Define width padding

```bash
$ ./dcm_att_plotter.py data_file --padw VAL
```

Define height padding

```bash
$ ./dcm_att_plotter.py data_file --padh VAL
```
Define number of columns in collage output

```bash
$ ./dcm_att_plotter.py data_file --column VAL
```
