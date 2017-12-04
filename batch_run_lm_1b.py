import subprocess
import numpy as np

'''
    batch_run_lm_1b runs bathes of testing data on lm_1b pre-trained model by Google Research
    specify the start and the number of testing data instances you want to run
    perplexity result will be save into .npy files

    Make sure you have lm_1b model already installed and ready to run.
    lm_1b model: https://github.com/tensorflow/models/tree/master/research/lm_1b
    Your folder should look like this:
    ./sentence_completion_lm_1b/
        ./lm_1b <-- lm_1b shoud be properly set up
        ./batch_run_lm_1b.py
        ...
'''

def batch_run(start, n):
    start = 101 # start
    n = 900 # run sentence from start to start + n
    n_ops = 5 # always 5 options for each sentence instance
    cmd_start = "bazel-bin/lm_1b/lm_1b_eval --mode eval --pbtxt data/graph-2016-09-10.pbtxt --vocab_file data/vocab-2016-09-10.txt"

    perplex = []
    for s_i in range(start, start + n + 1):
      probs = []
      for op_i in range(1, n_ops+1):
        cmd = cmd_start + " --input_data ./testing/testing_data_%i_%i" %(s_i, op_i) + " --ckpt 'data/ckpt-*'"

        p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, cwd='./')
        p.wait()
        output = p.stderr.readlines()[-1]
        prob = output.split()[-1]
        prob = float(prob[:-1])
        probs.append(prob)

      print probs
      perplex.append(probs)

    # Save result to .npy
    perplex = np.asarray(perplex)
    save_to = 'testing_data_perplex_%i_to_%i' % (start, start + n)
    np.save(save_to, perplex)

if __name__ == "__main__":
   # Command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", dest="start", type=int, default=0,
                        help="The index of testing data where you want to start running the model.")
    parser.add_argument("--count", dest="count", type=int, default=10,
                        help="The number of testing data instances you want to run on lm_1b model")
    ARGS = parser.parse_args()

    generate_files(ARGS.start, ARGS.count)
