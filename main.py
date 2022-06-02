import os
import time
import threading
from multiprocessing import Pool

from libs.GetConfig import GetConfig
from libs.GetDriver import GetDriver
from functions import *

from actions.doLogin import doLogin
from actions.clickMenuItem import clickMenuItem
from actions.setFilter import setFilter
from actions.setAllChecks import setAllChecks
from actions.downloadFile import downloadFile

# Начало работы программы
ROOT_DIR = os.getcwd()
config = GetConfig(ROOT_DIR).get()

meta = dict({
    "config": config,
    "root_dir": ROOT_DIR
})

bases = config['bases']

# Выставляем количество потоков
if (config['count_thead'] > 0):
    count_thead = config['count_thead']
else:
    count_thead = os.cpu_count()

bases_masses = splitMass(count_thead, bases)

def runOne(base):
    driver = GetDriver(meta['root_dir'], meta['config']).get()

    # Авторизируемся
    doLogin(driver, meta, base).go()
    time.sleep(config['time_fast'])

    # Переходим на главную страницу
    driver.get(joinUrl(config['url'], 'Common/Main.aspx'))
    time.sleep(config['time_fast'])

    # Находим и открываем пункт меню
    clickMenuItem(driver, 'Формирование и печать выплатных документов: ЖК льготы', config['time_fast']).go()
    time.sleep(config['time_fast'])

    # Устанавливаем фильтр
    setFilter(driver, config).go()
    time.sleep(config['time_fast'])

    # Выбираем все выплаты
    setAllChecks(driver, config).go()
    time.sleep(config['time_fast'])

    # Скачиваем xls файлы
    downloadFile(driver, config).go()
    time.sleep(config['time_very_slow'])

    # Выходим из браузера
    driver.quit()

def runAll(bases):
    print('Программа запущена!!!')
    for base in bases:
        print('Работаем над базой {}'.format(base['base']))
        runOne(base)
        print('Завершили работу над базой {}'.format(base['base']))
    print('Программа завершена!!!')


# Режим Мультитрейдинга
def ThreadMode(bases):
    threads = []
    for base in bases:
        t = threading.Thread(target=runAll, args=(base,))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()

# Режим Мультипроцессинг
def PoolMode(bases):
    array = bases
    p = Pool(len(array))
    p.map(runAll, array)

def Go(bases, thread_type='thread'):
    if (thread_type == 'thread'):
        ThreadMode(bases)
    elif (thread_type == 'pool'):
        PoolMode(bases)
    else:
        print('Ошибка!!! Не верно выбран тип многопоточности!')

if __name__ == '__main__':
    #runAll(bases)
    Go(bases_masses, config['type_thead'])