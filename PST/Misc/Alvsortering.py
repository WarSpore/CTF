def Sorting(lst):
    lst2 = sorted(lst, key=len)
    return lst2
     
# Driver code


with open ("PST\Misc\\random_text.bin","r") as f:
    text = f.read()
    text_split = text.split("\x00")
    li = []
    for x in text_split:
        if len(x) > len("}e5g2xsgM0DxcUTX73DWZigGtuY4CmPy3xN4c52DcU2UDxdg2WegrFuYGK7W5LAygqenX1Y6djNbGOZu"):
            continue
        li.append(x)
    text_split = li
    text_split = (Sorting(text_split))
    print(text_split)
    
    for x in range(1,len(text_split)):
        print(text_split[x][0],end="")

# print(text_split)




# for i,x in enumerate(text_split):
#   temp = (len(x))
#         if temp > max:
#             max = temp
#             k = i
#     print(max,text_split[k])