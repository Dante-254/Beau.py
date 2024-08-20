rm107 = ['Liz Sheila', 'Karen', 'Mimi', 'V.Venom', 'Susan']

print('Mimi' in rm107)

rm107.append('Carol')
print(rm107)
rm107.extend(['Sheryl', 'Ashley'])
print(rm107)
rm107+=['raechel']
print(rm107)
rm107.sort(key=str.lower)
print(rm107)

