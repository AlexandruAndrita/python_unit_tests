def select_files(files_list,files):
    for i in files_list:
        if i.endswith(".txt"):
            ok = 1
            for j in files:
                if i == j:
                    ok = 0
            if ok == 1:
                files.append(i)
    files.sort()

