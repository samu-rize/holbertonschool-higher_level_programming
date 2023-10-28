#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    rst_list = []

    for idx in range(list_length):

        rst = 0
        try:
            rst = my_list_1[idx] / my_list_2[idx]

        except TypeError:
            print('wrong type')
        except ZeroDivisionError:
            print('division by 0')
        except IndexError:
            print('out of range')

        finally:
            rst_list.append(rst)

    return rst_list
