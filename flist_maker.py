#!/usr/bin/python

import argparse
import os
from random import shuffle

parser = argparse.ArgumentParser()
parser.add_argument('--folder_path', default=os.path.join('datasets', 'celebahq'), type=str,
                    help='The folder path')
parser.add_argument('--train_filename', default=os.path.join('datasets', 'celebahq', 'flist', 'train.flist'), type=str,
                    help='The output filename.')
parser.add_argument('--validation_filename', default=os.path.join('datasets', 'celebahq', 'flist', 'validation.flist'), type=str,
                    help='The output filename.')
parser.add_argument('--test_filename', default=os.path.join('datasets', 'celebahq', 'flist', 'test.flist'), type=str,
                    help='The output filename.')

if __name__ == "__main__":

    args = parser.parse_args()
    files = os.listdir(args.folder_path)

    training_file_names = []
    validation_file_names = []
    test_file_names = []

    counter = 0
    for file in files:
        
        if len(file) < 3 or file[-3:] != "jpg":
            continue

        file = os.path.join(args.folder_path, file)
        
        if counter % 20 == 18:
            validation_file_names.append(file)
        elif counter % 20 == 19:
            test_file_names.append(file)
        else:
            training_file_names.append(file)
            
        counter += 1
        
    with open(args.train_filename, 'w') as f:
        f.write("\n".join(training_file_names))
        
    with open(args.validation_filename, 'w') as f:
        f.write("\n".join(validation_file_names))

    with open(args.test_filename, 'w') as f:
        f.write("\n".join(test_file_names))

    # print process
    print("Written file is: ", args.train_filename)
    print("Written file is: ", args.validation_filename)
    print("Written file is: ", args.test_filename)
    
    print("Number of training samples: ", len(training_file_names))
    print("Number of validation samples: ", len(validation_file_names))
    print("Number of test samples: ", len(test_file_names))
