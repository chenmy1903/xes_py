import os
import sys
import time
import ctypes

from pickleshare import PickleShareDB

pip_config = \
"""
[global]
index-url = https://pypi.org/simple/
[install]
trusted-host=pypi.org
"""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Setting:
    def __init__(self, file_name, config={}, config_path="~/.duck_game/xes_py"):
        super().__init__()
        self.file_name = file_name
        self.db = PickleShareDB(config_path)
        if file_name not in self.db:
            self.db[file_name] = config

    def add(self, key, value):
        """添加新值"""
        new = self.db[self.file_name]
        if value:
            new[key] = value
            self.db[self.file_name] = new

    def read(self, config=None):
        """读文件"""
        if config:
            return self.db[self.file_name][config]
        return self.db[self.file_name]


def pause(text=None, function=None):
    if text:
        print(text)
    os.system("pause")
    if function:
        function()


def title(title: str):
    os.system(f"title {title}")


def wait_time(t: int, text="程序将在{}秒后开始执行"):
    try:
        for timmer in range(t, -1, -1):
            print(text.format(timmer), end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("")
        print("\033[0;31m用户取消了操作\033[0m")
        pause()
        sys.exit(1)
    print('\r')


def search_path(file_name):
    cp = os.walk("C:/")
    count = 0
    for root, dirs, files in cp:
        root = str(root)
        dirs = str(dirs)
        count += 1
        print(f"寻找文件：{count}", end="\r")
        if file_name in dirs or file_name in files:
            flag = 1
            if "$Recycle.Bin" not in os.path.join(root, dirs):
                return os.path.join(root, dirs)
    print('')
    return None


def main():
    title("xes_py")
    config = Setting("config")
    print("欢迎使用xes_py")
    print("本工具为xes编程助手的pip补丁")
    pause("按任何键继续安装")
    print("正在查找程序")
    try:
        if "xes_helper" not in config.read() or not config.read("xes_helper") or not os.path.isdir(config.read("xes_helper")):
            helper = os.path.dirname(search_path("xes_py_helper.exe"))
        else:
            helper =  config.read("xes_helper")
    except KeyboardInterrupt:
        print("\033[0;31m用户取消了操作\033[0m")
        pause()
        sys.exit(1)
    if not helper:
        print("检测到您没有安装xes编程助手")
        pause(function=sys.exit)
    else:
        print("寻找成功")
        print(f"path: {helper}")
        config.add("xes_helper", helper)
    pip_config_file = os.path.join(helper, "pip.ini")
    try:
        with open(pip_config_file, "w", encoding="UTF-8") as f:
            print("开始修改")
            f.write(pip_config)
    except IOError:
        print("权限不足，请确认管理员")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", " ".join(sys.argv), None, 1)
    print("成功")
    


if __name__ == "__main__":
    main()
