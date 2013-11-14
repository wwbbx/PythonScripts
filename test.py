import subprocess
import re

processName = "tasklist.exe"
checkCmd = subprocess.Popen("tasklist", shell=True, stdout=subprocess.PIPE)
print(checkCmd)
for info in checkCmd.stdout:
    print(info)
    if re.search(processName, info):
        print ("Found " + processName)
    else:
        print ("Can't find this process.")