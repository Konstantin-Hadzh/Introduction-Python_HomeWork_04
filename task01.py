

'''1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета 
заработной платы сотрудника. В расчете необходимо использовать формулу: 
(выработка в часах*ставка в час) + премия. Для выполнения расчета для 
конкретных значений необходимо запускать скрипт с параметрами'''


from sys import argv

wages, output_hours, rate_hour, bonus = argv

print("Script Name: ", wages)
print("Output in hours: ", output_hours)
print("Rate per hour: ", rate_hour)
print("Prize: ", bonus)
print("Employee salary: ", (float(output_hours) * float(rate_hour)) + float(bonus))