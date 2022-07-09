from pathlib import Path
import argparse


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

optional = parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
optional.add_argument(
    '-t',
    '--dataset-dir',
    default='../datasets/dressipy',
    help='the folder to save the preprocessed dataset',
)
parser._action_groups.append(optional)
args = parser.parse_args()

dataset_dir = Path(args.dataset_dir)

from utils.data.preprocess import preprocess_dressipy

preprocess_dressipy(dataset_dir)