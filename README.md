# ready-set-run

This repository holds a collection of scripts and programs that run one or more clients and servers,
waiting for servers to be ready before running clients.
To contribute,
please create a pull request that creates a directory `tool-userid` (e.g., `python-gvwilson`)
with a self-contained example
and an `index.md` file that explains how to run it.
If you used any sort of AI to (help) craft your solution,
please mention it in your notes.

Please see `LICENSE.md` for licensing and `CODE_OF_CONDUCT.md` for community standards.

## Background

In January 2024 I started work on a short introduction to web programming for data scientists.
I wanted to be able to re-run the examples and capture their output automatically,
but concurrency kept getting in the way.
Launching multiple processes was easy;
getting arbitrary clients wait until servers were listening on specific ports
turned out to be surprisingly complicated.
Jean-Marc Saffroy kindly sent me a shell script that uses `lsof` in a busy-wait loop
to check the ports in question
(see `bash-saffroy/runner.sh` in this repository).
It does what I want (thanks, Jean-Marc)
but has me wondering what solutions would look like in other languages
and what we could learn by comparing them.

## Requirements

The command:

```
./runner.sh "8081 8082" \
    "server_1 8081 alpha" "server_2 8082 beta" \
    "client_1 8081 gamma" "client_2 8081 8082 delta"
```

in the `bash-saffroy` directory does the following:

1.  Run `server_1 8081 alpha` and `server_2 8082 beta`,
    where `server_1` and `server_2` are programs
    that listen on ports 8081 and 8082 and take extra arguments `alpha` and `beta` respectively.

2.  Wait until both programs are ready to accept socket connections on those ports.

3.  Run `client_1 gamma` and `client_2 delta`,
    where `client_1` sends a message based on the parameter `gamma` to port 8081
    while `client_2` sends a message based on the parameter `delta` to both ports 8081 and 8082.

4.  Waits for all the clients to exit,
    and then shuts down the servers by sending an interrupt.

Note that:

-   The first argument to `runner.sh` is a space-separated list of the ports used by the servers.

-   There is a one-to-one mapping between ports and servers,
    but the server commands need not appear in the same order as the ports
    (i.e., in the example above, `server_2` could appear before `server_1`).

-   Each client may send zero or more messages,
    and may communicate with zero or more servers.
    Client-server communication can be one-way or bidirectional,
    i.e.,
    a client might just send a message
    or it might wait for a reply.

## Contributions

| Name              | GitHub ID | Tool(s) | Directory    |
| ----------------- | --------- | ------- | ------------ |
| Jean-Marc Saffroy | saffroy   | bash    | bash-saffroy |
