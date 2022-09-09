import random
import subprocess


def bulkLaunch(scriptName, yourName):
    proxyList = []
    script = open("launch.ps1", "w")

    with open("proxies.txt", "r") as proxies:
        for proxy in proxies:
            proxyList.append(proxy)

    with open("accounts.txt", "r") as accs:
        for accounts in accs:
            account = accounts.split(":")
            userName = account[0]
            passWord = account[1].replace("\n", "")
            prxy = random.choice(proxyList).split(":")
            proxyHost = prxy[0]
            proxyPort = prxy[1]
            proxyUsername = prxy[2]
            proxyPass = prxy[3].replace("\n", "")

            command = f'javaw -Xmx512M -jar C:\\Users\\{yourName}\DreamBot\BotData\client.jar -script "{scriptName}" -fps 20 -no-fresh -destroy -accountUsername "{userName}" -accountPassword "{passWord}" -proxyHost "{proxyHost}" -proxyPort "{proxyPort}" -proxyUser "{proxyUsername}" -proxyPass "{proxyPass}" -breaks "Eating","Headache break" -minimized\nStart-Sleep -Seconds 15\n'
            script.write(command)
            print(command)

    script.close()


if __name__ == '__main__':
    file = open("systemInfo.txt", "r")
    scriptName = file.readline().replace("\n", "")
    systemName = file.readline()

    bulkLaunch(scriptName, systemName)
