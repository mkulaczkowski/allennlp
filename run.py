import subprocess
import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--mode", default="train", help="train or evaluate")
parser.add_argument("--logs_path", default="/logs/outputs", help="train or evaluate")
args = parser.parse_args()

EVALUATE ="python3 -m allennlp.run evaluate https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz --evaluation-data-file https://s3-us-west-2.amazonaws.com/allennlp/datasets/squad/squad-dev-v1.1.json --file-friendly-logging"
TRAIN ="python3 -m allennlp.run train training_config/bidaf.json -s %s --file-friendly-logging" % args.logs_path
TRAIN_CPU ="python3 -m allennlp.run train training_config/bidaf_cpu.json -s %s --file-friendly-logging" % args.logs_path

print("Running %s" % args.mode)
if args.mode == "train":
    subprocess.call(TRAIN, shell=True)
elif args.mode == "train_cpu":
    subprocess.call(TRAIN_CPU, shell=True)
elif args.mode =="evaluate":
    subprocess.call(EVALUATE, shell=True)
else:
    print(args.mode)
    raise(NotImplementedError)
