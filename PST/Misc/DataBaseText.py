with open("PST\Misc\databasefiles\db.txt", "r") as file:
    database = file.readlines()

with open("PST\Misc\databasefiles\wal.txt", "r") as f:
    wal = f.readlines()


sizes = {}

for line in database:
    # if "Nano" in line:
    #     if "Jade" in line:
    #         if "Nano" in sizes.keys():
    #             temp = sizes["Nano"]
    #             temp.append(line)
    #             sizes["Nano"] = temp
    #         else:
    #             sizes["Nano"] = [line]
    if "Medium" in line:
        if "Jade" in line:
            if "Medium" in sizes.keys():
                temp = sizes["Medium"]
                temp.append(line)
                sizes["Medium"] = temp
            else:
                sizes["Medium"] = [line]
    elif "Small" in line:
        if "Jade" in line:
            if "Small" in sizes.keys():
                temp = sizes["Small"]
                temp.append(line)
                sizes["Small"] = temp
            else:
                sizes["Small"] = [line]
    # elif "Micro" in line:
    #     if "Micro" in sizes.keys():
    #         sizes["Micro"] = sizes["Micro"] + 1
    #     else:
    #         sizes["Micro"] = 1
    # elif "Little" in line:
    #     if "Little" in sizes.keys():
    #         sizes["Little"] = sizes["Little"] + 1
    #     else:
    #         sizes["Little"] = 1
    # elif "Huge" in line:
    #     if "Huge" in sizes.keys():
    #         sizes["Huge"] = sizes["Huge"] + 1
    #     else:
    #         sizes["Huge"] = 1
    # elif "Large" in line:
    #     if "Large" in sizes.keys():
    #         sizes["Large"] = sizes["Large"] + 1
    #     else:
    #         sizes["Large"] = 1
#print(sizes.values())
                
result_list = []

for line in wal:
    # Find the index of "Medium Jade" in each line
    index = line.find("Nano Jade")
    
    # Extract the substring after "Medium Jade" and remove any leading/trailing whitespace
    result = line[index + len("Nano Jade"):].strip()
    
    # Append the result to the list
    result_list.append(result)
n = 0

print(sizes)

for i in sizes.keys():
    for b in sizes[i]:
        index = b.find("Medium Jade")
    # Extract the substring after "Medium Jade" and remove any leading/trailing whitespace
        result = b[index + len("Medium Jade"):].strip()
        if result in result_list:
            result_list.remove(result)
            print(n)
            n += 1
#print(result_list)