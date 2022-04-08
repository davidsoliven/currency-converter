"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: David Soliven
Date:   4/5/2022
"""
import introcs
import currency


src = input('3-letter code for original currency: ')
print(src) 
assert currency.iscurrency(src) == True

dst = input('3-letter code for the new currency: ')
print(dst)
assert currency.iscurrency(dst) == True

amt = input('Amount of the original currency: ')
print(amt)
assert introcs.isfloat(amt) or introcs.isint(amt)

currency_to = currency.exchange(src,dst,amt)

print(f"You can exchange {amt} {src} for {round(currency_to, 3)} {dst}.")

