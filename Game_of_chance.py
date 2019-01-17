#!/usr/bin/env python2
import sys;
import random;
def select_1(mode):
    total=0;
    expected_value=0.0;
    for x in range(1,7):
        nodes.append([]);
        if(mode=='a'):
            node_to_append=str(x)+str(b)+str(c);
        elif(mode=='b'):
            node_to_append=str(a)+str(x)+str(c);
        elif(mode=='c'):
            node_to_append=str(a)+str(b)+str(x);
        if(node_to_append[0]==node_to_append[1]==node_to_append[2]):
            expected_value=float(25)/6;
        else:
            expected_value=float((int(node_to_append[0])+int(node_to_append[1])+int(node_to_append[2])))/6;
        nodes[len(nodes)-1].append(node_to_append);
        nodes[len(nodes)-1].append(expected_value);
        nodes[len(nodes)-1].append(mode);
        total=total+expected_value;
    ans.append([]);
    ans[len(ans)-1].append(total);
    ans[len(ans) - 1].append(mode);
def select_2(mode):
    expected_value=0.0;
    total=0;
    for x in range(1,7):
        for y in range(1,7):
            nodes.append([]);
            if(mode=='ab'):
                node_to_append=str(x)+str(y)+str(c)
            elif(mode=='bc'):
                node_to_append = str(a) + str(x) + str(y)
            elif(mode=='ac'):
                node_to_append = str(x) + str(b) + str(y)
            if (node_to_append[0] == node_to_append[1] == node_to_append[2]):
                expected_value = float(25) / 36;
            else:
                expected_value = float((int(node_to_append[0]) + int(node_to_append[1]) + int(node_to_append[2]))) / 36;
            nodes[len(nodes)-1].append(node_to_append);
            nodes[len(nodes)-1].append(expected_value);
            nodes[len(nodes)-1].append(mode)
            total=total+expected_value;
    ans.append([]);
    ans[len(ans) - 1].append(total);
    ans[len(ans) - 1].append(mode);
def select_3(mode):
    #for rerolling 3 dice the expected value is always going to be 10.92
    ans.append([]);
    ans[len(ans) - 1].append(10.92);
    ans[len(ans) - 1].append(mode);
ans=[];
nodes=[];
print("Enter Your Input");
ip=input();
print ip;
a,b,c=str(ip);
a=int(a);
b=int(b);
c=int(c);
select_1('a');
select_1('b');
select_1('c');
select_2('ab');
select_2('ac');
select_2('bc');
select_3('abc');
if(a==b==c):
    print("Roll None of the dice")
    sys.exit(1);
max=0;
for x in ans:
    if(x[0]>(a+b+c) and x[0]>max):
        max=x[0];
        ans=x[1];
if(max!=0):
    print("Roll Dice: %s " % ans);
else:
    print("Roll None of the dice")
