# Dreambot Bulk Launcher

## Prerequisites

Before you proceed further make sure you have installed Java and attached it to your environment variables.

Also make sure to download python if you haven't:

https://www.python.org/downloads/

If you are unsure how to set environment variables follow this guide:

https://stackoverflow.com/questions/15796855/java-is-not-recognized-as-an-internal-or-external-command

Next clone down the project:

`git clone <url>`

**OR**

Download the project as a zip file


## How to use

This is a very simple tool launch your dreambot client in bulk. All you gotta modify is the
3 files you see in the project:

* accounts.txt
* proxies.txt
* systemInfo.txt

Now let me break them down and how you should format them.


### accounts.txt

Starting with the accounts.txt file, you have to write the accounts that you want to launch in the following format:

```
username:pass
username:pass
username:pass
username:pass
```

Very simple right? Just like in any other platforms :-)


### proxies.txt

Next we have the proxies.txt file. All you have to pass in this file are the proxies you want to use.
there's a catch here. A random proxy will be chosen from the file and be attached to an account.

Please fill the file in the following format:

```
<ip>:<port>:<username>:<password>
<ip>:<port>:<username>:<password>
<ip>:<port>:<username>:<password>
<ip>:<port>:<username>:<password>
```

### systemInfo.txt

Now you probably wonder what this systemInfo.txt file is. It is simply used to get access to the .jar file of dreambot, therefore the script needs the absolute path.

This file needs 2 inputs. First line should be the name of the script you want to run, and the second line should be the system name. You can find the system name by entering any folder and look at the name after C:\Users\ in the path.

Example:
```
Sub Account Builder
deniz
```


After you have filled the files as described, simply run the following command to generate a powershell script:

```
python bulkLauncher.py
```

then 

```
.\launch.ps1
```

Enjoy :-)
