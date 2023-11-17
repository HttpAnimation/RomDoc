# RomDoc
RomDoc is a docker that will allow you to host you're roms online for you're other pcs to download them.

# READ
This project is no longer maintand I will be remakeing this whole thing from scratch beacuse I did not like the way it ended up.

## Server
The server is made the pc that will host the rom files note tho that roms are not shared to everyone in the world only pcs on you're network will be able to download them.

## Client
The clinet is the software that will connect to the server and then allow you download you're roms.

## Surrported OS's
1) Linux 
2) MacOS
3) Windows (Not tested at all)

## Installing a server
To install this tool, follow these steps:
1) open a terminal and run these commands
```
sudo apt update
```

```
sudo apt upgrade -y
```

```
git clone https://github.com/HttpAnimation/RomDoc.git && cd RomDoc
```

Now build the docker with

```
python3 Build.py
```

Once done the run command will be

```
python3 Run.py
```

## Installing a client
To install a client, follow these steps:

### Python3
1) open a terminal and run these commands

Install the client
```
mkdir Python3-Client && cd Python3-Client && wget https://raw.githubusercontent.com/HttpAnimation/RomDoc/main/Clients/Python3/URL.ini && wget https://raw.githubusercontent.com/HttpAnimation/RomDoc/main/Clients/Python3/Client.py 
```
Run the client make sure to be in the same dir as the python3 script also make sure to have the [url setup](/Clients/Python3/README.md)
```
python3 Client.py
```