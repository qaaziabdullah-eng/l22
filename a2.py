#arrays
import array as arr
a= arr.array('i',[12,34,56,23,12,78,45])
print("array: "+str(a))
print("number of occurrence(num:12): "+str(a.count(12)))
a.reverse()
print("reverse array:", str(a))
