def add_time(start, duration, weekday=None):
    # Dicionário para os dias da semana
    the_week = {
        'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3,
        'Thursday': 4, 'Friday': 5, 'Saturday': 6
    }

    # Invertendo o dicionário
    inv_the_week = {v: k for k, v in the_week.items()}

    # Separando os componentes da hora de início
    start_time, period = start.split()
    start_hours, start_minutes = map(int, start_time.split(':'))

    # Convertendo para formato 24 horas
    if period == "PM" and start_hours != 12:
        start_hours += 12
    elif period == "AM" and start_hours == 12:
        start_hours = 0

    # Separando os componentes da duração
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Calculando a nova hora e minutos
    total_minutes = start_minutes + duration_minutes
    extra_hours = total_minutes // 60
    new_minutes = total_minutes % 60
    total_hours = start_hours + duration_hours + extra_hours

    # Contagem de dias passados
    days_passed = total_hours // 24
    new_hours = total_hours % 24

    # Convertendo de volta para AM/PM
    period = "AM" if new_hours < 12 else "PM"
    new_hours = new_hours if new_hours % 12 != 0 else 12
    new_hours = new_hours if new_hours <= 12 else new_hours - 12

    # Calculando o dia da semana, se fornecido
    if weekday:
        weekday = weekday.capitalize()
        day_index = (the_week[weekday] + days_passed) % 7
        week_str = f", {inv_the_week[day_index]}"
    else:
        week_str = ""

    # Formatando a saída para mostrar os dias passados corretamente
    if days_passed == 1:
        days_str = " (next day)"
    elif days_passed > 1:
        days_str = f" ({days_passed} days later)"
    else:
        days_str = ""

    return f"{new_hours}:{new_minutes:02d} {period}{week_str}{days_str}"