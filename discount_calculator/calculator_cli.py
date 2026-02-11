#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decimal import Decimal, ROUND_HALF_UP
import sys

class DiscountCalculatorCLI:
 def __init__(self):
 self.history = []
 
 def calculate_discount(self, original_price, discount_percent):
 """
 Рассчитывает скидку и итоговую цену
 
 Args:
 original_price (float): Исходная цена
 discount_percent (float): Процент скидки
 
 Returns:
 dict: Словарь с результатами расчета
 """
 try:
 original = Decimal(str(original_price))
 discount_pct = Decimal(str(discount_percent))
 
 if original < 0:
 raise ValueError("Цена не может быть отрицательной")
 if discount_pct < 0 or discount_pct > 100:
 raise ValueError("Скидка должна быть от 0 до 100%")
 
 discount_amount = original * (discount_pct / 100)
 final_price = original - discount_amount
 
 # Округление до 2 знаков
 discount_amount = discount_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
 final_price = final_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
 
 result = {
 'original_price': float(original),
 'discount_percent': float(discount_pct),
 'discount_amount': float(discount_amount),
 'final_price': float(final_price),
 'savings': float(discount_amount)
 }
 
 self.history.append(result)
 return result
 
 except Exception as e:
 raise Exception(f"Ошибка расчета: {str(e)}")
 
 def print_result(self, result):
 """Выводит результат расчета в консоль"""
 print("\n" + "="*50)
 print("РЕЗУЛЬТАТ РАСЧЕТА СКИДКИ")
 print("="*50)
 print(f"Исходная цена: {result['original_price']:.2f} руб.")
 print(f"Скидка: {result['discount_percent']:.1f}%")
 print(f"Сумма скидки: {result['discount_amount']:.2f} руб.")
 print(f"Итоговая цена: {result['final_price']:.2f} руб.")
 print(f"Экономия: {result['savings']:.2f} руб.")
 print("="*50)
 
 def show_history(self):
 """Показывает историю расчетов"""
 if not self.history:
 print("\nИстория расчетов пуста")
 return
 
 print("\n" + "="*80)
 print("ИСТОРИЯ РАСЧЕТОВ")
 print("="*80)
 print(f"{'№':<3} {'Цена':<10} {'Скидка':<8} {'Сумма скидки':<12} {'Итого':<10} {'Экономия':<10}")
 print("-"*80)
 
 for i, calc in enumerate(self.history, 1):
 print(f"{i:<3} {calc['original_price']:<10.2f} {calc['discount_percent']:<8.1f}% "
 f"{calc['discount_amount']:<12.2f} {calc['final_price']:<10.2f} {calc['savings']:<10.2f}")
 
 print("="*80)
 
 def interactive_mode(self):
 """Интерактивный режим работы"""
 print("\n🧮 КАЛЬКУЛЯТОР СКИДОК")
 print("Для выхода введите 'exit' или 'quit'")
 print("Для просмотра истории введите 'history'")
 
 while True:
 try:
 print("\n" + "-"*40)
 user_input = input("Введите команду (или 'help' для справки): ").strip().lower()
 
 if user_input in ['exit', 'quit', 'q']:
 print("До свидания!")
 break
 elif user_input == 'history':
 self.show_history()
 continue
 elif user_input == 'help':
 self.show_help()
 continue
 
 # Ввод данных для расчета
 original_price = float(input("Введите исходную цену: "))
 discount_percent = float(input("Введите процент скидки: "))
 
 result = self.calculate_discount(original_price, discount_percent)
 self.print_result(result)
 
 except KeyboardInterrupt:
 print("\nПрограмма прервана пользователем")
 break
 except ValueError:
 print("❌ Ошибка: Введите корректные числовые значения")
 except Exception as e:
 print(f"❌ {str(e)}")
 
 def show_help(self):
 """Показывает справку"""
 print("\n📖 СПРАВКА")
 print("-"*30)
 print("Команды:")
 print(" help - показать эту справку")
 print(" history - показать историю расчетов")
 print(" exit/quit - выйти из программы")
 print("\nПример использования:")
 print(" Исходная цена: 1000")
 print(" Процент скидки: 15")
 print(" Результат: цена со скидкой 850 руб., экономия 150 руб.")

def main():
 calculator = DiscountCalculatorCLI()
 
 # Проверяем аргументы командной строки
 if len(sys.argv) == 3:
 try:
 original_price = float(sys.argv[1])
 discount_percent = float(sys.argv[2])
 
 result = calculator.calculate_discount(original_price, discount_percent)
 calculator.print_result(result)
 except ValueError:
 print("❌ Ошибка: Некорректные аргументы. Используйте числовые значения.")
 print("Пример: python calculator_cli.py 1000 15")
 except Exception as e:
 print(f"❌ {str(e)}")
 else:
 # Интерактивный режим
 calculator.interactive_mode()

if __name__ == "__main__":
 main()