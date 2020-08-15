def Replace(str1):
	length=len(str1)
	str2=" "
	for i in range(0,length):
		ch=str1[i]
		if (ch not in str2[:i]):
			str2=str2+ch
		else:
			str2=str2+"*"
	return str2

def main():
	str1=input("INPUT A STRING: ")
	result=Replace(str1)
	print("ORIGINAL" , str1)
	print(" MODIFIED ",result)

if __name__=="__main__":
	main()
			
			
