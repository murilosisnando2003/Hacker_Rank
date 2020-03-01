if __name__ == '__main__':
    test=int(input())
    if 1<=test and test <=10:
	    for i in range(test):
		    palabra=str(input())
        #palabra means word in spanish, sorry :P
		    if 2 <= len(palabra) and len(palabra) <= 10000:
			    print(palabra[::2], palabra[1::2])
    else:
	    print("Error")