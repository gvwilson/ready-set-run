#!/usr/bin/env python

import requests
result = requests.get("http://localhost:8000/example.txt")
print(result)
