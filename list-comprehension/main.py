if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
results = [ [i,j,k] for i in range (x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != n] 

print (results)