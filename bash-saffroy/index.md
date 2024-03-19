1.  Create a virtual environment for Python 3.12 and activate it.

2.  `pip install -r requirements.txt`.

3.  `./runner.sh 8000 ./server.sh ./client.py`

Sample output:

```
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
::1 - - [19/Mar/2024 17:49:42] "GET /example.txt HTTP/1.1" 200 -
<Response [200]>
./runner.sh: line 31:  9257 Terminated: 15          $CMD
```
