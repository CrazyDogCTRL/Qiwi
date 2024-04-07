import os
import subprocess
import sys


def run_server():
    # Определяем пути к server.py и другим модулям
    script_path = os.path.join(os.path.dirname(__file__), 'web_app', 'server.py')
    response_module_path = os.path.join(os.path.dirname(__file__), 'web_app', 'response.py')
    control_module_path = os.path.join(os.path.dirname(__file__), 'Control', 'control.py')
    other_module_path = '/Users/crazydogctrl/PycharmProjects/banksystem/Control/control.py'

    # Добавляем пути к другим модулям в sys.path
    sys.path.append(response_module_path)
    sys.path.append(other_module_path)
    sys.path.append(other_module_path)

    # Проверяем, существует ли файл server.py
    if not os.path.isfile(script_path):
        print("Ошибка: Файл server.py не найден.")
        return

    # Запускаем server.py с помощью subprocess
    subprocess.call([sys.executable, script_path])


if __name__ == "__main__":
    run_server()
