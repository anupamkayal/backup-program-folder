fill_list=[]
ask_count=int(input("enter the number of time: "))
for i in range(0,ask_count):
    ask_num=int(input("enter number: "))
    fill_list.append(ask_num)
avg=sum(fill_list)/ask_count
#round_func=round(avg,2)
print(f"here is the average of your number:{avg}")