
print('''
  ###                                                                              ####     ####   
   ##                                                                             ##  ##   ##  ##  
   ##      ####     ####    ######            ##  ##    ####     ####    ######       ##       ##  
   ##     ##  ##       ##    ##  ##           ##  ##   ##  ##       ##    ##  ##     ##       ##   
   ##     ######    #####    ##  ##           ##  ##   ######    #####    ##        ##       ##    
   ##     ##       ##  ##    #####             #####   ##       ##  ##    ##                       
  ####     #####    #####    ##                   ##    #####    #####   ####       ##       ##    
                            ####              #####                                                


''')
print("\nWelcome to the best programme of checking whether the year is leap or not")
print("\nTHIS PROGRAMME WAS MADE BY THE BEST PROGRAMMER EVER ===> @mustafa_alhoz ")
year = int(input("\nEnter the year you want to learn if it is leap or not: "))
if year%4==0:
  if year%100==0:
    if year%400==0:
      print("\nit is a Leap year\n")
    else:
      print("\nit is Not a leap year\n")
  else:
    print("\nit is a Leap year\n")
else:
  print("\nit is Not leap year\n")
  