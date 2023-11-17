# RomDoc
RomDoc is a docker that will allow you to host you're roms online for you're other pcs to download them.

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