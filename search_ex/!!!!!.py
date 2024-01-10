# N=int(input())
N_list=[4,1,5,2,3]
# M=int(input())
M_list=[1,3,7,9,5]

N_list.sort() #리스트 오름차순

def binary_search(N_list,n):
  left=0
  right=len(N_list)-1

  while left <= right:
    mid=int((left+right)//2)
    if N_list[mid]==n:
      return 1
    else:
      if n<N_list[mid]:
        right=mid-1
      else:
        left=mid+1
  return 0

print(binary_search(N_list,5))

for i in M_list:
  print(binary_search(N_list,i))