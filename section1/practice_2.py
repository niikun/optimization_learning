import pulp
import numpy as np
import matplotlib.pyplot as plt

# 問題の定義
prob = pulp.LpProblem("practice2", sense=pulp.LpMaximize)

# 変数の定義
x = pulp.LpVariable("x", lowBound=0, cat="Continuous")
y = pulp.LpVariable("y", lowBound=0, cat="Continuous")

# 目的関数の追加
prob += 100 * x + 150 * y, "Objective"

# 制約条件の追加
prob += x + 2 * y <= 6
prob += 2 * x + y <= 9

# 問題の解決
status = prob.solve()

print("status:", pulp.LpStatus[status])
print("x:", x.value())
print("y:", y.value())

# グラフの描画
a = np.linspace(-10, 10, 100)
plt.plot(a, 3 - a / 2, label="x+2y<=6", color="blue")
plt.plot(a, 9 - 2 * a, label="2x+y<=9", color="red")
plt.plot(x.value(), y.value(), "ro")  # 解のプロット
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of Constraints and Solution')
plt.grid(True)

# グラフをファイルとして保存
plt.savefig('practice2.png')
print("グラフが 'practice2.png' として保存されました。")    