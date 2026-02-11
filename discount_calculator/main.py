import tkinter as tk
from tkinter import ttk, messagebox
from decimal import Decimal, ROUND_HALF_UP

class DiscountCalculator:
 def __init__(self, root):
 self.root = root
 self.root.title("Калькулятор скидок")
 self.root.geometry("400x500")
 self.root.resizable(False, False)
 
 # Настройка стиля
 style = ttk.Style()
 style.theme_use('clam')
 
 self.setup_ui()
 
 def setup_ui(self):
 # Главный фрейм
 main_frame = ttk.Frame(self.root, padding="20")
 main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
 
 # Заголовок
 title_label = ttk.Label(main_frame, text="Калькулятор скидок", 
 font=('Arial', 16, 'bold'))
 title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
 
 # Поля ввода
 ttk.Label(main_frame, text="Исходная цена:").grid(row=1, column=0, sticky=tk.W, pady=5)
 self.original_price = tk.StringVar()
 ttk.Entry(main_frame, textvariable=self.original_price, width=20).grid(row=1, column=1, pady=5, padx=(10, 0))
 
 ttk.Label(main_frame, text="Скидка (%):").grid(row=2, column=0, sticky=tk.W, pady=5)
 self.discount_percent = tk.StringVar()
 ttk.Entry(main_frame, textvariable=self.discount_percent, width=20).grid(row=2, column=1, pady=5, padx=(10, 0))
 
 # Кнопки
 button_frame = ttk.Frame(main_frame)
 button_frame.grid(row=3, column=0, columnspan=2, pady=20)
 
 ttk.Button(button_frame, text="Рассчитать", 
 command=self.calculate_discount).pack(side=tk.LEFT, padx=5)
 ttk.Button(button_frame, text="Очистить", 
 command=self.clear_fields).pack(side=tk.LEFT, padx=5)
 
 # Результаты
 results_frame = ttk.LabelFrame(main_frame, text="Результаты", padding="10")
 results_frame.grid(row=4, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E))
 
 ttk.Label(results_frame, text="Сумма скидки:").grid(row=0, column=0, sticky=tk.W, pady=5)
 self.discount_amount_label = ttk.Label(results_frame, text="0.00 руб.", 
 font=('Arial', 10, 'bold'))
 self.discount_amount_label.grid(row=0, column=1, sticky=tk.E, pady=5)
 
 ttk.Label(results_frame, text="Цена со скидкой:").grid(row=1, column=0, sticky=tk.W, pady=5)
 self.final_price_label = ttk.Label(results_frame, text="0.00 руб.", 
 font=('Arial', 10, 'bold'), 
 foreground='green')
 self.final_price_label.grid(row=1, column=1, sticky=tk.E, pady=5)
 
 ttk.Label(results_frame, text="Экономия:").grid(row=2, column=0, sticky=tk.W, pady=5)
 self.savings_label = ttk.Label(results_frame, text="0.00 руб.", 
 font=('Arial', 10, 'bold'), 
 foreground='red')
 self.savings_label.grid(row=2, column=1, sticky=tk.E, pady=5)
 
 # История расчетов
 history_frame = ttk.LabelFrame(main_frame, text="История расчетов", padding="10")
 history_frame.grid(row=5, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E, tk.N, tk.S))
 
 # Создание Treeview для истории
 columns = ('original', 'discount', 'final', 'savings')
 self.history_tree = ttk.Treeview(history_frame, columns=columns, show='headings', height=6)
 
 # Настройка заголовков
 self.history_tree.heading('original', text='Цена')
 self.history_tree.heading('discount', text='Скидка %')
 self.history_tree.heading('final', text='Итого')
 self.history_tree.heading('savings', text='Экономия')
 
 # Настройка ширины колонок
 self.history_tree.column('original', width=80)
 self.history_tree.column('discount', width=80)
 self.history_tree.column('final', width=80)
 self.history_tree.column('savings', width=80)
 
 self.history_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
 
 # Скроллбар для истории
 history_scrollbar = ttk.Scrollbar(history_frame, orient=tk.VERTICAL, 
 command=self.history_tree.yview)
 history_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
 self.history_tree.configure(yscrollcommand=history_scrollbar.set)
 
 # Кнопка очистки истории
 ttk.Button(history_frame, text="Очистить историю", 
 command=self.clear_history).grid(row=1, column=0, pady=10)
 
 # Настройка весов для адаптивности
 main_frame.columnconfigure(1, weight=1)
 self.root.columnconfigure(0, weight=1)
 self.root.rowconfigure(0, weight=1)
 
 def calculate_discount(self):
 try:
 # Получение значений
 original = Decimal(self.original_price.get().replace(',', '.'))
 discount_pct = Decimal(self.discount_percent.get().replace(',', '.'))
 
 # Валидация
 if original < 0:
 raise ValueError("Цена не может быть отрицательной")
 if discount_pct < 0 or discount_pct > 100:
 raise ValueError("Скидка должна быть от 0 до 100%")
 
 # Расчеты
 discount_amount = original * (discount_pct / 100)
 final_price = original - discount_amount
 
 # Округление до 2 знаков
 discount_amount = discount_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
 final_price = final_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
 
 # Обновление результатов
 self.discount_amount_label.config(text=f"{discount_amount} руб.")
 self.final_price_label.config(text=f"{final_price} руб.")
 self.savings_label.config(text=f"{discount_amount} руб.")
 
 # Добавление в историю
 self.add_to_history(original, discount_pct, final_price, discount_amount)
 
 except ValueError as e:
 if "invalid literal" in str(e):
 messagebox.showerror("Ошибка", "Введите корректные числовые значения")
 else:
 messagebox.showerror("Ошибка", str(e))
 except Exception as e:
 messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
 
 def add_to_history(self, original, discount_pct, final_price, savings):
 self.history_tree.insert('', 0, values=(
 f"{original}",
 f"{discount_pct}%",
 f"{final_price}",
 f"{savings}"
 ))
 
 def clear_fields(self):
 self.original_price.set("")
 self.discount_percent.set("")
 self.discount_amount_label.config(text="0.00 руб.")
 self.final_price_label.config(text="0.00 руб.")
 self.savings_label.config(text="0.00 руб.")
 
 def clear_history(self):
 for item in self.history_tree.get_children():
 self.history_tree.delete(item)

def main():
 root = tk.Tk()
 app = DiscountCalculator(root)
 root.mainloop()

if __name__ == "__main__":
 main()