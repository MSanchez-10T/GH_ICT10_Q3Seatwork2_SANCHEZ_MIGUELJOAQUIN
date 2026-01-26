#  Coding a Intramural Team Checker 
from pyscript import display, document # type:ignore

radio1 = document.querySelector('input[name="Yes"]:checked').value
radio2 = document.querySelector('input[name="Yes1"]:checked').value
selecter1 = document.getElementbyId('Gradelvl').value
selecter2 = document.getElementbyId('Section').value

if radio1 == 'r1':
    display(f"Proceed to the next field", target='output')
elif radio1 =="r2":
    display(f"Fill out the online registration", target='output')
if radio1 == 'r3':
    display(f"Proceed to the next field", target='output')
elif radio1 =="r4":
    display(f"Please procees a medical clearence", target='output')
 
if selecter1 == '0' : 
      pass  # nothing will return because its a pass, its true but nothing will happen
elif selecter1 == '7' or selecter1 == '8' or selecter1 == '9' or selecter1 == '10' :
    display(f"Congratualtions you are part of the the RedBulldogs")

if selecter2 == '01' : 
      pass  # nothing will return because its a pass, its true but nothing will happen
elif selecter2 == 'Topaz' or selecter2 == 'Sapphire' or selecter2 == 'Ruby' or selecter2 == 'Emerald' :
    display(f"Congratualtions you are part of the the RedBulldogs")


