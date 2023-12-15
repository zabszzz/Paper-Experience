
#num = 0
#value = 8.80024376 * 10**30 vem de 9,3016*10^9*461*10^12*10^6=0,1*2^(n-1); n= num
#while 2**num < value and 2**num+1 < value:
    #num += 1
#print(num)
#print(2**103)
#if(2**104>value):
    #print("abacate")

value1 = 630/2**102
value2 = 630/2**103
h = 6.626 * 10**-34
G = 6.674 * 10**-11
c = (3 * 10**8)
lp = (h*G/c**3)**0.5#formula do comprimento de um planck
print(lp/value1, "102")#aqui confirma que é possivel fazer esse experimento
print(lp/value2, "103")#aqui confirma que é possivel fazer esse experimento
print(value1,"ola")
print(value2,"mundo")
print(lp,"bunda")
#da para diminuir ainda mais a área
