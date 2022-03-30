to_usd()

'${:,.2f}'.format






#if this code is in the global scope
#...of a file we're trying to import from
#...it will throw errors when we try to run those
price = input("Please choose a price like 4.9999")

print(to_usd(float(price)))


#nesting code in the main condition will 
#allow other scripts to cleanly 