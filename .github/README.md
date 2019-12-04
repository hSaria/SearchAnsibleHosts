# SearchAnsibleHosts

I like using my Ansible inventory when SSH-ing or running a script against a list of devices, but the native method of listing hosts in Ansible (i.e. `ansible --list-hosts some:pattern`) is too slow for me (\~800ms), so I made this to drop that way down (\~50ms).

# Installation

```shell
pip3 install search-ansible-hosts
```

# Usage

```shell
search-ansible-hosts some:pattern
```

Checkout `search-ansible-hosts -h` for the list of options.

I **highly** recommend that you create an alias for this script. For instance, I've got `alias shost=search-ansible-hosts` in my `.bash_profile`.

# Internals

Whenever you run this script, it will create a server that runs in the background if one doesn't exist. The job of that server is to cache the Ansible inventory in memory and listen on a local port. Afterwards, it will act as a client and will send the pattern to the server. The server will send back the list of hosts and then closes the connection to that client, but it will remain in the background, ready to accept any other requests.

The process of importing the required Ansible modules and instantiating the inventory takes the most time, but since the server continues to run in the background, you will only suffer from the delay on the first run of this script (i.e. when there isn't a server).

Technically, the script is only needed to launch the server, after which you can use any program to send the pattern to it. For instance, you can do something like `echo some:pattern | nc 127.0.0.1 16001` so long as the server is already running.
