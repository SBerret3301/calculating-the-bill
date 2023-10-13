x = int(input("enter the number of copies : "))
if x <= 10 :
    print ("the price is : " , x * 0.30 , "DH" )
elif x > 10 and x <= 30 :
    print ( "the price is: " , 10 * 0.30 + (x - 10) * 0.25 , "DH" )
elif x > 30 :
    print ("the price is : " , 10 * 0.30 + 20 * 0.25 + (x-30) * 0.20 , "DH")
else :
    print ("enter corectly the number")