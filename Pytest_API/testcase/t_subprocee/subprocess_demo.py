
import subprocess

# 使用列表形式传递命令和参数, linux 上的 ls 命令
# exit_code = subprocess.call(["ls", "-l"])
# 使用 Windows 上的 dir 命令
# exit_code = subprocess.call(["dir"], shell=True)
exit_code = subprocess.call(["cmd.exe", "/c", "dir"])

print(exit_code)
