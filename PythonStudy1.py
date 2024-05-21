import random

##MY USEFUL TIPS AND STUDIES FOR PYTHON!!##

#================================
##-------LIST----------
#================================

#list to dic
names=['Name1', 'Name12','Name123','Name1234']

#get list length
length =[len(name) for name in names]
print(length)

#list to dic
length ={name: len(name) for name in names}
print(length)

#----------------------------------------
#--------------List2 removes duplicates but keep integrity

thislist =['a','b','b','c','d','e','e','f']

#this will clean but not in order as we want
#newthislist = list(set(old))
#print(newthislist)

#this s t normal way
#newthislist = []
#for item in thislist:
 #   if item not in newthislist:
  #      newthislist.append(item)

#new approach
newthislist = list(dict.fromkeys(thislist).keys())
print(newthislist)

#----------------------------------------
#find the elements that occurs most frq
xx =[random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]
maxof = max(set(xx),key=xx.count) #using SET to remove duplicateds
print("MaxofArray: ",xx)
print("Maxofrepeated: ",maxof)


#================================
##--------USER INPUT-----
#================================

user_input = input('myName: ')

#normal user code
if user_input:
    name = user_input
else:
    name = 'None'

#cleaner code
name = user_input or 'None'
print(name)

#----------------------------------------
 ##simple validation?

def dofunc_A():
     print('A')


def dofunc_B():
    print('B')

match input('Read A or B'):
    case 'A':
        dofunc_A()
    case 'B':
        dofunc_B()
    case _:
        print('Invalid func')


#----------------------------------------
#input profile update

profile ={
    'Name':'None','Date':'None','Phone':'None','email':'None'}

user_input = {
'Name':'Chirs',
'Phone':'8899393993'
}

#profile.update(user_input)
profile |= user_input #faster way

print("Profile: ",profile)

#================================
##-------SET------
#================================


#merger 2 arrays
# remove dup
# and sort the list in asc
def merge_array(arrayX,arryY):
    return sorted(set(aX+aY))
#set remove duplicates
#sorted - it

aX =[random.randrange(1,5,6)]
aY =[random.randrange(1,7,6)]
aNormal = aX+aY
aR = merge_array(aX,aY)
print(aNormal)
print("MergeArry: ",aR)


#================================
##-------DIC COMBINE------
#================================

# combine 2 dic invetory

inve = {'Pan': 1, 'Waterbt': 1 ,'Firestick': 2 }
bag ={'Cookie': 4, 'Waterbt': 3 ,'Firestick': 1,'Pan': 1 }

inv_update = {ni:inve.get(ni,0) + bag.get(ni,0)
              for ni in set(inve | bag)
              }
print("CombineDic: ",inv_update)


#----------------------------------------
#update a new item order

#rndm inv
# remove f1 and put as the last
inve2 = ['Money','Coin','Cash','Gold','Bitcoin']

indtemp = inve2.index('Money')
orderitem = inve2.pop(indtemp)
inve2.append(orderitem)
print("Update Order: ",inve2)



#================================
##-------TUPLE ------
#================================
