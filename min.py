def poly(x, y):
    return 6*x**6 + 2*x**4*y**2 + 10*x**2 + 6*x*y + 10*y**2 - 6*x + 4
def partialX(x, y):
    return 36*x**5 + 8*x**3*y**2 + 20*x + 6*y - 6
def partialY(x, y):
    return 4*x**4*y + 6*x + 20*y

def grad(x, y, step_size=0.001, eps=1e-3):
    x_old = 100000000
    y_old = 100000000
    while abs(x - x_old) + abs(y - y_old) > eps:
        x_new = x - step_size * partialX(x, y)
        y_new = y - step_size * partialY(x, y)
        x_old = x
        y_old = y
        x = x_new
        y = y_new
    return x, y

x, y = grad(1, 1, step_size=0.000001, eps=1e-10)
print(f"x = {x}, y = {y}")
print("min = ", poly(x, y))