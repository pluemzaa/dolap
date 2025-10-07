# Dog => 4
# Cat => 3.5
# Fish => 3
Enteryourpet_num = {"Dog":[1,0,0], "Cat":[0,1,0], "Fish":[0,0,1], "Dog" : [1,0,0], "Cat" : [0,1,0]}
Enteryourpet_text = "Dog,Cat,Fish"
#4,4,3.5,0
E = Enteryourpet_text.split(",")
print(E)
print("Result",end=' ')
print(Enteryourpet_num[E[0]],",",Enteryourpet_num[E[1]],",",Enteryourpet_num[E[2]],",",Enteryourpet_num[E[3]],",",Enteryourpet_num[E[4]],sep='')