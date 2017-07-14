
# function used to calculate the total pay    
def computePay(hours, rate, overtimeRate):     
    # if hours is greater than 40, the overtime pay must be calculated 
    if hours > 40:
        overtimeHours = hours - 40
        overtimePay = overtimeHours * rate * overtimeRate
        pay = overtimePay + 40 * rate         
    # else just calculate the pay without overtime 
    else:
        pay = hours * rate         
    return pay
  
  
stage = 0    # variable to store the stage of the loop that the user is at

# continue looping until all stages have been completed
while stage < 5:     
    # stage 1 - employee name
    if stage == 0:
        name = raw_input('Enter Employee Name: ')        
        # check that name is not too short
        if len(name) < 2:
            print 'Name must contain two or more characters'
            continue 
    # stage 2 - hours 
    elif stage == 1:
        s_hours = raw_input('Enter hours worked: ')        
        # try to cast hours to floating number. If input is invalid, continue 
        # looping in the current iteration
        try:
            hours = float(s_hours)
        except:
            print 'Please enter a numeric value'
            continue            
    # stage 3 - hourly rate 
    elif stage == 2:
        s_rate = raw_input('Enter hourly rate: ')        
        # try to cast string hourly rate to floating number. If input is invalid, 
        # continue looping in the current iteration
        try:
            rate = float(s_rate)
        except:
            print 'Please enter a numeric value'
            continue            
    # stage 4 - overtime rate 
    elif stage == 3:
        s_overtimeRate = raw_input('Enter overtime rate: ')      
        # try to cast string input overtime rate to floating number. If input is invalid,
        # continue looping in the current iteration 
        try:
            overtimeRate = float(s_overtimeRate)
        except:
            print 'Please enter a numeric value'
            continue
    # stage 5 - tax rate 
    elif stage == 4:
        s_taxRate = raw_input('Enter tax rate: ')           
        # try to cast string input tax rate to floating number. If input is invalid, 
        # continue looping in the current iteration 
        try:
            taxRate = float(s_taxRate)
        except:
            print 'Please enter a numeric value'
            continue  
    stage = stage + 1

# executes only when user has finished entering their details
if stage == 5:
    # gross pay is calculated by calling the computePay function 
    grossPay = computePay(hours, rate, overtimeRate)
    # tax deductions are calculated by multiplying gross pay by tax rate, then dividing by 100
    taxDed = (grossPay * taxRate)/100
    netPay = grossPay - taxDed
    # tax deductions and net pay are rounded to two decimal places
    taxDed = round(taxDed, 2)
    netPay = round(netPay, 2) 
 
    print 'Employee Name: %s' % name 
    print 'Gross Pay: %g' % grossPay
    print 'Tax Deductions %g' % taxDed
    print 'Net Pay: %g' % netPay