#!/usr/bin/env python
import argparse

from kubernetes import config
from lib.resource_utilization import get_cluster_utilization

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Get overall cluster utilization.')
	parser.add_argument(
		"-o", "--output", type=str, choices=["table", "json", "yaml"], 
		default="table", help="Format of output."
	)
	args = parser.parse_args()
	
	
	config.load_kube_config()
	print(get_cluster_utilization(
		output=args.output
	))

