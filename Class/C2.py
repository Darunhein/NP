#First way to do it
week=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
weekend=[]
for i,day in enumerate(week):
    if i==5:
        weekend.append(i)
        weekend.append(i+1)
print(weekend)

#Second way to do it
week=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
weekend=[]
for i,day in enumerate(week):
    if(day=='Sabado' or day=='Domingo'):
        weekend.append(i)
print(weekend)

#Third way to do it
week=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
weekend=[]
for i,day in enumerate(week):
    if i in [5,6]:
        weekend.append(i)
print(weekend)

#Single Line of Code First Way
print([week.index('Sabado'),week.index('Domingo')])

#Single Line of Code Second Way
print([i for i,day in enumerate(week) if day in ['Sabado','Domingo']])