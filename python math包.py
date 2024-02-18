
import math as m

print(dir(m))  # 先看看有哪些方法

print(m.e)  # 返回欧拉数

print(m.inf)
print(-m.inf)  # 返回正/负无穷大常量

print(m.nan)
print(float(m.nan))  # 非法数字

print(m.pi)  # 圆周率

print(m.tau)  # 2 * math.pi
print(bool(m.tau == 2 * m.pi))  # 证实

# 输出反余弦值
print(m.acos(0.55))
print(m.acos(-0.55))
print(m.acos(0))
print(m.acos(1))
print(m.acos(-1))

# math.acosh(x) 返回 x 的反双曲余弦值。
# 输出反双曲余弦值
print(m.acosh(7))
print(m.acosh(56))
print(m.acosh(2.45))
print(m.acosh(1))

# math.asin(x) 返回 x 的反正弦值，结果范围在 -pi/2 到 pi/2 之间。
# 输出反正弦值
print(m.asin(0.55))
print(m.asin(-0.55))
print(m.asin(0))
print(m.asin(1))
print(m.asin(-1))

# math.asinh(x) 返回 x 的反双曲正弦值。
# 输出反双曲正弦值
print(m.asinh(7))
print(m.asinh(56))
print(m.asinh(2.45))
print(m.asinh(1))

# math.atan(x) 返回 x 的反正切值，以弧度为单位，结果范围在 -pi/2 到 pi/2 之间。
print(m.tan(67))
print(m.tan(0.55))
print(m.tan(1))
print(m.tan(0))
print(m.tan(-1))
print(m.tan(-67))

# math.atan2(y,x) 返回给定的 y 及 x 坐标值的反正切值 atan(y / x)，以弧度为单位，结果是在 -pi 和 pi 之间。
print(m.atan2(8, 5))
print(m.atan2(20, 10))
print(m.atan2(34, -7))

# math.atanh(x) 返回 x 的反双曲正切值。
# math.atanh(x) 的参数介于 -0.99 到 0.99 之间。
print(m.atanh(0.88))
print(m.atanh(-0.12))

# math.ceil(x) 方法将 x 向上舍入到最接近的整数。
print(m.ceil(0.11))
print(m.ceil(99.9))

# math.comb(n,k) 方法返回不重复且无顺序地从 n 项中选择 k 项的方式总数。
# 传入的参数必须是正整数。
print(m.comb(1, 100))

# math.copysign(x, y)  返回x的绝对值，符号是y
print(m.copysign(-4, -1))
print(m.copysign(-4,-2))

# math.cos(x) 返回 x 弧度的余弦值。(这个不介绍也知道)
print(m.cos(0.00))
print(m.cos(-1.23))
print(m.cos(10))
print(m.cos(m.pi))

# math.cosh(x) 返回 x 的双曲余弦值，相当于 (exp(number) + exp(-number)) / 2。
print(m.cosh(1))
print(m.cosh(0))
print(m.cosh(9.80))
print(m.cosh(1.52))

#  math.degrees(x) 方法将角度 x 从弧度转换为度数。
print(m.degrees(90))
print(m.degrees(1))
print(m.degrees(-20))
print(m.degrees(8.9))

# math.dist(p, q) 方法返回 p 与 q 两点之间的欧几里得距离，以一个坐标序列（或可迭代对象）的形式给出。
# 两个点必须具有相同的维度。
# 传入的参数必须是正整数。
p = [2]
q = [47]
print(m.dist(p, q))
p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
q = [11, 22, 33, 44, 55, 66, 77, 88, 99, 0]
print(m.dist(p,q))

# math.erf(x) 方法返回一个数的误差函数
# math.erf(x) 方法接受 - inf 和 + inf 之间的值，并返回 - 1 到 + 1 之间的值。
print(m.erf(1.28))
print(m.erf(-1.28))

# math.exp(x) 方法返回 e 的 x 次幂（次方）Ex，其中 e = 2.718281... 是自然对数的基数。
print(m.exp(-6.89))
print(m.exp(65))

# math.expm1(x) 方法返回 e 的 x 次幂（次方）减 1，Ex - 1，其中 e = 2.718281... 是自然对数的基数。
# math.expm1(x) 方法比调用 math.exp() 减去 1 更精确。
print(m.expm1(32))
print(m.expm1(120))

#  math.fabs(x) 方法返回 x 的绝对值。
# 绝对值是非负数，有负号会删除。
# 与 Python 内置的 abs() 不同，此方法始终将值转换为浮点值。
print(m.fabs(49))
print(m.fabs(-49))
print(abs(49))
print(abs(-49))

# math.factorial(x) 方法返回 x 的阶乘。参数只能是正整数。否则返回TypeError
print(m.factorial(9))        # 9*8*7*6*5*4*3*2*1
print(m.factorial(100))      # !@^&(&^$#&@%*$$^&

#  math.floor(x) 方法将 x 向下舍入到最接近的整数。
print(m.floor(10.9))
print(m.floor(1.3))

# Python math.fmod(x, y) 方法返回 x/y 的余数。
print(m.fmod(3, 2))
print(m.fmod(100000000, 32))  # enormous

# math.frexp(x) 方法以 (m, e) 对的形式返回 x 的尾数和指数。
# 该方法的数学公式为: number = m * 2**e。
print(m.frexp(10))
print(m.frexp(39))

# math.fsum(iterable) 方法计算可迭代对象 (元组, 数组, 列表, 等)中的元素的总和。
print(m.fsum([1, 2, 3, 4, 5]))
print(m.fsum([100, 400, 340, 500]))
print(m.fsum([1.7, 0.3, 1.5, 4.5]))

#  math.gamma(x) 方法返回 x 处的伽玛函数（Gamma 函数）。
# 伽玛函数，也叫欧拉第二积分，是阶乘函数在实数与复数上扩展的一类函数。
# 要查找数字的对数伽玛值，请使用 math.lgamma() 方法。
#  本函数只在python3.2以上有效！
print(m.gamma(-0.1))
print(m.gamma(8))
print(m.gamma(1.2))
print(m.gamma(80))
print(m.gamma(-0.55))

# math.gcd() 方法返回给定的整数参数的最大公约数。
# gcd(0,0) 返回 0。
print(m.gcd(100,50))

# math.hypot() 方法返回欧几里得范数。 欧几里得范数是从原点到给定坐标的距离。 欧几里得度量又称为欧几里得距离，指的是欧几里得空间中两点间"普通"（即直线）距离。
# 在 Python 3.8 之前，此方法用于查找直角三角形的斜边：sqrt(x*x + y*y)。
# 从 Python 3.8 开始，此方法也用于计算欧几里得范数。
# 对于 n 维情况，假定传递的坐标类似于 (x1, x2, x3, ..., xn)，从原点开始的欧几里得长度由 sqrt(x1*x1 + x2*x2 +x3*x3 .... xn*xn) 计算。
# 设置垂直线和底边
parendicular = 10
base = 5
# 输出直角三角形的斜边
print(m.hypot(parendicular, base))
# 输出给定坐标的欧几里得范数
print(m.hypot(10, 2, 4, 13))
print(m.hypot(4, 7, 8))
print(m.hypot(12, 14))

# math.isclose() 方法返回用于检查两个值是否彼此接近，如果值接近，则返回 True，否则返回 False。
# math.isclose() 根据给定的绝对和相对容差确定两个值是否被认为是接近的。
# 计算公式为：
# abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
# 本方法要求python版本至少为：Python 3.5
# 语法
# math.isclose() 方法语法如下：
# math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
# 参数说明：
# a -- 必需，数字。如果 x 不是一个数字，返回 TypeError。如果值为 0 或负数，则返回 ValueError。
# b -- 必需，数字。如果 x 不是一个数字，返回 TypeError。如果值为 0 或负数，则返回 ValueError。
# rel_tol -- 是相对容差，它是 a 和 b 之间允许的最大差值，相对于 a 或 b 的较大绝对值。例如，要设置5％的容差，请传递 rel_tol=0.05 。默认容差为 1e-09，确保两个值在大约9位十进制数字内相同。 rel_tol 必须大于零。
# abs_tol -- 是最小绝对容差，对于接近零的比较很有用。 abs_tol 必须至少为零。
# 输出两个值是否接近
print(m.isclose(8.005, 8.450, abs_tol = 0.4))
print(m.isclose(8.005, 8.450, abs_tol = 0.5))
# 可用于浮点数判断
# 这样会输出 false，0.1+0.2 不会等于 0.3
print(0.1+0.2 == 0.3)
print(0.1+0.2 )
# 这样会输出 true
print(m.isclose(0.1+0.2, 0.3))

# math.isfinite() 方法判断 x 是否有限，如果 x 既不是无穷大也不是 NaN，则返回 True ，否则返回 False
print(m.isfinite(2000))
print(m.isfinite(-45.34))
print(m.isfinite(+45.34))
print(m.isfinite(m.inf))
print(m.isfinite(float("nan")))
print(m.isfinite(float("inf")))
print(m.isfinite(float("-inf")))
print(m.isfinite(-m.inf))
print(m.isfinite(0.0))

#  math.isinf() 方法判断 x 是否是无穷大，如果 x 是正或负无穷大，则返回 True ，否则返回 False 。
print(m.isinf(56))
print(m.isinf(-45.34))
print(m.isinf(+45.34))
print(m.isinf(m.inf))
print(m.isinf(float("nan")))
print(m.isinf(float("inf")))
print(m.isinf(float("-inf")))
print(m.isinf(-m.inf))

# math.isnan() 方法判断数字是否为 NaN（非数字），如果数字是 NaN（不是数字），则返回 True ，否则返回 False 。
print (m.isnan (56))
print (m.isnan (-45.34))
print (m.isnan (+45.34))
print (m.isnan (m.inf))
print (m.isnan (float("nan")))
print (m.isnan (float("inf")))
print (m.isnan (float("-inf")))
print (m.isnan (m.nan))

#  math.isqrt(x) 方法返回 x 的平方根，并将平方根数向下舍入到最接近的整数。
# 数字必须大于等于 0。
print(m.isqrt(4))

# math.ldexp(x, i) 方法返回 x * (2**i)，是math.frexp() 的反函数。
print(m.ldexp(9, 453))
print(m.ldexp(-25, 12))
print(m.ldexp(125, 32))

# math.lgamma(x) 方法返回一个数字的自然对数伽玛值。
# 我们也可以通过使用 math.gamma() 方法找到伽玛值，然后使用 math.log() 方法计算该值的自然对数。
# 伽玛值等于 factorial(x-1)。
print (m.lgamma(7))
print (m.lgamma(-4.2))

#  math.log(x) 方法使用一个参数，返回 x 的对数（默认情况下底为 e，可以通过传递第二个参数（base）来改变底的值 ）。
# 输出一个数字的自然对数
print(m.log(2.7183))
print(m.log(2))
print(m.log(1))

#  math.log10(x) 方法返回 x 以 10 为底的对数。
print(m.log10(2.7183))
print(m.log10(2))
print(m.log10(1))

# math.log1p(x) 方法返回 1+x 的自然对数（以 e 为底）。
print(m.log1p(2.7183))
print(m.log1p(2))
print(m.log1p(1))

#  math.log2(x) 方法返回 x 以 2 为底的对数。
print(m.log2(2.7183))
print(m.log2(2))
print(m.log2(1))

# Python math.perm(n, k) 方法返回不重复且有顺序地从 n 项中选择 k 项的方式总数。
# 是的，这个方法就是用来计算排列的。
# 注意：k 参数是可选的。 如果我们没有设置 k，这个方法将返回 n! （也就是全排列，例如，math.perm(7) 将返回 5040）。
print(m.perm(1,9))

# math.pow(x, y) 方法返回返回 x 的 y 次幂（ 次方 ）。
# 如果 x 为负且 y 不是整数，则返回 ValueError。 该方法会将两个参数转换为浮点数。 math.pow(1.0,x) 或 math.pow(x,0.0)，始终返回 1.0。
print(m.pow(9, 3))

# Python math.prod() 方法用于计算可迭代对象中所有元素的积。
sequence = (2, 2, 2)
print(m.prod(sequence))

# math.radians(x) 方法将角度 x 从角度转换为弧度。
#
# 在math模块中（特别是三角函数相关的函数），都是使用弧度制，所以在使用之前要先将角度数值转化为弧度才能进行运算。
# 另有math.degrees() 方法，可以将弧度值转换为角度。
print(m.radians(180))
print(m.radians(100.03))
print(m.radians(-20))

# math.remainder(x, y) 方法返回 x/y 的余数。
#
# 本函数要求Python的最低版本为python3.7！
#
# 另外：
#
# 在 Python 中，% 运算符是模运算符，它返回除法的余数。例如，10 % 3 的结果是 1，因为 10 除以 3 的商是 3，余数是 1。与此不同的是，math.remainder() 函数返回 IEEE 754 标准下 x/y 的余数，其中 x 和 y 是浮点数。如果 x/y 恰好处于两个连续整数之间的中间，则返回偶数整数。例如，math.remainder(10, 3) 的结果是 -1.0，因为它等于 10 - (-3) * (-4)，而不是等于 10 - (-3) * (-3)。
#
# 总的来说，% 运算符和 math.remainder() 函数都可以用于计算余数，但它们的行为略有不同。如果你需要计算两个浮点数的余数，则应该使用 math.remainder() 函数。
print (m.remainder(9, 2))
print (m.remainder(9, 3))
print (m.remainder(18, 4))
print (m.remainder(23.5, 5))
print (m.remainder(23, 5.5))
print (m.remainder(12.5, 2.5))
print (m.remainder(12, 2))

# math.sin(x) 返回 x 弧度的正弦值。
#
# 要获取指定角度的正弦，必须首先使用 math.radians() 方法将其转换为弧度。
# 导入 math 包
# 输出正弦值
print (m.sin(0.00))
print (m.sin(-1.23))
print (m.sin(10))
print (m.sin(m.pi))
print (m.sin(m.pi/2))

# math.sinh(x) 返回 x 的双曲正弦值。
# 输出双曲正弦值
print(m.sinh(0.00))
print(m.sinh(-23.45))
print(m.sinh(23))
print(m.sinh(1.00))
print(m.sinh(m.pi))

# math.sqrt(x) 方法返回 x 的平方根。
#
# 数字必须大于等于 0。
# 输出平方根
print (m.sqrt(9))
print (m.sqrt(25))
print (m.sqrt(16))

# Python math.tan(x) 返回 x 弧度的正切值。
# 输出正切值
print (m.tan(90))
print (m.tan(-90))
print (m.tan(45))
print (m.tan(60))

# math.tanh(x) 返回 x 的双曲正切值。
# 输出双曲正切值
print(m.tanh(8))
print(m.tanh(1))
print(m.tanh(-6.2))

# math.trunc(x) 方法返回 x 截断整数的部分，即返回整数部分，忽略小数部分。
# math.trunc(x) 方法不会将数字向上/向下舍入到最接近的整数，而只是删除小数。
# 输出整数部分
print(m.trunc(2.77))
print(m.trunc(8.32))
print(m.trunc(-99.29))


# It is over.















































