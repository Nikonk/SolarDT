def outCapacity(Ia, n, A, kl):
    Ppv = Ia * n/100 * A * kl
    return (Ppv)

def KPD(nConst, B, Tpv):
    n = nConst * (1 - B*(Tpv - 48))
    return (n)

def workTempFoto(Ta, Ia, Vw):
    k0 = 30.02
    k1 = 6.28
    Tpv = Ta + Ia / (k0 + k1 * Vw)
    return Tpv

def photoCurrent(Ia, Isc, Tpv, k1):
    Iph = Ia / 1000 * (Isc + k1*(Tpv - 25))
    return Iph

def outVoltage(Ppv, Iph):
    Upv = Ppv / Iph
    return Upv