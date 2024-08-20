def hello(name, age, value):
  print('Hello '+name+' you are ' +str(age)+' of value '+str(value))
  value = 28
  print('Hey '+name+' '+str(value))

  print(age.bit_length())
  print(value.bit_length())

  views={
    'id':'1',
    'name':'Dante',
    'date of birth':'22-feb-02'
  }

  

  return name, id(name), id(age), id(views)

print(hello('Manoti', 22 , 44))
