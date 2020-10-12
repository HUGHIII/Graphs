def getval(dct):
    # itms = dct.items()
    sumlist = []

    for key in dct:
        if isinstance(dct[key],int):
            sumlist.append(dct[key])
            
    print(sum(sumlist)) 


      # google type check if int

d = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}



getval(d)