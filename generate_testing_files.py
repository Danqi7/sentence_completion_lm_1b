import csv
import argparse

def generate_files(testing_file, number):
  with open(testing_file, 'rb') as f:
    reader = csv.reader(f, skipinitialspace=True)
    reader.next()

    for i, row in enumerate(reader):
      # Fill in the blanks 
      sent = row[1]
      options = row[2:2+5]
      complete_sents = [sent.replace('_____', op) for op in options]

      # Write complete sents to testing_input files
      for op_i, complete_sent in enumerate(complete_sents):
        output_file = open("./testing/testing_data_%i_%i" %(i+1, op_i+1), 'w')
        output_file.write(complete_sent)
        output_file.close()

      print complete_sents

      if i == number:
        break;

if __name__ == "__main__":
   # Command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", dest="file_name", default="testing_data.csv",
                        help="The testing data file (.csv) that you want generate the bathes.")
    parser.add_argument("--count", dest="count", type=int, default=30,
                        help="The number of testing data instances you want to generate")
    ARGS = parser.parse_args()

    generate_files(file_name, count)
