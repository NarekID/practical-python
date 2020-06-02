# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000
month_counter = 0

while principal > 0:
    month_counter += 1
    if month_counter == extra_payment_start_month:
        payment += extra_payment
    elif month_counter == extra_payment_end_month + 1:
        payment -= extra_payment

    principal = principal * (1 + rate / 12)

    if principal > payment:
        total_paid += payment
        principal -= payment
    else:
        total_paid += principal
        principal = 0

    print(f"Month #{month_counter:4d} | Total paid: {total_paid:0.2f} | Principal: {principal:0.2f}")


print(f'\n=============================')
print('Total paid', round(total_paid, 2))
print('Months', month_counter)
