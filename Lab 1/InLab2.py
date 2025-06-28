hourly_wage = float(input("Enter hourly wage: "))
regular_hours = float(input("Enter total regular hours: "))
overtime_hours = float(input("Enter total overtime hours: "))

regular_pay = hourly_wage * regular_hours
overtime_pay = overtime_hours * 1.5 * hourly_wage
total_pay = regular_pay + overtime_pay

print(f"Total weekly pay: ${total_pay:.2f}")