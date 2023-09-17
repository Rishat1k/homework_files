def merging_files(list_of_files):
    merged_file = []
    for file in list_of_files:
        list_of_row = [file]
        with open(file, 'r', encoding='utf-8') as f:
            list_of_row.extend(f.readlines())
        merged_file.append(list_of_row)
    merged_file.sort(key=len)

    with open('merged_file.txt', 'w', encoding='utf-8') as f:
        for lst in merged_file:
            for row in lst:
                f.write(row.strip() + '\n')

merging_files(['2.txt', '1.txt'])




