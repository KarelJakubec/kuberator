# Kuberator

Things you cannot do simply with just kubectl. Currently set of independent tools with
common library. Can be used as CLI or as lib for other tools.

## Installation

Clone repo and install dependencies. Then just run the tool you want from src.

PyPi package to be added soon.

```
virtualenv env
. env/bin/activate

pip install -r requirements.txt

python3 src/the_tool_you_want.py
```

## Tools

### get_cluster_utilization.py

Provides information about resource requests and limits on all nodes in cluster. Output
in yaml, json or human readable table.
