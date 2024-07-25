usd_exchange_rate = float(input())
rub_quantity = int(input())
rub_to_usd = rub_quantity / usd_exchange_rate

print(f"Вы можете получить {int(rub_to_usd)}$ за {rub_quantity} рублей по курсу {usd_exchange_rate}")