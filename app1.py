import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def get_transalation(w):
    makeword_in_lower= w.lower()
    if w in data:
        result = data[makeword_in_lower]
        return result   
    elif len(get_close_matches(w, data.keys())) > 0:
       confirmation =  input("Did you mean %s instead if Yes press y if no press n :  " % get_close_matches(w, data.keys()) [0])
       if confirmation == 'y':
           return  data[get_close_matches(w, data.keys()) [0]]
       elif confirmation== 'n':
           return "\n\n Sorry ! the word isn't found in the dictionary\n"
       else:
           return "\n\n We didn't understand your query\n"

          
    else:
        return "\n\n The word isn't found in the dictionary\n"
        


while True:
    user_input = input("Enter Word  : ")
    if  user_input == "\end":
        break
    else:
        output = get_transalation(user_input)
        if type(output) == list:
            i = 1
            for temp in output:
                print(i,".",temp)
                i=i+1        
        else:
            print(output)
            
            
        
             

