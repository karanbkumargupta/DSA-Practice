str_in="abvsgabhjuiabvs"
sub_str="ab"


# print(str_in.count(sub_str))

sub_n=len(sub_str)
n=len(str_in)
count=0

for i in range(n-sub_n+1):
    result=str_in[i:sub_n+i]
    if result == sub_str:
        count+=1


print(count)