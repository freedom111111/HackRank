def rotations(arr):
  res = 0

  for i in range(len(arr)-1):
      if arr[i] & 1:
          arr[i+1] += 1
          res += 2
  if arr[-1] & 1:
      print('NO')
  else:
      print(res)
