# 02_Problem

# Write a program to fill in a letter template given below with name and date.
# letter = ''' Dear <|Name|>,
# You are selected!
# <|Date|

letter = ''' Dear  <|Name|>,
 You are selected!
 <|Date|> '''

print(letter)
print(letter.replace("|Name|", "Asfand") .replace ("|Date|","25 August 2024")) # REPLACE FUNCTION chaining