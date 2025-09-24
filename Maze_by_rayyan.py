import sys

maze = [
    list("**************************************************"),
    list("*******                             ********* ****"),
    list("******* ************* ************* E******** ****"),
    list("******* ************* ***         *  ***    * ****"),
    list("*       ************* *   *********  ***  *** ****"),
    list("*******            ** *  ********        **** ****"),
    list("******* *** ****** ** *  ******************** ****"),
    list("******* *** ****** **    ******************** ****"),
    list("******* *** ****** ************************** ****"),
    list("******* *** **                      ********* ****"),
    list("***     *** ** **** **** ******************** ****"),
    list("*** ********** **** ****                ***** ****"),
    list("*** ********** **** ************************* ****"),
    list("*** ********** **** ************************* ****"),
    list("***            **** ***** ****** ************ ****"),
    list("******** ********** ************ ************ ****"),
    list("******** ********** ************      ******* ****"),
    list("********     ** *** ************ **** ******* ****"),
    list("*******************              **** ******* ****"),
    list("************************************* ******* ****"),
    list("************************************* ******* ****"),
    list("*************************************            S"),
    list("**************************************************"),
]


def printing_maze():
    print("\n")
    for g in maze:
        for gk in g:
            print(gk, end=" ")
        print()


print()
print("Problem".upper().center(100, "~"))
printing_maze()


def row_and_column_of_identifiers(l):
    for nu, i in enumerate(maze):
        for n in i:
            if n == l:
                return (nu, maze[nu].index(l))


e = row_and_column_of_identifiers("E")
s = row_and_column_of_identifiers("S")


def reverse_index_of_a_list(desired_list, j):
    indexes = []
    for ri, i in enumerate(desired_list):
        if i == j:
            indexes.append(ri)
    return indexes[-1]


def available_moving_points():
    list_of_all_available_moving_points = []
    for no1, rows in enumerate(maze):
        for no2, column in enumerate(rows):
            if column == " ":
                list_of_all_available_moving_points.append((no1, no2))
    return list_of_all_available_moving_points


a_m_p = available_moving_points()

x = 0
current_address = e  # keep it out of the loop for check
c = []  # ALl the moved and optional addresses are entered there
desired_path_list = []  # here we get original path
r, t = s
try:
    while True:
        # print('c:', c)
        # print('d:', desired_path_list)
        p = 0
        n, v = current_address
        if (n + 1, v) in a_m_p:
            c.append((n + 1, v))
            a_m_p.remove((n + 1, v))
            p += 1
        if (n - 1, v) in a_m_p:
            c.append((n - 1, v))
            a_m_p.remove((n - 1, v))
            p += 1
        if (n, v + 1) in a_m_p:
            c.append((n, v + 1))
            a_m_p.remove((n, v + 1))
            p += 1
        if (n, v - 1) in a_m_p:
            c.append((n, v - 1))
            a_m_p.remove((n, v - 1))
            p += 1
        if p == 1:
            desired_path_list.append(current_address)
            current_address = c[-1]
        if p >= 2:
            desired_path_list.append(current_address)
            desired_path_list.append("#")
            current_address = c[-1]
        if (
            current_address == (r + 1, t)
            or current_address == (r - 1, t)
            or current_address == (r, t + 1)
            or current_address == (r, t - 1)
        ):
            desired_path_list.append(current_address)
            final_path = desired_path_list[1:]
            for value in final_path:
                if value == "#":
                    final_path.remove(value)
            for inner_addresses in final_path:
                row, column = inner_addresses
                maze[row][column] = "#"
            print("\n")
            print("Solution".upper().center(100, "~"))
            printing_maze()
            sys.exit()
        if p == 0:
            ending_index1 = reverse_index_of_a_list(desired_path_list, "#")
            address_to_be_removed = current_address
            if ending_index1 != len(desired_path_list) - 1:
                address_to_be_removed = desired_path_list[ending_index1 + 1]
            ending_index2 = c.index(address_to_be_removed)
            desired_path_list = desired_path_list[:ending_index1]
            c = c[:ending_index2]
            current_address = c[-1]
        x += 1
except IndexError:
    print('Path Not Found...')