# Linear vs Log Returns
## Linear vs Log Returns

python
```
X_log = np.log(1 + X_lin)
mu = X_log.mean().values
Sigma = X_log.cov().values
```

In finance, transforming **linear (arithmetic) returns** to **log returns** is a common practice. Let's break down the reasons and the **advantages** of computing:

```python
X_log = np.log(1 + X_lin)
```

### 🔁 Why compute log returns from linear returns?

This transformation is based on the formula:

$$
r_{\text{log}} = \ln(1 + r_{\text{linear}})
$$

Where:

* $r_{\text{linear}}$: linear (arithmetic) return
* $r_{\text{log}}$: continuously compounded (log) return

---

### ✅ Advantages of using **log returns**:

#### 1. **Time Additivity**

* **Log returns are additive over time**, which simplifies analysis.

  Example:

  $$
  \ln\left(\frac{P_2}{P_0}\right) = \ln\left(\frac{P_2}{P_1} \cdot \frac{P_1}{P_0} \right) = \ln\left(\frac{P_2}{P_1}\right) + \ln\left(\frac{P_1}{P_0}\right)
  $$

* This property is useful when aggregating returns over multiple periods.

#### 2. **Normality Assumption**

* Log returns are **closer to normally distributed** than linear returns, especially for daily/short-term data.
* This makes them more suitable for **statistical modeling**, **risk management**, and **portfolio optimization**.

#### 3. **Better for Multivariate Statistics**

* When you're computing:

  ```python
  mu = X_log.mean().values
  Sigma = X_log.cov().values
  ```

  you're likely planning to use them for **multivariate analysis** (e.g., mean-variance optimization, multivariate forecasting).
* Log returns have **more stable variance-covariance structures**.

#### 4. **Ease of Derivation in Calculus**

* Log returns arise naturally in models using calculus (e.g., **Black-Scholes**, **Ito calculus** in stochastic processes).

---

### 🚫 When not to use log returns?

* For very large time intervals or extremely volatile assets, the difference between log and linear returns can be significant.
* Investors often **think in terms of percent gain/loss (linear)**, so for reporting or user interfaces, linear returns are more intuitive.

---

### Summary Table

| Property                          | Linear Returns    | Log Returns   |
| --------------------------------- | ----------------- | ------------- |
| Additive over time                | ❌                 | ✅             |
| Approximate normal distribution   | ❌ (less accurate) | ✅             |
| Suitable for statistical modeling | ⚠️ (OK)           | ✅             |
| Intuitive to interpret            | ✅ (in %)          | ❌ (log scale) |

---

### Final Thought

So, in your code:

```python
mu = X_log.mean().values
Sigma = X_log.cov().values
```

This is probably part of a **multivariate model** (e.g., mean-variance optimization, portfolio simulation), where log returns are a better fit due to their statistical and mathematical properties.
