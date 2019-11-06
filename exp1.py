def CheckCochannel(a,b,c,i,j):
    eCheck = a-2
    if(eCheck <= 0):
        eCheck += 6
    
    if(a==1 or a==4):        
        lCheck = 1+j

        if(eCheck == b and lCheck == c):
            return True
        else:
            return False

    elif(a==2 or a==5):
        lCheck = i+j+1

        if(eCheck == b and lCheck == c):
            return True
        else:
            return False
    else:
        lCheck = 1+i

        if(eCheck == b and lCheck == c):
            return True
        else:
            return False

print("Welcome To the Co-Channel guessing game\n")
z = input("Enter to continue........")

i = int(input("\nEnter The i value :"))
j = int(input("Enter The j value :"))

N = i**2 + i*j + j**2

print("\nThe Value of generated N: "+str(N)+"\n")

z = input("Enter to continue........")

print("\n     *   ")
print("  (3) (2)")
print("  *     *")
print(" (4)   (1)")
print("  *     *")
print("  (5) (6)")
print("     *   ")

print("\nInstruction : \n1: Consider The above diagram where * denotes Vertex and () denotes edge number")
print("2: For guessing the cell use the edge number for it")
print("3: Guessing a cell will require 3 inputs \n   a:Starting Edge number \n   b:Which edge the destination cell reached\n   b:Which layer is the cell present")
print("4: Every right ans gives +1 and wrong ans -1 point")
print("5: On Reaching  score=3 you win and on going below 0 you lose")
print("\n^-^    Thats all    ^-^")


score,right,wrong = 0,0,0
arr = []

print("\n Let the game begin | Current Score '0' \n\n")

while(score>=0 and score<3):

    a,b,c = map(int , input("Enter the guessing value in 3 digits:").split())
    val = a*b*c

    if(val in arr):
        print("No same answers are accepted!!")
        print("Enter the value again!!")
        continue

    if(CheckCochannel(a,b,c,i,j)):
        score += 1
        right += 1
        arr.append(val)
        print("Correct !!!!!\nCurrent Score:"+str(score))
    else:
        score -= 1
        wrong += 1
        print("Wrong !!!!!!\nCurrent Score:"+str(score))

if(score == 3):
    print("Congratualions you won !!")
    print("Right:  "+str(right)+" Wrong: "+str(wrong))
else:
    print("Go study and come again !!")        
    print("Right:  "+str(right)+" Wrong: "+str(wrong))

