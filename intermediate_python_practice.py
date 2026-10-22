li.pop(2)
print(li)
print(li.append('neonce'))
print(li.extend('neosyn'))
marks=['prince',88.4,'neo',99,'synapse',100,'prince neo synapse']
print(marks)
marks[1]
print(marks)
#del marks
print(marks)
print(len(marks))
print(marks.append('99'))
print(marks)
print(marks.extend(['prince neo synapse']))
print(marks)
print(marks.clear())
mark=['prince',1,2,3,4,5,6,7,8,9,10]
print(mark.insert(9,8.5))
print(mark)
name,*rest=mark
print(name,rest)
print(mark.insert(4,5.5))
fan=['toofan','crompton','bldc','condenser','very_fast_fan']
bulb=['led','glass_bulb','torch','mobile_bulb']
no=[1,4,3,5,2,6,7,8,7,6,4,8,9,11,22,33,344,444,4,44,44444,4444444,5]
print(no,type(no),len(no),5 in no)
print(fan,bulb,type(fan),type(bulb))
fan.append('big_fan')
print(fan)
fan.append(bulb)
print(fan)
print(fan,bulb)
fan.extend('bulb')
print(fan)
print('crompton' in fan)
print('led' in bulb)
print(len(fan),len(bulb),type(fan),type(bulb))
no.insert(2,4.5)
print(no*15)
print(bulb+fan+no)
fan.remove('crompton'),bulb.remove('led')
print(fan,bulb)
fan.pop(1)
print(fan)
no.sort(reverse=True)
print(no)
no.sort()
print(no)
print(no+no)
print(fan,bulb,no,my_list,list_my,list,marks)
print(len(fan),len(no),len(bulb))






