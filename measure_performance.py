import numpy as np
import argparse

def measure_accuracy(p_files, labels):
  perplexities = [np.load(x) for x in p_files]
  x = np.concatenate(perplexities, axis=0)
  y = np.load(labels)

  n = x.shape[0]

  predicted = np.argmin(x, axis=1)
  accuracy = np.mean(predicted == y[:n])

  print "testing data accuracy: %f, run lm_1b model on %i testing examples" % (accuracy, n)

if __name__ == "__main__":
  # Commoand line arguments
  parser = argparse.ArgumentParser()
  parser.add_argument("-p", "--perplexity", dest="p_file", nargs="+",
                      help="The file (.npy) that contains the perplexity result of running lm_1b, files should be in order",
                      required=True)
  parser.add_argument("-l", "--label", dest="labels",
                      help="The file (.npy) that contains the labels corresponding to the testing instences",
                      required=True)
  ARGS = parser.parse_args()
  print ARGS.p_file
  print ARGS.labels

  measure_accuracy(ARGS.p_file, ARGS.labels)
