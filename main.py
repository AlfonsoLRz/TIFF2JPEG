import argparse
import csv
import cv2
import glob
import numpy as np
import os
import subprocess

csv_extension = '.csv'
jpeg_extension = '.jpg'
script_folder = 'Scripts/'
exiftool_exe = os.path.abspath(script_folder + 'exiftool.exe')
temp_folder = 'temp/'
tif_extensions = ['.tif', '.tiff']


def export_temp_to_csv(filename, img):
    with open(filename, 'w', newline='') as fh:
        writer = csv.writer(fh, delimiter=',')
        writer.writerow(['x', 'y', 'temp (c)'])
        row_values = [[e[0][0], e[0][1], e[1]] for e in np.ndenumerate(img)]
        writer.writerows(row_values)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("TIFF2JPEG")
    parser.add_argument("--input", help="Input folder", type=str, default='In/', required=True)
    parser.add_argument("--output", help="Output folder", type=str, default='Results/', required=True)
    parser.add_argument('--high_gain', action=argparse.BooleanOptionalAction, default=False)
    args = parser.parse_args()

    if os.path.isdir(args.input):
        if not os.path.isdir(args.output):
            os.mkdir(args.output)

        if not os.path.isdir(temp_folder):
            os.mkdir(temp_folder)

        for tif_extension in tif_extensions:
            for path in glob.glob(args.input + '*' + tif_extension):
                basename = os.path.basename(path)
                basename = basename[0:len(basename) - len(tif_extension)]

                tiff_img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
                norm = np.linalg.norm(tiff_img)
                max, min = np.max(tiff_img), np.min(tiff_img)
                tiff_img = (tiff_img - min) / (max - min) * 255

                cv2.imwrite(args.output + basename + jpeg_extension, tiff_img)
                export_temp_to_csv(args.output + basename + csv_extension, tiff_img)

                print('Done processing of ' + path + '...')

                command_copy = exiftool_exe + ' -TagsFromFile ' + args.input + basename + tif_extension + \
                                              ' -all:all>all:all ' + args.output + basename + jpeg_extension
                p = subprocess.Popen(command_copy, stdout=subprocess.PIPE, shell=True, cwd='.')
                if p.stdout.read() != b'':
                    print(p.stdout.read())
