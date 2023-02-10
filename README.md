# namakanui-tools

Software tools used by the engineering groups to analyze the engineering data products from the Namakanui instrument.

Used with:

- dcm_att.py
- trx_fast.py:
    - trx_sweep_b3.py (for band 3 [alaihi] currently)
- if_power.py

specifically the data files they emit.

Used for:

- produce plots:
    - specify x
    - y comes specified
- produce csv data file:
    - specify columns to include

## if_power_plotter.py

Used to plot the data products of if_power.py

- create scatter plot
- create csv data file

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
