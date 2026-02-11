import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Fonction et gradient
# ============================================================
def f(x):
    return x**2

def grad_f(x):
    return 2*x

# ============================================================
# Recherche linéaire d'Armijo (avec affichage du pas)
# ============================================================
def armijo_line_search(x, d, f, grad_f, alpha_init=1.0, beta=0.5, c=1e-4):
    alpha = alpha_init
    steps = 0

    # condition d'Armijo
    while f(x + alpha * d) > f(x) + c * alpha * grad_f(x) * d:
        alpha *= beta
        steps += 1

    print(f"    Armijo: alpha = {alpha:.6f} (réduit {steps} fois)")
    return alpha

# ============================================================
# Descente de gradient + sauvegarde de la trajectoire
# ============================================================
def gradient_descent_line_search(x0, f, grad_f, max_iter=20, epsilon=1e-6):
    x = x0
    history = [x]

    for k in range(max_iter):
        g = grad_f(x)

        print(f"Iteration {k}: x = {x:.6f}, gradient = {g:.6f}")

        if abs(g) < epsilon:
            print("Gradient très petit → arrêt.")
            break

        d = -g

        alpha = armijo_line_search(x, d, f, grad_f)
        x = x + alpha * d

        print(f"    Nouveau x = {x:.6f}, f(x) = {f(x):.6f}\n")

        history.append(x)

    return np.array(history)

# ============================================================
# Exécution de la descente
# ============================================================
x0 = 5.0
trajectory = gradient_descent_line_search(x0, f, grad_f)

# ============================================================
# Visualisation de la fonction et de la trajectoire
# ============================================================
x_vals = np.linspace(-6, 6, 400)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="f(x) = x²")

# afficher les points + lignes
for i, x in enumerate(trajectory):
    plt.scatter(x, f(x), color="red")
    if i > 0:
        plt.plot([trajectory[i-1], trajectory[i]],
                 [f(trajectory[i-1]), f(trajectory[i])],
                 color="blue")

plt.title("Descente de Gradient avec Recherche Linéaire (Armijo)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
