# Create a method that decrypts the duplicated-chars.txt

def decrypt(file_name):
    rf=open(file_name,"r")
    readfile=rf.read()
    s = set()
    ch_list =""
    for ch in readfile:
        if ch not in s:
            s.add(ch)
            ch_list.add(ch)
    wf=open(file_name,"w")
    writefile=wf.write(ch_list)

decrypt("doubled.txt")


