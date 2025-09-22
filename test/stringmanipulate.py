name = "deepAk R"
print(name.upper())
print(name.lower())
print(name.capitalize())
print("****************************************************************************************")
print("                                       sking                                       ")
#masking 

mbno="82148121857"
masked=mbno[:2]+"******"+mbno[-2:]
print(f"your masked number:{masked}") 
print("****************************************************************************************")
print("                                       tmating                                       ")

#formating of words 

moviename = "mangatha"
herocast = "Ajith kumar"
director = "venkat prabhu"
moviedescription=(f" {moviename.title()} - {herocast.title()} - {director.title()}")
print(moviedescription)
print("****************************************************************************************")
print("                                       split strip                                       ")

#cleaning split
 # printing only otp
message = "hi your otp is :2212234 , dont share to any one"
enclyp=message.split(":")[1].split(",")[0].strip()
print(enclyp)
print("****************************************************************************************")
print("                                       using if in string                                       ")

#using if in in the string 

message = "all your data is stored in 232323 number locker"
if "232323" in message:
    print("locker id is present")

print("****************************************************************************************")
