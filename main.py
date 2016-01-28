
import subprocess
import argparse
import os
import shutil
from os import listdir
from os.path import isfile, join, isdir
import sys
from datetime import datetime
from profileGenerator import Generator
from Comparator import Comparator


def main():

	parser = argparse.ArgumentParser(description="This program generates a random sample of profiles of a given length in a given distribution")
	parser.add_argument('-l', nargs='?', type=int, help="profile length", required=False, default= 7)
	parser.add_argument('-d', nargs='?', type=str, help="distribution", required=False, default="normal")
	parser.add_argument('-n', nargs='?', type=int, help="number of profiles", required=False, default=7)
	parser.add_argument('-o', nargs='?', type=str, help='Destination folder', required=False , default="./")
	#parser.add_argument('-c', nargs='?', type=bool, help="is cluster version", required=True)
	#parser.add_argument('-', nargs='?', type=str, help="type of ANI (ANIm or ANIb)", required=True)

	args = parser.parse_args()

	runGenerator(args)

def runGenerator(args):

	generator = Generator(args.n, args.l, args.d)

	profiles = generator.generate_profiles()

	comparator = Comparator(profiles)
	
	print 'Prim:'
	print comparator.goeBURST('prim')
	print 'Kruskal:'
	print comparator.goeBURST('kruskal')



if __name__ == "__main__":
    main()