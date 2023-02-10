# namakanui-tools

Software tools used by the engineering groups to analyze the engineering data products from the Namakanui instrument.

- if_power_plotter.py:
    - plots the data files produced by if_power.py
    - plots the data files produced by att_table.py
    - data files usually found in:
        - /jac_logs/hetLogs/{Rx}/if_power/
        - /jac_sw/itsroot/src/namakanui_instrument/xml/ 
- trx_plotter.py:
    - plots the data files produced by trx_fast.py (and trx_sweep_b3.py)
    - data files usually found in /jac_logs/hetLogs/{Rx}/trx/
- dcm_att_plotter.py:
    - plots the data files produced by dcm_att.py
    - data files usually found in /jac_logs/hetLogs/{Rx}/att/

## if_power_plotter.py

Used to plot the data products of if_power.py and att_table.py.

- data files usually found in:
    - /jac_logs/hetLogs/{Rx}/if_power/
    - /jac_sw/itsroot/src/namakanui_instrument/xml/ 
- create scatter plot
- create csv data file
- create difference plot between a pair of attenuation tables
- create a difference csv data file between a pair of attenuation tables

<p align="center">
<img src=https://i.imgur.com/PSaAFmS.png alt="" width="500"/>
</p>
<p align = "center">Example of a difference plot</p>

<p align="center">
<img src=https://i.imgur.com/xQnBg6p.png alt="" width="500"/>
</p>
<p align = "center">Example of an IF power plot</p>

TODO:

- Add parameter to control x axis increment (plotting)
- Add quiet parameter

### Usage

Make a plot

```bash
$ ./if_power_plotter.py data_file
```

Make a CSV

```bash
$ ./if_power_plotter.py data_file --csv

```

Create difference plot of two attenuation tables

```bash
$ ./if_power_plotter.py new_att_table --diff old_att_table
```

Create difference csv data file of two attenuation tables

```bash
$ ./if_power_plotter.py new_att_table --diff old_att_table --csv
```

## trx_plotter.py

Used to plot the data products of trx_fast.py (and trx_sweep_b3.py).

- data files usually found in /jac_logs/hetLogs/{Rx}/trx/
- create scatter plot
- create csv data file

TODO:

- allow plotted columns to be increased selectively
- allow emitted csv columns to be paired selectively
- automatically compute header/footer:
    - remove parameter

### Usage

Make a plot

```bash
$ ./trx_plotter.py data_file
```

Make a CSV

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

- data files usually found in /jac_logs/hetLogs/{Rx}/att/
- create collage of plots
- create csv data file

TODO:

- allow plotted columns to be increased selectively
- allow emitted csv columns to be paired selectively
- automatically compute header/footer:
    - remove parameter

### Usage 

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
