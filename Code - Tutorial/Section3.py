windows_serial_number="abc-def-ghi-jkl"
print(windows_serial_number)

new_a=windows_serial_number[0:3]
new_b=windows_serial_number[4:7]
new_c=windows_serial_number[8:11]
new_d=windows_serial_number[12:15]
print(new_a)
print(new_b)
print(new_c)
print(new_d)

new_var_a = new_a.replace("abc","aaa")
new_var_b = new_b.replace("def","bbb")
new_var_c = new_c.replace("ghi","ccc")
new_var_d = new_d.replace("jkl","ddd")
print(new_var_a)
print(new_var_b)
print(new_var_c)
print(new_var_d)

encoded_windows_serial_number= new_var_a+"-"+new_var_b+"-"+new_var_c+"-"+new_var_d
print("this is the encoded serial number :"+encoded_windows_serial_number)