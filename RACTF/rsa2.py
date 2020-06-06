import math
def getModInverse(a, m):
	if math.gcd(a, m) != 1:
		return None
	u1, u2, u3 = 1, 0, a
	v1, v2, v3 = 0, 1, m

	while v3 != 0:
		q = u3 // v3
		v1, v2, v3, u1, u2, u3 = (
			u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
	return u1 % m

n = 223922008395000014283723882760043013065620539801942997270066014714444427363520046178491495846777410229650596356717074951108688822198285613233594532478253401
e = 65537
c = 46927100178484164054422389460642412566557695583199776470820879720759927161614477494084640525145368116489400445149854096703153163465010997139019479726766394

p = 17
q = 13171882846764706722571993103531941945036502341290764545298000865555554550795296834028911520398671189979446844512769114771099342482252094896093796028132553


phi = (p-1)*(q-1)

d = getModInverse(e, phi)

plaintext = pow(c,d,n)

print(plaintext)