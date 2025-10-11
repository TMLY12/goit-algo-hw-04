import random

def get_numbers_ticket(min_number: int, max_number: int, quantity: int) -> list:
    numbers = random.sample(range(min_number, max_number+1), quantity)
    return sorted(numbers)
lottery_numbers = get_numbers_ticket(1,49,6)
print("Ваші лотерейні числа:", lottery_numbers)