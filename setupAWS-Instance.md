# Setup Instance on AWS

## Setup SSH Key

1. Use the key pair given to you by the instructor.
2. Cd into the to `~/.ssh/` directory.
3. Create a file called `eng130.pem` and copy the contents of the key pair into it.
4. Change the permission of the key pair by running `chmod 400 eng130.pem`

## Steps to create an instance

1. Selet the region `Europe (Ireland)` from the top right corner.
2. Click on `Services` and select `EC2`.
3. Click on `Launch Instance`.
4. Select `Ubuntu Server 18.04 LTS (HVM), SSD Volume Type` and click on `Select`.
5. Leave the `Instance Type` as default
6. Leave the `Storage` as default
7. Select Key Pair as `eng-130`
8. Select `Create a new security group` and add the following rules:
   - Type: `SSH`, Protocol: `TCP`, Port Range: `22`, Source: `My IP`
   - Type: `HTTP`, Protocol: `TCP`, Port Range: `80`, Source: `Anywhere`
9. Click on `Launch Instance`.

## Steps to connect to the instance

1. Click on `View Instances`.
2. Select your instance and click on `Connect`.
3. Copy the SSH command and paste it in the Bash terminal.
4. You should be connected to the instance.

## Update and Upgrade the Instance

Once you're connected to the instance, you can run the following commands to update and upgrade the instance:

```bash
sudo apt update
sudo apt upgrade
```

## Install Nginx and Setup Reverse Proxy

1. Install Nginx by running `sudo apt install nginx`
2. From here you can follow the instructions in the [ReverseProxyNginx.md](https://github.com/AbisheK0726/eng130-virtualisation/blob/main/ReverseProxyNginx.md) file to setup the reverse proxy.
