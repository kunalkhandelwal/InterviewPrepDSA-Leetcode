#Sol 0 - beats - 45, 32
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = ""

        arr = list(map(str, nums))

        arr.sort(key = lambda x:x*10, reverse = True)

        if arr[0] == '0':
            return "0"
        
        return "".join(arr)

  EXPLANATION:
""" 
array = list(map(str, nums))
The map() function applies the str function to each element of the list nums, converting each integer to a string.
The list() function wraps the result, converting it into a list of strings.
Example: If nums = [3, 30, 34, 5, 9], after this step, array = ['3', '30', '34', '5', '9'].
3. Line 6 - Custom sorting with a lambda function:
python
Copy code
array.sort(key=lambda x: x*10, reverse=True)
The sort() function sorts the array based on a custom key.
The key=lambda x: x*10 is a custom sorting rule that multiplies the string by 10. This ensures that each string is compared as if it were repeated multiple times, which helps compare longer numbers effectively.
The reason for x*10 is that it ensures the digits of shorter strings are repeated and can be compared with longer strings.
Sorting is done in descending order (reverse=True).
Example:

Consider array = ['3', '30', '34', '5', '9'].
The lambda function will evaluate them as:
'3' * 10 = '3333333333'
'30' * 10 = '3030303030'
'34' * 10 = '3434343434'
'5' * 10 = '5555555555'
'9' * 10 = '9999999999'
Sorting them in descending order gives: ['9', '5', '34', '3', '30'].
4. Line 9 - Handle the case where the largest number is "0":
python
Copy code
if array[0] == "0":
    return "0"
After sorting, if the first element is '0', it means the entire number will be '0' (like if all elements in nums were zeros). In that case, the function returns '0' directly.
Example: If nums = [0, 0], after sorting, array = ['0', '0'], so the function would return '0'.
5. Line 12 - Build the largest number:
python
Copy code
largest = ''.join(array)
The ''.join(array) concatenates the sorted strings in array into a single string, which represents the largest possible number.
Example: If array = ['9', '5', '34', '3', '30'], then largest = '9534330'.
"""
