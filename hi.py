import time 
import os
# exactly as how it looks
frameList = [
'''
   O                  O
   |>   .             |
  / \\                / \\
  ''','''
   O                  O
   |>      .          |
  / \\                / \\
  ''','''
   O                  O
   |>           .     |
  / \\                / \\
  ''','''
   O                  O
   |>                .|
  / \\                / \\
  ''','''
   O                    O
   |>                  /
  / \\                 /\\
  ''','''
   O   
   |>                    >--O 
  / \\                  
  ''','''
   O                    
   |>                  
  / \\                   >--O    
  ''','''
   O                    
  <|                  
  / \\                   >--O 
  ''','''
  O                    
 <|                  
 / \\                    >--O
 ''','''
O                    
|                 
 \\                      >--O
 '''

]
while True:
	for frame in frameList:
		os.system("cls")
		print(frame)
		time.sleep(.2)