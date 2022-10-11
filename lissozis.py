"""
key string value int şeklinde verilen karışık sözlğü sıralamak için yazılmıştır.
"""


def shower(pbd): #key kelime value rakam olan bir değer veriyorsun sana azalan sırada sonucu veriyor.
    
    maxindict={}
    maxindictlast={}
    dictvalues = sorted(pbd.values())
    uniqueval=[]
    equity_flag=False



    for slo in dictvalues:
        if slo not in uniqueval:
            uniqueval.append(slo)

    suniqueval=sorted(uniqueval)

    for sloo in uniqueval:
        counter=dictvalues.count(sloo)
        if counter >= 2:
            equity_flag=True

    if equity_flag == False:
        for slooo in dictvalues:
            for sloooo in pbd.keys():
                if pbd[sloooo] == slooo:
                    maxindict[sloooo] = slooo
    else:
        for mlo in suniqueval:
            counter=dictvalues.count(mlo)
            if counter > 1 :
                be=[]
                for mloo in pbd.keys():
                    if pbd[mloo] == mlo and mloo not in be :
                        be.append(mloo)
                for k in range(len(be)):
                    maxindict[be[k-1]]=mlo
                be=[]

            else:
                for mlooo in pbd.keys():
                    if pbd[mlooo] == mlo:
                        maxindict[mlooo] = mlo

    reversekey=[]
    for to in maxindict.keys():
        reversekey.append(to)

    reversekey.reverse()
    for too in reversekey:
        maxindictlast[too]=maxindict[too]

    return maxindictlast

def wordcountinlis(genelliste):
    sozsay={}
    liste2 = []
    liste2 = set(genelliste)
    for eleman in liste2:
        count = 0
        while eleman in genelliste:
            genelliste.remove(eleman)
            count += 1
        sozsay[eleman] = count
    return sozsay


def reverse_dictionary(takedc):
    lst_keys=[]
    lst_vals=[]
    for lo in takedc.keys():
        lst_keys.append(lo)
        lst_vals.append(takedc[lo])
    lst_keys.reverse()
    lst_vals.reverse()
    reversed_dict={}
    for ro,roo in zip(lst_keys,lst_vals):
        reversed_dict[ro]=roo

    return reversed_dict