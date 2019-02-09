#Variable Length Banner challenge
name = input('Enter your username: ')
bannerstring = "**"
for x in name:
    bannerstring = bannerstring + "*"
    
print (bannerstring)
print ("* " + name+ " *")
print (bannerstring) 
