

diary = [
    {"day": 1, "text": "Прибув до містечка Вербівка, зупинився на заїжджому дворі."},
    {"day": 2, "text": "Знайшов стару карту в руїнах на околиці міста."},
    {"day": 3, "text": "Вирушив у путь до міста Київ."},
]


def print_diary(diary):
    """Виводить усі записи щоденника."""
    print("\n=== Щоденник мандрівника ===")

    for entry in diary:
        print(f"День {entry['day']}: {entry['text']}")


def add_entry(diary):
    """Додає новий запис, не видаляючи попередні."""
    text = input("Введи новий запис: ").strip()

    if not text:
        print("Запис не може бути порожнім.")
        return

    # Наступний номер дня визначається за кількістю записів.
    day = max((entry["day"] for entry in diary), default=0) + 1

    diary.append({"day": day, "text": text})
    print("Запис успішно додано!")


def main():
    print_diary(diary)
    add_entry(diary)
    print_diary(diary)


if __name__ == "__main__":
    main()