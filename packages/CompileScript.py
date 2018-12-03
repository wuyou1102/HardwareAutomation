# -*- encoding:UTF-8 -*-
import os
import sys
from libs import Utility
import shutil

root_path = "C:\Users\OEMUSER\PycharmProjects\HardwareAutomation"
name = "Automation.py"
abs_path = os.path.abspath(os.path.dirname(sys.argv[0]))
resource_files = list()


def find_resource_files(path):
    for f in os.listdir(path):
        p = os.path.join(path, f)
        if os.path.isdir(p):
            find_resource_files(path=p)
        else:
            relative_path = os.path.relpath(path, root_path)
            resource_files.append((p, relative_path))


def get_add_data_part(resources):
    tmp = list()
    for abs, rel in resources:
        line = "--add-data {abs_path};{relative_path}".format(abs_path=abs, relative_path=rel)
        tmp.append(line)
    return ' '.join(tmp)


def build():
    find_resource_files(os.path.join(root_path, 'resource'))
    data_part = get_add_data_part(resources=resource_files)
    command = "pyinstaller -w -y --icon=favicon.ico --workpath {tmp} --distpath {out} {data} {script}".format(
        tmp=os.path.join(abs_path, 'tmp'),
        out=os.path.join(abs_path, 'out'),
        data=data_part,
        script=os.path.join(root_path, name)
    )
    result = Utility.execute_command(command)
    if result.exit_code == 0:
        return True
    return False


def deploy():
    shutil.move(os.path.join(abs_path, 'out', "Automation"),
                os.path.join(abs_path, "Automation_%s" % Utility.get_timestamp()))
    shutil.rmtree(os.path.join(abs_path, 'tmp'))
    shutil.rmtree(os.path.join(abs_path, 'out'))
    os.remove(os.path.join(abs_path, 'Automation.spec'))


if __name__ == '__main__':
    if build():
        deploy()
