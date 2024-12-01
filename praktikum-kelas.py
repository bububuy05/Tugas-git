#Diberikan sebuah array bilangan bulat nums, urutkan array tersebut dalam urutan naik dan kembalikan hasilnya.
#Contoh 1:
#Input: nums = [5,2,3,1]
#Output: [1,2,3,5]
#Penjelasan: Setelah array diurutkan, posisi beberapa angka tidak berubah (misalnya, 2 dan 3), 
#sedangkan posisi angka lainnya berubah (misalnya, 1 dan 5).
#Gunakan  function,loop, if
def bubble_sort(nums):
  n = len(nums)
  for i in range(n):
    for j in range(0, n-i-1):
      if nums[j] > nums[j+1] :
        nums[j], nums[j+1] = nums[j+1], nums[j]
  return nums
nums = [5, 2, 3, 1]
sorted_nums = bubble_sort(nums)
print(sorted_nums)