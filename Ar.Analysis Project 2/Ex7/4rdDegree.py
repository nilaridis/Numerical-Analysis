import numpy as np 

def PALU(A,b):
    n = len(A)
    U = A
    L = np.identity(n)


    # LU αναλυση
    for i in range(n-1):
        for j in range(n):
            if j>i:
                L[j][i]=U[j][i]/U[i][i]
                for z in range(n):
                    U[j][z]-= L[j][i]*U[i][z]

    y = np.zeros(n)
    for i in range(n):
        Sum=0
        for j in range(n):
            if(i!=j):
                Sum += L[i,j]*y[j]
        y[i]=(b[i]-Sum)/L[i][i]

    #Backward substitution Ux= y
    x = np.zeros(n)
    for i in range(n-1,-1,-1):
        Sum=0
        for j in range(n):
            if(i!=j):
                Sum+= U[i][j]*x[j]
        x[i]=(y[i]-Sum)/U[i][i]

    return x


dates = np.array([10,11,12,13,14,15,16,17,18,19])
BTC = np.array([27391.02 , 26873.32, 26756.80, 26862.38, 26861.71, 27159.65, 28519.47, 28415.75, 28328.34, 28719.81])
SOL = np.array([22.11, 22.01, 21.30, 21.83, 22.01, 21.92, 23.98, 23.96, 23.43, 24.94])

n = len(dates)

xBTC = np.zeros((n,5))
xSOL = np.zeros((n,5))
for i in range(n):
    for j in range(5):
        xBTC[i][j]= dates[i] ** j
        xSOL[i][j]= dates[i] ** j



# Calculate the Transposed Array 
BTC_T = np.zeros((5,n))
SOL_T = np.zeros((5,n))
for i in range(5):
    for j in range(n):
        BTC_T[i][j] = xBTC[j][i]
        SOL_T[i][j] = xSOL[j][i]


# Multiply xBTC with Transposed xBTC 
xBTC_BTCT = np.zeros((5,5))
xSOL_SOLT = np.zeros((5,5))
for i in range(5):
    for j in range(5):
        for k in range(n):
            xBTC_BTCT[i][j] += BTC_T[i][k] * xBTC[k][j]
            xSOL_SOLT[i][j] += SOL_T[i][k] * xSOL[k][j]

#Multiply xBTC with BTC 
BTCT_BTC = np.zeros((5))
SOLT_SOL = np.zeros((5))

for i in range(5):
    for j in range(n):
        BTCT_BTC[i] += BTC_T[i][j] * BTC[j]
        SOLT_SOL[i] += SOL_T[i][j] * SOL[j]

palu_BTC = PALU(xBTC_BTCT,BTCT_BTC)
palu_SOL = PALU(xSOL_SOLT,SOLT_SOL)


a = palu_BTC[0]
b = palu_BTC[1]
c = palu_BTC[2]
d = palu_BTC[3]
e = palu_BTC[4]

closeBTC21 = a + b*21 + c*(21**2) + d*(21**3) + e*(21**4)
print(f"Closing Price of BTC on 21/10/2023 : {closeBTC21:.2f} USD, Actual prize: 29,918.41")
closeBTC22 = a + b*22 + c*(22**2) + d*(22**3) + e*(22**4)
print(f"Closing Price of BTC on 22/10/2023 : {closeBTC22:.2f} USD, Actual prize: 29,993.90")
closeBTC23 = a + b*23 + c*(23**2) + d*(23**3) + e*(23**4)
print(f"Closing Price of BTC on 23/10/2023 : {closeBTC23:.2f} USD, Actual prize: 33,086.23")
closeBTC24 = a + b*24 + c*(24**2) + d*(24**3) + e*(24**4)
print(f"Closing Price of BTC on 24/10/2023 : {closeBTC24:.2f} USD, Actual prize: 33,901.53")
closeBTC25 = a + b*25 + c*(25**2) + d*(25**3) + e*(25**4)
print(f"Closing Price of BTC on 25/10/2023 : {closeBTC25:.2f} USD, Actual prize: 34,502.82")

print("-"*60)

a_SOL = palu_SOL[0]
b_SOL = palu_SOL[1]
c_SOL = palu_SOL[2]
d_SOL = palu_SOL[3]
e_SOL = palu_SOL[4]

closeSOL21 = a_SOL + b_SOL*21 + c_SOL*(21**2) + d_SOL*(21**3) + e_SOL*(21**4)
print(f"Closing Price of SOL on 21/10/2023 : {closeSOL21:.2f} USD, Actual prize: 29.39")
closeSOL22 = a_SOL + b_SOL*22 + c_SOL*(22**2) + d_SOL*(22**3) + e_SOL*(22**4)
print(f"Closing Price of SOL on 22/10/2023 : {closeSOL22:.2f} USD, Actual prize: 29.04")
closeSOL23 = a_SOL + b_SOL*23 + c_SOL*(23**2) + d_SOL*(23**3) + e_SOL*(23**4)
print(f"Closing Price of SOL on 23/10/2023 : {closeSOL23:.2f} USD, Actual prize: 31.85")
closeSOL24 = a_SOL + b_SOL*24 + c_SOL*(24**2) + d_SOL*(24**3) + e_SOL*(24**4)
print(f"Closing Price of SOL on 24/10/2023 : {closeSOL24:.2f} USD, Actual prize: 30.15")
closeSOL25 = a_SOL + b_SOL*25 + c_SOL*(25**2) + d_SOL*(25**3) + e_SOL*(25**4)
print(f"Closing Price of SOL on 25/10/2023 : {closeSOL25:.2f} USD, Actual prize: 32.46")