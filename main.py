import matplotlib.pyplot as plt
from generate import generate_data_and_write


def read_file(file_name):
    file = open(file_name)
    result = file.readlines()
    file.close()
    return result


def from_str_to_dict(lst):
    lst = list(map(lambda st: st.split(', '), lst))
    data = []
    lst[0][-1] = lst[0][-1].replace('\n', '')
    list(map(lambda l: data.append(dict(zip([row for row in lst[0]], l))), lst))
    for dic in data:
         dic[lst[0][-1]] = dic[lst[0][-1]].replace('\n', '')
    data.pop(0)
    return data


def show_graph(title, x_lable, y_lable, x_data, y_data):
    plt.plot(x_data, y_data, color='red', marker='o')
    plt.title(title)
    plt.xlabel(x_lable)
    plt.ylabel(y_lable)
    plt.show()


def filtrate(key_word1, key_word2, data):
    data = list(filter(lambda d: d[key_word1] == str(key_word2), data))
    data.sort(key=lambda x: x['DATE'])
    return data


def single_graph(key_word1, key_word2, data):
    if key_word1 not in data[0]:
        return
    data = filtrate(key_word1, key_word2, data)
    x_data = [row['DATE'] for row in data]
    y_data = [int(row['count']) for row in data]
    title = key_word1 + ': ' + str(key_word2)
    show_graph(title,  'DATE', 'AMOUNT', x_data, y_data)


def group_graph(key_word1, data):
    if key_word1 not in data[0]:
        return
    data.sort(key=lambda x: x[key_word1])
    object_list = {}
    for row in data:
        if row[key_word1] not in object_list:
            object_list[row[key_word1]] = 0
    for row in data:
        object_list[row[key_word1]] += int(row['AMOUNT'])
    x_data = [key for key in object_list]
    y_data = [object_list[key] for key in object_list]
    show_graph('GRAPH OF GROUP', key_word1, 'GENERAL AMOUNT', x_data, y_data)


def main():
    generate_data_and_write(12, 'FILE', 3, 4)
    data = read_file('FILE')
    data = from_str_to_dict(data)
    single_graph('STAFFID', 1, data)
    single_graph('RESOURCE', '1', data)
    group_graph('STAFFID', data)
    group_graph('RESOURCE', data)
    group_graph('DATE', data)

if __name__ == '__main__':
    main()
