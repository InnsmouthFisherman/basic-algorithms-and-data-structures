def merge_sort(nums):
	if len(nums) > 1:
		
		# разделение списка на две части 
		mid = len(nums) // 2
		left = nums[:mid]
		right = nums[mid:]
		
		merge_sort(left)
		merge_sort(right)
		
		# i - позиция в левой половине j - позиция в правой половине 
		# k - позиция в исходном массиве
		i = j = k = 0
		
		# каждый элемент двух половин массива сранивается с элементом 
		# из другой половины: если левое число больше, оно помещается 
		# в nums на позицию k, i увеличивается на 1
		# в противном случае j увеличивается на 1
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				nums[k] = left[i]
				i += 1
			else:
				nums[k] = right[j]
				j += 1
			k += 1
		
		# сортировка оставшиъся элементов 
		
		while i < len(left):
			nums[k] = left[i]
			i += 1
			k += 1
			
		while j < len(right):
			nums[k] = right[j]
			j += 1
			k += 1
			
		return nums 
		

print(merge_sort([2,15,23,3,3,7]))
