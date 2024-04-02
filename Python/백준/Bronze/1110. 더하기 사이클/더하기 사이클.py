n = int(input())
time = 0

def get_each_sum(num):
   str_num = str(num)
   if(len(str_num)==1):
       str_num = '0' + str_num
   str_list1 = [int(digit) for digit in str_num]
   compare_1 = sum(str_list1)
   if(compare_1<10):
       return 10*str_list1[1]+compare_1
   else:
       str_num2 = str(compare_1)
       str_list2 = [int(digit) for digit in str_num2]
       return str_list2[1] + 10*str_list1[1]
        

n_temp = n
while True:
    n = get_each_sum(n)
    time+=1
    if(n == n_temp):
        break
    
print(time)
    

