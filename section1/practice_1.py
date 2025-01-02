import numpy as np
import pulp
import matplotlib.pyplot as plt

# 問題の定義
prob = pulp.LpProblem("practice1", sense=pulp.LpMaximize)

# 変数の定義
x = pulp.LpVariable("x", cat="Continuous")
y = pulp.LpVariable("y", cat="Continuous")

# 目的関数の追加
prob += x + y, "Objective"

# 制約条件の追加
prob += x - y + 1 <= 0
prob += 3 * x + y <= -3

# 問題の解決
status = prob.solve()

print("status:", pulp.LpStatus[status])
print("x:", x.value())
print("y:", y.value())

# グラフの描画
a = np.linspace(-10, 10, 100)
plt.plot(a, a + 1, label="x-y+1<=0", color="blue")
plt.plot(a, -3 - 3 * a, label="3x+y<=-3", color="red")
plt.plot(x.value(), y.value(), "ro")  # 解のプロット
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of Constraints and Solution')
plt.grid(True)

# グラフをファイルとして保存
plt.savefig('graph_solution.png')
print("グラフが 'graph_solution.png' として保存されました。")
