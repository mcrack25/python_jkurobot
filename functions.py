def joinUrl(main_url, url):
    full_url = main_url + '/' + url
    return full_url

def rowsOnPool(count, countPools):
    rows_on_pool = count // countPools
    return rows_on_pool

def splitMass(count, array):
    rows_on_pool = rowsOnPool(len(array), count)

    mass = []
    mas = []
    add_i = 0
    for arr in array:
        mas.append(arr)
        if not (len(mass) >= count):
            if len(mas) >= rows_on_pool:
                mass.append(mas)
                mas = []
        else:
            mass[add_i].extend(mas)
            mas = []
            add_i += 1
    return mass