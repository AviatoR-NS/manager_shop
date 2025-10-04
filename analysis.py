def analyze_orders(orders, text_widget):
    """Простой анализ заказов с выводом в tk.Text"""
    text_widget.delete(1.0, "end")
    if not orders:
        text_widget.insert("end", "❌ Нет заказов для анализа.\n")
        return
    total_sum = sum(o.total for o in orders)
    avg = total_sum / len(orders)
    text_widget.insert("end", "=== Анализ заказов ===\n")
    text_widget.insert("end", f"Всего заказов: {len(orders)}\n")
    text_widget.insert("end", f"Общая сумма: {total_sum} руб.\n")
    text_widget.insert("end", f"Средний чек: {avg:.2f} руб.\n")
