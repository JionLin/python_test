# for循环实现
# day = 1
# for day in range(1,31):
#     print(f'********📅第{day}天********')
#     for group in range(1,4):
#         print(f'💪这是第{group}组仰卧起坐')
#     print(f'✅第{day}天任务已完成！明天继续！\n')
# print(f'🎉为期{day}天的健身计划完成，我的腹肌在闪闪发光！')




day=1
for i in range(1,31):
    print(f"第{day}天")
    for j in range(1,4):
        print(f'是第{j}组')
        j=j+1
    print(f'第{day}天做完了第{j-1}组')
    day=day+1




# while循环实现
# day = 1
# while day <= 30:
#     print(f'********📅第{day}天********')
#     group = 1
#     while group <= 3:
#         print(f'💪这是第{group}组仰卧起坐')
#         group += 1
#     print(f'✅第{day}天任务已完成！明天继续！\n')
#     day += 1
# print(f'🎉为期{day - 1}天的健身计划完成，我的腹肌在闪闪发光！')
#


# day=1
# while day < 5:
#     print(day)
#     group =1
#     while group <=3:
#         print(f'做第{group}组')
#         group =group+1
#     print(f'第{day}做完{group-1}组')
#     day=day+1
# print('完成')