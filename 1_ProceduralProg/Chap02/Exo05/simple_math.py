fnum = input('What is the first number? ') 
snum = input('What is the second number? ')

fnum = int(fnum)
snum = int(snum)

print(f"""{fnum} + {snum} = {fnum+snum}
{fnum} - {snum} = {fnum-snum}
{fnum} * {snum} = {fnum*snum}
{fnum} / {snum} = {fnum/snum:.2f}
""")