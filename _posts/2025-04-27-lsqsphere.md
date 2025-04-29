---
category: [積體電路]
tags: [数学]
title: 的最小平方法(球體)
date: 2025-04-27 1:00:00
---

<style>
  table {
    width: 100%
    }
  td {
    vertical-align: center;
    text-align: center;
  }
  table.inputT{
    margin: 10px;
    width: auto;
    margin-left: auto;
    margin-right: auto;
    border: none;
  }
  input{
    text-align: center;
    padding: 0px 10px;
  }
  iframe{
    width: 100%;
    display: block;
    border-style:none;
  }
</style>

# 球體的最小平方法擬合

点云由 $n$ 个点给出，坐标分别为 $x_i, y_i, z_i$。目标是估计与这些点最匹配的球体参数 $x_c, y_c, z_c$ 和 $r$：

 - $X_c$ 是球心的 x 坐标
 - $Y_c$ 是球心的 y 坐标
 - $Z_c$ 是球心的 z 坐标
 - $r$ 是球体的半径

理想球体的方程为:


$$
(x_i-x_c)^2 + (y_i-y_c)^2  + (z_i-z_c)^2 = r^2
$$

上述方程重写为：

$$
x_i^2 + x_c^2 - 2x_ix_c + y_i^2 + y_c^2 - 2y_iy_c + z_i^2 + z_c^2 - 2z_iz_c = r^2
$$

$$
2x_cx_i + 2y_cy_i  + 2z_cz_i + r^2 - x_c^2 - y_c^2 - z_c^2 = x_i^2 + y_i^2 + z_i^2
$$

$$
ax_i + by_i + cz_i + d  = x_i^2 + y_i^2  + z_i^2
$$

$$
a = 2x_c,b = 2y_c,c = 2z_c,,d = r^2 - x_c^2 - y_c^2 - z_c^2
$$

整个系统（针对所有点）可以重写为：


$$
\begin{array}{rcl} ax_1 + by_1 + cz_1 + d & = & x_1^2 + y_1^2 + z_1^2 \\
ax_2 + by_2 + cz_2 + d & = & x_2^2 + y_2^2 + z_2^2 \\
& ... & \\
ax_n + by_n + cz_n + d & = & x_n^2 + y_n^2 + z_n^2 \\
\end{array}
$$

该系统的矩阵形式为：

$$
\left[ \begin{matrix} x_1 & y_1 & z_1 & 1 \\
x_2 & y_2 & z_2 & 1 \\
... & ... & ... & ... \\
x_n & y_n & z_3 & 1 \\
\end{matrix} \right].\left[ \begin{matrix}
a \\
b \\
c \\
d
\end{matrix} \right] = \left[ \begin{matrix}
x_1^2 + y_1^2 + z_1^2 \\
x_2^2 + y_2^2 + z_2^2 \\
... \\
x_n^2 + y_n^2 + z_n^2 \\
\end{matrix} \right]
$$

讓我們定義 A、B 和 X：

$$
\begin{matrix}
A=\left[ \begin{matrix}
x_1 & y_1 & z_1 & 1 \\
x_2 & y_2 & z_1 & 1 \\
... & ... & ... \\
x_n & y_n & z_1 & 1 \\
\end{matrix} \right]
&
B=\left[ \begin{matrix} x_1^2 + y_1^2 + z_1^2 \\  x_2^2 + y_2^2 + z_2^2  \\...  \\  x_n^2 + y_n^2 + z_n^2  \\ \end{matrix} \right]
&
X=\left[ \begin{matrix} a \\ b \\ c \\ d \end{matrix} \right]
\end{matrix}
$$

该系统现在由以下公式给出：

$$
A.X=B
$$

## 求解系统公式

$$
\hat{x}=A^{+}.B = A^{T}(A.A^{T})^{-1}.B
$$


其中 $A^{+}$ 是 $A$ 的伪逆。$A^{+}$ 可以通过以下公式计算：

$$
A^{+}=A^{T}(A.A^{T})^{-1}
$$


以上偽逆是非奇異方陣逆的概念向奇異矩陣和矩形矩陣的擴展。它是眾多廣義逆之一，但由於它具有許多特殊性質，因此在實踐中最有用。

如下動畫說明 $A$ 转换至 $A^{T}$ 可源自透過主對角線的反射。

![Alt X](../assets/img/math/mtranspose.gif)

逆距陣求法：

$$
D=A.A^{T}
$$


$$
D^{-1}= \frac {1}{|D|} \cdot Adj  D
$$


## 求逆距陣 **D** 的 C 源代码

```c
#include <stdio.h>
#define MAX_SIZE 10

// 讀取矩陣元素的函數
void readMatrix(int matrix[MAX_SIZE][MAX_SIZE], int size) {
  printf("Enter the elements of the %dx%d matrix:\n", size, size);
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      printf("Enter element [%d][%d]: ", i, j);
      scanf("%d", &matrix[i][j]);
    }
  }
}

// 獲取函數餘因子 matrix[p][q] in temp[][]
void getCofactor(int matrix[MAX_SIZE][MAX_SIZE], int temp[MAX_SIZE][MAX_SIZE], int p, int q, int n) {
  int i = 0, j = 0;
  for (int row = 0; row < n; row++) {
    for (int col = 0; col < n; col++) {
      if (row != p && col != q) {
        temp[i][j++] = matrix[row][col];
        if (j == n - 1) {
           j = 0;
           i++;
        }
      }
    }
  }
}

// 遞歸函數找出矩陣的行列式
int determinant(int matrix[MAX_SIZE][MAX_SIZE], int n) {
  int det = 0;
  if (n == 1)
    return matrix[0][0];
    int temp[MAX_SIZE][MAX_SIZE];
    int sign = 1;
    for (int f = 0; f < n; f++) {
      getCofactor(matrix, temp, 0, f, n);
      det += sign * matrix[0][f] * determinant(temp, n - 1);
      sign = -sign;
    }
  return det;
}

// 計算矩陣伴隨的函數
void adjoint(int matrix[MAX_SIZE][MAX_SIZE], int adj[MAX_SIZE][MAX_SIZE], int n) {
  if (n == 1) {
    adj[0][0] = 1;
    return;
  }
  int sign = 1;
  int temp[MAX_SIZE][MAX_SIZE];
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
    // 獲取的餘因子 matrix[i][j]
    getCofactor(matrix, temp, i, j, n);
    // 若行和列索引之和為偶數，則 adj[j][i] 的符號為正
    sign = ((i + j) % 2 == 0) ? 1 : -1;
    // 交換行和列以獲得餘因子矩陣的轉置
    adj[j][i] = sign * determinant(temp, n - 1);
    }
  }
}

// 計算矩陣逆的函數
int inverse(int matrix[MAX_SIZE][MAX_SIZE], float inverse[MAX_SIZE][MAX_SIZE], int n) {
  // 求矩陣的行列式
  int det = determinant(matrix, n);
  // 如果行列式為零，則矩陣不可逆
  if (det == 0) {
    printf("Matrix is not invertible as determinant is zero.\n");
    return 0;
  }
  // 求矩陣的伴隨
  int adj[MAX_SIZE][MAX_SIZE];
  adjoint(matrix, adj, n);
  // 將伴隨式除以行列式來求逆
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      inverse[i][j] = adj[i][j] / (float)det;
    }
  }
  return 1;
}

// 顯示整數矩陣的函數
void displayMatrix(int matrix[MAX_SIZE][MAX_SIZE], int size) {
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      printf("%d\t", matrix[i][j]);
    }
    printf("\n");
  }
}

// 顯示浮點矩陣的函數（用於逆）
void displayFloatMatrix(float matrix[MAX_SIZE][MAX_SIZE], int size) {
  for (int i = 0; i <   size; i++) {
    for (int j = 0; j < size; j++) {
      printf("%.4f\t", matrix[i][j]);
    }
    printf("\n");
  }
}

int main() {
  int matrix[MAX_SIZE][MAX_SIZE];
  float inv[MAX_SIZE][MAX_SIZE];
  int size;
    // 取得矩陣大小
  printf("Matrix Inverse Calculator\n"); printf("=========================\n");
  printf("Enter the size of the square matrix (1-%d): ", MAX_SIZE);
  scanf("%d", &size);
  // 驗證矩陣大小
  if (size <= 0 || size > MAX_SIZE) {
    printf("Invalid matrix size. Please enter a size between 1 and %d.\n", MAX_SIZE);
    return 1;
  }
  // 讀取矩陣元素
  readMatrix(matrix, size);
  // 顯示原始矩陣
  printf("\nOriginal Matrix:\n");
  displayMatrix(matrix, size);
  // 計算並顯示行列式
  int det = determinant(matrix, size);
  printf("\nDeterminant of the matrix is: %d\n", det);
  // 計算並顯示逆
  if (inverse(matrix, inv, size)) {
    printf("\nInverse Matrix:\n");
    displayFloatMatrix(inv, size);
  }
  return 0;
}
```


$$
A^{+}=A^{T}(D)^{-1}
$$


$$
\left[ \begin{matrix}
a \\
b \\
c \\
d
\end{matrix} \right] = \hat{x}=A^{+}.B = A^{T}D^{-1}.B
$$

由於變數發生了變化，因此只需計算 $x_c、y_c、z_c$ 和 $r$：

$$ x_c = \dfrac{a}{2} $$

$$ y_c = \dfrac{b}{2} $$

$$ z_c = \dfrac{c}{2} $$

$$ r = \dfrac{ \sqrt{4d + a^2 + b^2 + c^2}}{2} $$

并获取球体的参数：

![Alt X](../assets/img/math/lsqsphere.png)







