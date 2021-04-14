from itertools import product
import numpy as np
import matplotlib.pyplot as plt

F = 0
P = 1

# włamanie
p_w = np.zeros(2)
p_w[P] = 0.001
p_w[F] = 0.999

# piorun
p_r = np.zeros(2)
p_r[P] = 0.002
p_r[F] = 0.998

# alarm
pw_a_wr = np.zeros((2, 2, 2))
pw_a_wr[P, P, P] = 0.95
pw_a_wr[P, P, F] = 0.94
pw_a_wr[P, F, P] = 0.29
pw_a_wr[P, F, F] = 0.001

pw_a_wr[F, P, P] = 0.05
pw_a_wr[F, P, F] = 0.06
pw_a_wr[F, F, P] = 0.71
pw_a_wr[F, F, F] = 0.999

# telefon do stefana
pw_s_a = np.zeros((2, 2))
pw_s_a[P, P] = 0.9
pw_s_a[P, F] = 0.1
pw_s_a[F, P] = 0.05
pw_s_a[F, F] = 0.95

# telefon do barbary
pw_b_a = np.zeros((2, 2))
pw_b_a[P, P] = 0.7
pw_b_a[P, F] = 0.3
pw_b_a[F, P] = 0.01
pw_b_a[F, F] = 0.99

# Obliczanie wybranych prawdopodobieństw warunkowch metodą dokładną

# Generowanie tablicy łącznego rozkładu pradopodobieństwa
pw = np.zeros((2, 2, 2, 2, 2))
for W in [P, F]:
    for R in [P, F]:
        for A in [P, F]:
            for S in [P, F]:
                for B in [P, F]:
                    pw[W, R, A, S, B] = p_w[W]*p_r[R]*pw_a_wr[A, W, P]*pw_s_a[S, A]*pw_b_a[B, A]

# 1) Alarm, jeżeli obydwoje sąsiedzi zadzwonili
# P(A = P | P(S = P, B = P)) = P(A = P, S = P, B = P) / P(S = P, B = P)

# P(A = P, S = P, B = P)
pw_a_and_s_and_b = sum([pw[w, r, P, P, P] for w, r in product([P, F], [P, F])])

# P(S = P, B = P)
pw_s_and_b = sum([pw[w, r, a, P, P] for w, r, a in product([P, F], [P, F], [P, F])])

pw_a_sb_exact = pw_a_and_s_and_b / pw_s_and_b;
print('P(A = P|(S = P, B = P)) exact: ', pw_a_sb_exact)

# 2) Włamanie, jeżeli obydwoje zadzwonili
# P(W = P | P(S = P, B = P)) = P(W = P, S = P, B = P) / P(S = P, B = P)

# P(W = P, S = P, B = P)
pw_w_and_s_and_b = sum([pw[P, r, a, P, P] for r, a in product([P, F], [P, F])])

# P(S = P, B = P)
# obliczone wyżej

pw_w_sb_exact = pw_w_and_s_and_b / pw_s_and_b;
print('P(W = P|(S = P, B = P)) exact: ', pw_w_sb_exact)

# Obliczanie wybranych prawdopodobieństw warunkowch metoda Monte Carlo

I = 100  # liczba iteracji
K = 2000  # liczba probek na ieracje

avg_p_a_if_sb = 0
avg_p_w_if_sb = 0

plt.axis([0, I, 0, 2])
plt.xlabel('Iteracja')
plt.ylabel('Prawdopodobieństwo')
plt.plot([0, I], [pw_a_sb_exact, pw_a_sb_exact], color='b')
plt.plot([0, I], [pw_w_sb_exact, pw_w_sb_exact], color='b')

np.random.seed(1)
for i in range(1, I):
    # Wygenerowanie wartości poszczególnych zmiennych losowych dla losowego przebiegu sieci
    w = np.random.random(K) < p_w[P]
    r = np.random.random(K) < p_r[P]
    aPP = np.random.random(K) < pw_a_wr[P, P, P]
    aPF = np.random.random(K) < pw_a_wr[P, P, F]
    aFP = np.random.random(K) < pw_a_wr[P, F, P]
    aFF = np.random.random(K) < pw_a_wr[P, F, F]
    a = np.logical_or.reduce((
        np.logical_and.reduce((w, r, aPP)),
        np.logical_and.reduce((w, np.logical_not(r), aPF)),
        np.logical_and.reduce((np.logical_not(w), r, aFP)),
        np.logical_and.reduce((np.logical_not(w), np.logical_not(r), aFF))
    ))

    s_p = np.random.random(K) < pw_s_a[P, P]
    s_f = np.random.random(K) < pw_s_a[F, P]
    stefan = np.logical_or(
        np.logical_and(a, s_p),
        np.logical_and(np.logical_not(a), s_f)
    )

    b_p = np.random.random(K) < pw_b_a[P, P]
    b_f = np.random.random(K) < pw_b_a[F, P]
    barbara = np.logical_or(
        np.logical_and(a, b_p),
        np.logical_and(np.logical_not(a), b_f)
    )

    # Oszacowanie prawdopodobienstw warunkowych na podstawie tablic: w, p, a, stefan, barbara

    # P(A = P | S = T, B = T) = P(A = T | S = T, B = T) / P(S = T, B = T)
    p_a_if_sb__mc = np.sum(np.logical_and.reduce((a, stefan, barbara))) / np.sum(
        np.logical_and.reduce((stefan, barbara)))

    # P(W = P | S = T, B = T) = P(W = T | S = T, B = T) / P(S = T, B = T)
    p_w_if_sb__mc = np.sum(np.logical_and.reduce((w, stefan, barbara))) / np.sum(
        np.logical_and.reduce((stefan, barbara)))

    # Ze wzoru na iteracyjne liczenie sredniej
    avg_p_a_if_sb = avg_p_a_if_sb + (p_a_if_sb__mc - avg_p_a_if_sb) / i
    avg_p_w_if_sb = avg_p_w_if_sb + (p_w_if_sb__mc - avg_p_w_if_sb) / i

    plt.scatter(i, avg_p_a_if_sb, marker='.', s=1, color='r')
    plt.scatter(i, avg_p_w_if_sb, marker='.', s=1, color='r')

    plt.pause(0.001)

print('P(A = P | S = T, B = T) Monte Carlo: ', avg_p_a_if_sb)
print('P(W = P | S = T, B = T) Monte Carlo: ', avg_p_w_if_sb)

