import string
import random
#switch will be defined
def switch1(list):
    f = open("switch1.txt", "a")#open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\switch1.txt')]
    flag=0#initially check:
    flag1=0
    for j in lines:
        str1 = j.split()# so create list of words
        if (list[0] in str1):  # in case host is present in file
            #print(list[0] + 'is found')
            flag=flag+1#increment flag by one
        if(list[2] in str1):
            print("Destination found")
            flag1=1
            cpy=str1[1]
    if(flag==0):#host will be updated
        f.write(list[0]+" "+list[3]+"\n")#switch for corresponding host
        f.close()
    if(flag1==1):#so we have what port it is at
        if(cpy=='0'):
            list[3]='1'
            switch4(list)
        if(cpy=='3'):
            list[3]=='2'
            switch2(list)
        if(cpy=='1' or cpy=='2'):
            print("message: "+list[1]+" reieved at "+list[2])#message received at destination
    else:#that is, we need to broadcast.
        for i in S1:
            if(i[0]!='s' and i!=list[0]):#dont send message broadcast at host please
                print("message broadcasted at "+i)
        if(list[3]=='0'):
            list[3]='2'
            switch2(list)
        else:
            if(list[3]=='3'):
                list[3]='1'
                switch4(list)
            elif(list[3]=='1' or list[3]=='2'):
                list[3] = '1'
                switch4(list)
                list[3] = '2'
                switch2(list)
def switch2(list):
    f = open("switch2.txt", "a")  # open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in
             open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\switch2.txt')]
    flag = 0  # initially check:
    flag1 = 0
    for j in lines:
        str1 = j.split()  # so create list of words
        if (list[0] in str1):  # in case host is present in file
            #print(list[0] + 'is found')
            flag = flag + 1  # increment flag by one
        if (list[2] in str1):
            print("Destination found")
            flag1 = 1
            cpy = str1[1]
    if (flag == 0):  # host will be updated
        f.write(list[0] + " " + list[3]+"\n")  # port for corresponding host
        f.close()
    if (flag1 == 1):  # so we have what port it is at
        if (cpy == '2'):
            list[3] = '3'#update port and send
            switch1(list)
        if (cpy == '1'):
            list[3] == '0'#update port for it and send
            switch3(list)
        if (cpy == '3'):
            print("message: " + list[1] + " reieved at " + list[2])  # message received at destination
    else:  # that is, we need to broadcast.
        for i in S2:
            if (i[0] != 's' and i != list[0]):  # dont send message broadcast at host please
                print("message broadcasted at " + i)
        if(list[3]=='2'):
            list[3] = '0'
            switch3(list)
        else:
            if(list[3] =='1'):
                list[3]='3'
                switch1(list)
            elif(list[3]=='3'):
                list[3] = '0'
                switch3(list)
                list[3] = '3'
                switch1(list)

def switch3(list):
    f = open("switch3.txt", "a")  # open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in
             open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\switch3.txt')]
    flag = 0  # initially check:
    flag1 = 0
    for j in lines:
        str1 = j.split()  # so create list of words
        if (list[0] in str1):  # in case host is present in file
            #print(list[0] + 'is found')
            flag = flag + 1  # increment flag by one
        if (list[2] in str1):
            print("Destination found")
            flag1 = 1
            cpy = str1[1]
    if (flag == 0):  # host will be updated
        f.write(list[0] + " " + list[3]+"\n")  # port for corresponding host
        f.close()
    if (flag1 == 1):  # so we have what port it is at
        if (cpy == '0'):
            list[3] = '1'  # update port and send
            switch2(list)
        if (cpy == '3' or cpy=='1'):
            print("message: " + list[1] + " reieved at " + list[2])  # message received at destination
    else:  # that is, we need to broadcast.
        for i in S3:
            if (i[0] != 's' and i!= list[0]):  # dont send message broadcast at host please
                print("message broadcasted at " + i)
        if(list[3]=='1'):
            switch2(list)
        else:
            if(list[3]=='3'):
                list[3]='1';
                switch2(list)

def switch4(list):
    f = open("switch4.txt", "a")  # open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in
             open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\switch4.txt')]
    flag = 0  # initially check:
    flag1 = 0
    for j in lines:
        str1 = j.split()  # so create list of words
        if (list[0] in str1):  # in case host is present in file
            #print(list[0] + 'is found')
            flag = flag + 1  # increment flag by one
        if (list[2] in str1):
            print("Destination found")
            flag1 = 1
            cpy = str1[1]
    if (flag == 0):  # host will be updated
        f.write(list[0] + " " + list[3]+"\n")  # port for corresponding host
        f.close()
    if (flag1 == 1):  # so we have what port it is at
        if (cpy == '1'):
            list[3] = '0'  # update port and send
            switch1(list)
        if(cpy == '3'):
            list[3]='2'
            switch5(list)
        if (cpy == '2' or cpy == '0'):
            print("message: " + list[1] + " reieved at " + list[2])  # message received at destination
    else:  # that is, we need to broadcast.
        for i in S4:
            if (i[0] != 's' and i != list[0]):  # dont send message broadcast at host please
                print("message broadcasted at " + i)
        if(list[3]=='1'):
            list[3] = '2'
            switch5(list)
        else:
            k=0
            if(list[3]=='3'):
                list[3] = '0'
                switch1(list)
            else:
                if(list[3]=='2'):
                    k=k+1
                    list[3] = '2'
                    switch5(list)
                    if(k>0):
                        list[3] = '0'
                        switch1(list)
                elif(list[3]=='2'):
                    list[3] = '2'
                    switch5(list)
                    if (k > 0):
                        list[3] = '0'
                        switch1(list)

def switch5(list):
    f = open("switch5.txt", "a")  # open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in
             open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\switch5.txt')]
    flag = 0  # initially check:
    flag1 = 0
    for j in lines:
        str1 = j.split()  # so create list of words
        if (list[0] in str1):  # in case host is present in file
            #print(list[0] + 'is found')
            flag = flag + 1  # increment flag by one
        if (list[2] in str1):
            print("Destination found")
            flag1 = 1
            cpy = str1[1]
    if (flag == 0):  # host will be updated
        f.write(list[0] + " " + list[3]+"\n")  # port for corresponding host
        f.close()
    if (flag1 == 1):  # so we have what port it is at
        if (cpy == '2'):
            list[3] = '3'  # update port and send
            switch4(list)
        if (cpy == '3' or cpy == '0'):
            print("message: " + list[1] + " reieved at " + list[2])  # message received at destination
    else:  # that is, we need to broadcast.
        for i in S5:
            if (i[0] != 's' and i != list[0]):  # dont send message broadcast at host please
                print("message broadcasted at " + i)
        if (list[3] == '0'):#that is, we have messafe from H8 then
            list[3] = '3'
            switch4(list)
        else:
            if(list[3]=='3'):
                switch4(list)
#host methods are defined
def host1(list):
    list.append('2');
    switch1(list)
def host2(list):
    list.append('1');
    switch1(list)
def host3(list):
    list.append('2');
    switch4(list)
def host4(list):
    list.append('0');
    switch4(list)
def host5(list):
    list.append('1');
    switch3(list)
def host6(list):
    list.append('3');
    switch3(list)
def host7(list):
    list.append('3');
    switch2(list)
def host8(list):
    list.append('0');
    switch5(list)
def host9(list):
    list.append('3');
    switch5(list)
#Define MAC Adress
def macgen():
    lst = [random.choice(string.hexdigits) for n in range(12)]
    str = "".join(lst)
    str=str[:2]+":"+str[2:4]+":"+str[4:6]+":"+str[6:8]+":"+str[8:10]+":"+str[10:12]
    return(str);
#Create Hosts and swithces
H1=macgen()
H2=macgen()
H3=macgen()
H4=macgen()
H5=macgen()
H6=macgen()
H7=macgen()
H8=macgen()
H9=macgen()
H=['H1','H2','H3','H4','H5','H6','H7','H8','H9']
print(H)
S1=['H1','H2','switch2','switch4']#list of strings associated to switch 1
S2=['switch1','H7','switch3']#list of strings associated to switch 2
S3=['H5','H6','switch2']
S4=['switch1','H3','H4','switch5']
S5=['H8','H9','switch4']
ctr=0
i=0
while ctr==0:
    i=int(input('Enter 1 if you want to send a message, else press 0 to exit program:'))
    if(i!=0):
        ssrc = input('Enter the sender host number:')
        msg = input('Enter the message:')
        dsrc = input('Enter the destination host number:')
        list=[ssrc,msg,dsrc]#mac address and message is sent
        if(ssrc in H):
            j=H.index(ssrc)#where the host number matches in the list
            if(j==0):
                host1(list);
            if(j==1):
                host2(list);
            if(j==2):
                host3(list);
            if(j==3):
                host4(list);
            if(j==4):
                host5(list);
            if(j==5):
                host6(list);
            if(j==6):
                host7(list);
            if(j==7):
                host8(list);
            if(j==8):
                host9(list);
    else:
        ctr=ctr+1# break out of the while loop.