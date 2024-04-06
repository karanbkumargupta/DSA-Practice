


input_l=[1,2,3,4,5,6,7,8,9,10]

# o/p
# o_l=[1,2,3,4,8,7,6,5,9,10]



start=4
end=7

def swap(input_l,start,end):

    while start<end:
        c = input_l[start]
        input_l[start]=input_l[end]
        input_l[end]=c


        start+=1
        end-= 1
    return input_l



for i in range(len(input_l)):
    if i ==start:
        swap(input_l,start,end)

print(input_l)


# or


input_l[start:end+1]=reversed(input_l[start:end+1])

print(input_l)



