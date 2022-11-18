# Task 4 : Rank the students

with open("input4.txt", 'r') as file_in:

    n = int(file_in.readline())
    ids = file_in.readline()
    marks = file_in.readline()

    ids = list(map(int, ids.split()))
    marks = list(map(int, marks.split()))


    newDict = {}

    for i in range(len(ids)):
        if newDict.get(marks[i]) == None:
            newDict[marks[i]] = [ids[i]]
        else:
            newDict[marks[i]].append(ids[i])


    # Sorting by marks
    def ins_sort(array):

        for j in range(1, len(array)):
            key = array[j]
            i = j - 1

            while i >= 0 and array[i] > key:

                array[i + 1] = array[i]
                i = i - 1
            array[i + 1] = key

    ins_sort(marks)

    for key, value in newDict.items():
        temp = newDict[key]
        ins_sort(temp)
        newDict[key] = temp

    with open("output4.txt", 'w') as file_out:

        for m in range(len(marks) - 1, 0, -2):

            i_d = newDict[marks[m]]

            if len(i_d) == 0:

                file_out.write(f"ID: {i_d[0]} Mark: {marks[m]}\n")

            else:
                for x in i_d:
                    file_out.write(f"ID: {x} Mark: {marks[m]}\n")


