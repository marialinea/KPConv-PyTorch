import os
import laspy
from ply import read_ply, write_ply
from tqdm import tqdm
import numpy as np
import pdb
from config import bcolors
import sys
import time

def find_classes(directory):
    files = os.listdir(directory)
    cats = []

    for i, fn in enumerate(files):
        print("{}/{} files".format(i+1, len(files)))
        las = laspy.read(directory + fn)
        classes = list(np.unique(las['classification']))
        for cl in classes:
            if cl not in cats:
                cats.append(cl)
    return sorted(cats)


# Første versjon av å transformere las -> ply
# Se datasets/Autokart.py for endelig versjon av koden
#
# def las_to_array(self, filename):
#     print('Reading values from las file into numpy array')
#
#     las_info = {}
#     categories = ["X", "Y", "Z", "intensity", "classification"]
#
#
#     with laspy.open(filename) as f:
#
#         las = f.read()
#         points = las.points
#
#         # Reads the points category wise into a dictionary
#         for i, cat in enumerate(categories):
#             print("Processing category {}/{}".format(i+1, len(categories)), end='\r')
#             las_info["{}".format(cat)] = []
#             for i in tqdm(range(len(points)), desc='Points', leave=False):
#                 las_info["{}".format(cat)].append(float(points[cat][i]))
#             las_info["{}".format(cat)] = np.array(las_info["{}".format(cat)])
#
#
#         cloud_values = np.vstack([las_info["{}".format(cat)] for cat in categories]).T   # values stored in the following order: x y z intensity class
#
#         return cloud_values

# def prepare_las_to_ply(self):
#
#     print('\nPreparing ply files')
#     t0 = time.time()
#
#     # Folder for the ply files
#     ply_path = join(self.path, self.processed_path)
#     if not exists(ply_path):
#         makedirs(ply_path)
#
#     # Process the files in the different sets
#     for set in self.las_path:
#
#         which_set = set.split("/")[-1]
#
#         print("\nProcessing {} set".format(which_set))
#
#         # Folder for processed files for the different splits
#         set_path = join(ply_path, which_set)
#         if not exists(set_path):
#             makedirs(set_path)
#
#         las_files = listdir(set)
#         with tqdm(total=len(las_files), desc='Files') as t:
#             for las_file in las_files:
#
#                 # Pass if the ply file has already been computed
#                 ply_file = join(set_path, las_file.split('.')[0] + '.ply')
#                 if exists(ply_file):
#                     t.update()
#                     continue
#
#                 cloud_points = self.las_to_array(join(self.path, which_set, las_file))
#
#                 # Save as ply
#                 write_ply(ply_file, cloud_points, ['x', 'y', 'z', 'intensity', 'class'])
#                 t.update()
#
#     print('Done in {:.1f}s'.format(time.time() - t0))
#
#     return
