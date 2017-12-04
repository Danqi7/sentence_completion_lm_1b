import csv
import numpy as np
import argparse

labels = []
answers= {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}

def generate_labels(file_name, save_to_file):
  with open(file_name, 'rb') as f:
    reader = csv.reader(f, skipinitialspace=True)
    reader.next()
  
    for row in reader:
      label = answers[row[-1]]
      labels.append(label)

  labels = np.asarray(labels)
  np.save(save_to_file, labels)

if __name__ == "__main__":
   # command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", dest="file_name", default="./test_answer.csv",
                        help="The file (.csv) that contains the labels for your sentence completion instances.")
    parser.add_argument("--save_to", dest="save_to", default="./testing_labels.csv",
                        help="The file (.npy) that you want to save the porsed labels into.")
    ARGS = parser.parse_args()
    
    generate_labels(ARGS.file_name, ARGS.save_to_file)
