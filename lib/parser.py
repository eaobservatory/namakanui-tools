from pathlib import Path


__all__ = ['if_power', 'dcm_att', 'trx']


def if_power(parser):
    parser.add_argument('data_file', type=Path, help='Path to the data file to make plots of.')
    # parser.add_argument('--title', help='Optional title for the produced plot')
    parser.add_argument('--csv', default=False, action='store_true', help='Pass flag to also emit CSV file')
    return parser


def dcm_att(parser):
    parser.add_argument('data_file', type=Path, help='Path to the data file to make plots of.')
    parser.add_argument('--x', default='lo_ghz', help='Specify the column to use as the x-axis. default: lo_ghz')
    parser.add_argument('--ymin', default=0, type=int, help='Minimum value for the Y-axis. default=0')
    parser.add_argument('--ymax', default=50, type=int, help='Maximum value for the Y-axis. default=500')
    parser.add_argument('--yinc', default=5, type=int, help='Value to increment the Y-axis by. default=50')
    parser.add_argument('--xinc', default=5, type=int, help='Value to increment the X-axis by. default=1')
    parser.add_argument('--header', default=3, type=int, help='Number of lines in the header of the datafile. Do not include the column headers in this count, only the unstructured portion. default: 5')
    parser.add_argument('--footer', default=0, type=int, help='Number of lines in the footer of the datafile. default: 1')
    parser.add_argument('--dpi', default=150, type=int, help='Dots per inch of the individual plots, larger values result in larger resolution images. default: 600')
    parser.add_argument('--column', default=4, type=int, help='Number of columns in the plot collage output. default: 2')
    parser.add_argument('--noCleanUp', default=True, action="store_false", help='When passed the subplots created in the plots/ directory are NOT cleaned up.')
    parser.add_argument('--plots', default=Path('plots'), type=Path, help='Working directory to store subplots in, will be deleted if --noCleanUp is not passed AND it contains only files created by this script. default: plots')
    parser.add_argument('--quiet', default=False, action='store_true', help='When passed nothing will be sent to STDOUT')
    parser.add_argument('--sep', default=' ', help='seperation character used. default:" "')
    parser.add_argument('--csv', default=False, action="store_true", help='Flag to emit a csv.')
    parser.add_argument('--padw', default=0, type=int, help='left and right padding of the final collage. default=0')
    parser.add_argument('--padh', default=0, type=int, help='top and bottom padding of the final collage. default=0')
    return parser


def trx(parser):
    parser.add_argument('data_file', type=Path, help='Path to the data file to make plots of.')
    parser.add_argument('--x', default='#lo_ghz', help='Specify the column to use as the x-axis. default: #lo_ghz')
    parser.add_argument('--ymin', default=0, type=int, help='Minimum value for the Y-axis. default=0')
    parser.add_argument('--ymax', default=500, type=int, help='Maximum value for the Y-axis. default=500')
    parser.add_argument('--yinc', default=50, type=int, help='Value to increment the Y-axis by. default=50')
    parser.add_argument('--xinc', default=1, type=int, help='Value to increment the X-axis by. default=1')
    parser.add_argument('--header', default=5, type=int, help='Number of lines in the header of the datafile. Do not include the column headers in this count, only the unstructured portion. default: 5')
    parser.add_argument('--footer', default=1, type=int, help='Number of lines in the footer of the datafile. default: 1')
    parser.add_argument('--dpi', default=500, type=int, help='Dots per inch of the individual plots, larger values result in larger resolution images. default: 600')
    parser.add_argument('--column', default=2, type=int, help='Number of columns in the plot collage output. default: 2')
    parser.add_argument('--noCleanUp', default=True, action="store_false", help='When passed the subplots created in the plots/ directory are NOT cleaned up.')
    parser.add_argument('--plots', default=Path('plots'), type=Path, help='Working directory to store subplots in, will be deleted if --noCleanUp is not passed AND it contains only files created by this script. default: plots')
    parser.add_argument('--quiet', default=False, action='store_true', help='When passed nothing will be sent to STDOUT')
    parser.add_argument('--sep', default=' ', help='seperation character used. default:" "')
    parser.add_argument('--usb', default=True, action="store_false", help='Flag to plot USB DCMs. When passed disables USB output. default True')
    parser.add_argument('--lsb', default=False, action="store_true", help='Flag to plot LSB DCMs. When passed enables LSB output. default False')
    parser.add_argument('--csv', default=False, action="store_true", help='Flag to emit a csv.')
    parser.add_argument('--padw', default=0, type=int, help='left and right padding of the final collage. default=0')
    parser.add_argument('--padh', default=0, type=int, help='top and bottom padding of the final collage. default=0')
    return parser
