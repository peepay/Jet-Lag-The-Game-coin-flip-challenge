import random

def cointoss():
    x=None #will be used for randomly generating 0 or 1
    i=0 #count of flipping heads in a row
    j=0 #total count of flips
    while i<7:
        x=random.randint(0,1)   #generate heads or tails
        if x==0:    #if it is heads
            i+=1    #increment the count of flips in row
            j+=1    #increment the total count of flips
        elif x==1:  #if it is tails
            i=0     #reset the count of flips in row
            j+=1    #increment the total count of flips
    f.write(str(j)+"\n")    #write the number of flips to a file
    return j        #return the number of flips it took

r=0 #will be used to iterate current round number
t=int(input("Number of rounds: ")) #total rounds
c=0 #cumulative sum of flips

f=open("numbers.csv","w")   #rewrite the file
f.close()
f=open("numbers.csv","a")   #open the file so that values can be appended

while r<t:
    c+=cointoss()   #add number of flips from this round to cumulative sum
    r+=1            #increment the round number
    print(str(round(r/t*100,2))+" % ",end='\r') #print out the percentage elapsed

f.close()
a=c/r   #calculate the average number of flips
print("Seven heads in a row on average in "+str(a)+" coin tosses.")
