#text = "Cdnuolt blveiee taht I cluod aulaclty uesdnatnrd waht I was rdanieg. The phaonmneal pweor of the hmuan mnid, aoccdrnig to a rscheearch at Cmabrigde Uinervtisy, it dseno't mtaetr in waht oerdr the ltteres in a wrod are, the olny iproamtnt tihng is taht the frsit and lsat ltteer be in the rghit pclae. The rset can be a taotl mses and you can sitll raed it whotuit a pboerlm. Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe. Azanmig huh? yaeh and I awlyas tghuhot slpeling was ipmorantt!"
#Above is a passage of text without line breaks. Write a program to wrap the text at a selectable width but without splitting the letters of any word.
#Example: width = 80
#--------------------------------------------------------------------------------
#Cdnuolt blveiee taht I cluod aulaclty uesdnatnrd waht I was rdanieg. The
#phaonmneal pweor of the hmuan mnid, aoccdrnig to a rscheearch at Cmabrigde
#Uinervtisy, it dseno't mtaetr in waht oerdr the ltteres in a wrod are, the
#olny iproamtnt tihng is taht the frsit and lsat ltteer be in the rghit pclae.
#The rset can be a taotl mses and you can sitll raed it whotuit a pboerlm. Tihs
#is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod
#as a wlohe. Azanmig huh? yaeh and I awlyas tghuhot slpeling was ipmorantt!
#Example: width = 40
#----------------------------------------
#Cdnuolt blveiee taht I cluod aulaclty
#uesdnatnrd waht I was rdanieg. The
#phaonmneal pweor of the hmuan mnid,
#aoccdrnig to a rscheearch at Cmabrigde
#Uinervtisy, it dseno't mtaetr in waht
#oerdr the ltteres in a wrod are, the
#olny iproamtnt tihng is taht the frsit


text = "Cdnuolt blveiee taht I cluod aulaclty uesdnatnrd waht I was rdanieg. The phaonmneal pweor of the hmuan mnid, aoccdrnig to a rscheearch at Cmabrigde Uinervtisy, it dseno't mtaetr in waht oerdr the ltteres in a wrod are, the olny iproamtnt tihng is taht the frsit and lsat ltteer be in the rghit pclae. The rset can be a taotl mses and you can sitll raed it whotuit a pboerlm. Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe. Azanmig huh? yaeh and I awlyas tghuhot slpeling was ipmorantt!"

# Save each word in a list
lst1 = text.split()

# Prompt the user the number of width
x = int(input('Enter the width: '))

i = 0
str1 = ''
while True:
    el = lst1[i] 
    str1 = str1 + el + ' '
    i += 1
    if len(str1) % x == 0:
        str1 += '\n'
    
    if i == len(lst1):
        print(str1.rstrip())
        break
    
    
        





    
            




   
    
    

