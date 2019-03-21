"""
Functions related to cluster utilization
"""
import json
import yaml
from kubernetes import client
from tabulate import tabulate

from lib.conversions import mem_bytes_to_mi, mem_share_to_bytes, cpu_share_to_cores

def get_cluster_utilization(output="table"):
	v1 = client.CoreV1Api() 
	ret = v1.list_node(watch=False)
	nodes = {}

	for i in ret.items:
		nodes[i.metadata.labels["kubernetes.io/hostname"]] = {
			"role": i.metadata.labels["kubernetes.io/role"],
			"cpu": {
				"capacity": float(i.status.capacity["cpu"]),
				"requests": 0,
				"limits": 0
			},
			"memory": {
				"capacity": mem_share_to_bytes(i.status.capacity["memory"]),
				"requests": 0,
				"limits": 0
			},
			"pod_classes": {
				"Burstable": 0,
				"Guaranteed": 0,
				"BestEffort": 0
			}
		}

	pods = v1.list_pod_for_all_namespaces()

	for pod in pods.items:
		node = pod.spec.node_name
		nodes[node]["pod_classes"][pod.status.qos_class] += 1
		for c in pod.spec.containers:
			r = c.resources.requests
			l = c.resources.limits

			r_cpu = 0.0
			r_mem = 0.0
			l_cpu = 0.0
			l_mem = 0.0
			
			if r is not None:
				r_cpu = r.get("cpu", 0.0)
				r_mem = r.get("memory", 0.0)

			if l is not None:
				l_cpu = l.get("cpu", 0.0)
				l_mem = l.get("memory", 0.0)

			nodes[node]["cpu"]["requests"] += cpu_share_to_cores(r_cpu)
			nodes[node]["cpu"]["limits"] += cpu_share_to_cores(l_cpu)

			nodes[node]["memory"]["requests"] += mem_share_to_bytes(r_mem)
			nodes[node]["memory"]["limits"] += mem_share_to_bytes(l_mem)
	if output == "json":
		return json.dumps(nodes, indent=2)
	elif output == "yaml":
		return yaml.dumps(nodes, indent=2)
	elif output == "table":
		table_data = []
		for (node_name, node) in nodes.items():
			table_data.append(
				[
					node_name,
					node["role"],
					round(node["cpu"]["capacity"], 2),
					round(node["cpu"]["requests"], 2),
					round(node["cpu"]["requests"] / node["cpu"]["capacity"] * 100, 2),
					round(node["cpu"]["limits"], 2),
					round(node["cpu"]["limits"] / node["cpu"]["capacity"] * 100, 2),
					round(mem_bytes_to_mi(node["memory"]["capacity"]), 2),
					round(mem_bytes_to_mi(node["memory"]["requests"]), 2),
					round(node["memory"]["requests"] / node["memory"]["capacity"] * 100, 2),
					round(mem_bytes_to_mi(node["memory"]["limits"]), 2),
					round(node["memory"]["limits"] / node["memory"]["capacity"] * 100, 2),
                    node["pod_classes"]["Guaranteed"],
                    node["pod_classes"]["Burstable"],
                    node["pod_classes"]["BestEffort"]
				]
			)

		return tabulate(
			table_data, 
			headers=[
				"Node name", "Role", "CPU Capacity", "CPU Req", "CPU Req Perc", "CPU Lim", "CPU Lim Perc", 
				"Mem Capacity MB", "Mem Req", "Mem Req Perc", "Mem Lim", "Mem Lim Perc", "Pods Guranteed", 
				"Pods Burstable", "Pods BestEffort"
			]
		)