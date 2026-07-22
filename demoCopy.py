import copy
original = [1, 2, [3, 4]]
#浅拷贝：复制容器 内部对象引用—内部对象是公用
shallow = original.copy()  # or copy.copy(original) 

#深拷贝：递归复制所有内部对象，完全独立
deep = copy.deepcopy(original)

original[2][0] = 'X'
print("Original:", original)  # Output: Original: [1, 2, ['X', 4]]
print("Shallow Copy:", shallow)  # Output: Shallow Copy: [1, 2, ['X', 4]]
print("Deep Copy:", deep)  # Output: Deep Copy: [1, 2, [3, 4]]




