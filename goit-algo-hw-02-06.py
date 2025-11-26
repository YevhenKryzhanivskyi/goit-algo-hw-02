def hanoi(n, source, target, auxiliary, pegs, log):
    """Рекурсивне переміщення дисків між стрижнями."""
    if n == 1:
        disk = pegs[source].pop()
        pegs[target].append(disk)
        log.append(f"Перемістити диск з {source} на {target}: {disk}")
        log.append(f"Проміжний стан: {pegs}")
    else:
        hanoi(n - 1, source, auxiliary, target, pegs, log)
        disk = pegs[source].pop()
        pegs[target].append(disk)
        log.append(f"Перемістити диск з {source} на {target}: {disk}")
        log.append(f"Проміжний стан: {pegs}")
        hanoi(n - 1, auxiliary, target, source, pegs, log)


def solve_hanoi(n):
    """Ініціалізація стрижнів та запуск алгоритму."""
    pegs = {
        'A': list(range(n, 0, -1)),  # [n, n-1, ..., 1]
        'B': [],
        'C': []
    }
    log = []
    log.append(f"Початковий стан: {pegs}")
    hanoi(n, 'A', 'C', 'B', pegs, log)
    log.append(f"Кінцевий стан: {pegs}")
    return log


def main():
    """Основна функція програми."""
    n = int(input("Введіть кількість дисків: "))
    result = solve_hanoi(n)
    for line in result:
        print(line)


if __name__ == "__main__":
    main()