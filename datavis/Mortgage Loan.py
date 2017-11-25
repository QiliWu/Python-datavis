from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np

colors = [tuple(np.random.randint(0, 255, 3)/255.0) for i in range(20)]

def printHeaders(term, extra):
    print "\nExtra-Payment: $"+str(extra)+" Term:"+str(term)+" years"
    print '-'*50
    print 'Pmt no'.rjust(6), ' ', 'Beg. bal.'.ljust(13), ' ',
    print 'Payment'.ljust(9), ' ', 'Principal'.ljust(9), ' ',
    print 'Interest'.ljust(9), ' ', 'End. bal.'.ljust(13)
    print ''.rjust(6, '-'), ' ', ''.ljust(13, '-'), ' ',
    print ''.rjust(9, '-'), ' ', ''.ljust(9, '-'), ' ',
    print ''.rjust(9, '-'), ' ', ''.ljust(13, '-'), ' ',
    
def amortization_table(principal, rate, term, extrapayment, printData=False):
    xarr = []
    begarr = []
    original_loan = principal
    money_saved = 0
    total_payment  = 0
    payment = pmt(principal, rate, term)
    begBal = principal
    
    num = 1 
    endBal = 1
    if printData==True:
        printHeaders(term, extrapayment)
    while (num < term + 1) and (endBal > 0):
        interest = round(begBal * (rate / (12 * 100.0)),2)
        applied = extrapayment + round(payment-interest, 2)
        endBal = round(begBal - applied, 2)
        if (num-1)%12 == 0 or (endBal < applied+extrapayment):
            begarr.append(begBal)
            xarr.append(num/12)
            if printData == True:
                print '{:3d}'.format(num).center(6), ' ',
                print '{0:,.2f}'.format(begBal).rjust(13), ' ',
                print '{0:,.2f}'.format(payment).rjust(9), ' ',
                print '{0:,.2f}'.format(applied).rjust(9), ' ',
                print '{0:,.2f}'.format(interest).rjust(9), ' ',
                print '{0:,.2f}'.format(endBal).rjust(13)
        total_payment += applied+extrapayment
        num += 1
        begBal = endBal
    if extrapayment > 0:
        money_saved = abs(original_loan - total_payment)
        print '\nTotal Payment:', '{0:,.2f}'.format(total_payment).rjust(13)
        print ' Money Saved:', '{0:,.2f}'.format(money_saved).rjust(13)
    return xarr, begarr, '{0:,.2f}'.format(money_saved)
    
def pmt(principal, rate, term):
    ratePerTwelve = rate / (12*100.0)
    result = principal * (ratePerTwelve / (1-(1+ratePerTwelve)**(-term)))
    result = Decimal(result)
    result = round(result, 2)
    return result
    
plt.figure(figsize=(18,14))
i=0
markers = ['o', 's', 'D', '^', 'v', '*','p', 's', 'D', 'o', 's', 'D', '^', 'v', '*', 'p', 's', 'D']
markersize = [8, 8, 8, 12, 8, 8, 8, 12, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]

for extra in range(100, 1700, 100):
    xv, bv, saved = amortization_table(450000, 5, 360, extra, False)
    if extra == 0:
        plt.plot(xv, bv, color=colors[i], lw=2.2,label='Principal only', marker=markers[i], markersize=markersize[i])
    else:
        plt.plot(xv, bv, color=colors[i], lw=2.2,label='Principal plus$'+str(extra)+str('/month, Saved:\$')+saved, marker=markers[i], markersize=markersize[i])
    i += 1
plt.grid(True)
plt.xlabel('Year', fontsize=18)
plt.ylabel('Mortgage Balance', fontsize=18)
plt.title('Mortgage Loan For $350,000 With Additional Payment Chart', fontsize=20)
plt.legend()
plt.show()   
    
    