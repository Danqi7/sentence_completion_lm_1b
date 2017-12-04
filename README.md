# sentence_completion_lm_1b

#### This repo provides data pipeline for measuring the performance of lm_1b model on sentence completion task

### Data
testing data is provided by Microsoft sentence completion
testing instance: testing_data.csv; testing_label: test_answer.csv

### Model
lm_1b pre-trained model: https://github.com/tensorflow/models/tree/master/research/lm_1b

lm_1b paper: @article{jozefowicz2016exploring, title={Exploring the Limits of Language Modeling}, author={Jozefowicz, Rafal and Vinyals, Oriol and Schuster, Mike and Shazeer, Noam and Wu, Yonghui}, journal={arXiv preprint arXiv:1602.02410}, year={2016} }

### Pipeline Structure
* generate_testing_files.py: Parse each sentence instance in sentence completion task into separate files labeled by its instance index and option index. For example, a sentence at index 5 with option a will be saved as "testing_data_5_1".
* generate_testing_labels.py: Parse test answers and bundle the labels into file in .npy format.
* batch_run_lm_1b.py: Run lm_1b model in 'eval' mode on each testing data instance and save the produced perplexity in to np.array in shape (number of testing data, number of options) into file in .npy format.
* measure_performance.py: Measure model accuracy on sentence completion testing data, given the produced perplexity done by _batch_run_lm_1b.py_ and the ground-truth labels generated in _generate_testing_labels.py_.

### Result
| Model         | Testing Data Size | Accuracy  |
| ------------- |:-----------------:| ---------:|
| LSTM+CNN      | 100               | 0.62      |
| LSTM+CNN      | 10001             | 0.65      |

### How to run
1. Run _generate_testing_files.py_ to generate testing data that's ready to be fed into lm_1b model
```
python generate_testing_files -h to see its input args
```
For example:
```
python generate_testing_files --file_name 'testing_data.csv' --count 100
```
2. Run _generate_testing_labels.py_ to parse test answers and save to .npy file
3. Run _batch_run_lm_1b.py_ to run lm_1b model on produced testing_data and save result perplexity to .npy file
4. Run _measure_performance.py_ to get model's accuracy on the sentence completion instances
> Make sure that you installed lm_1b model and can successfully execute it in eval mode.
> batch_run_lm_1b.py will take a while to run, depending on the number of instances you want to test
