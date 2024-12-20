import numpy as np

def simplex(c, A, b):
    """
    Решает задачу линейного программирования в канонической форме
    с помощью симплекс-метода.

    Args:
        c: Массив коэффициентов целевой функции.
        A: Матрица коэффициентов ограничений.
        b: Вектор правых частей ограничений.

    Returns:
        Кортеж (x, z), где x - оптимальное решение, z - значение целевой функции.
    """

    m, n = A.shape
    A = np.hstack((A, np.eye(m)))
    c = np.hstack((c, np.zeros(m)))

    basis = list(range(n, n + m))

    while True:
        z = np.dot(c[basis], A[:, basis].T)

        if all(z <= 0):
            break

        entering = np.argmax(z)

        ratios = b / A[:, entering]
        ratios[A[:, entering] <= 0] = np.inf

        leaving = np.argmin(ratios)

        basis[leaving] = entering

    x = np.zeros(n + m)
    x[basis] = A[:, basis].T @ np.linalg.inv(A[:, basis]) @ b

    return x[:n], np.dot(c[:n], x[:n])

# Пример использования
c = np.array([2, 3])
A = np.array([[1, 1], [2, 1]])
b = np.array([4, 5])

x, z = simplex(c, A, b)

print("Оптимальное решение:", x)
print("Значение целевой функции:", z)
