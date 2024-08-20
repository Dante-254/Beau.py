def counter():
  count = 0

  def increment():
    nonlocal count
    count = count + 1

    return count
  
  return increment


increment = counter()


print(increment())
print(increment())
print(increment())