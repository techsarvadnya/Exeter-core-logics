# Exeter-core-logics
Daily logic building and Python mini-experiments for Exeter profile.

----------------------------------------------------------------------------------------------------

# Phoenix-Learn Core Logic Suite 🚀

An educational logic engine designed to handle quiz scoring, enrollment automation, and progression analytics. Built for Phillips Exeter Academy (PEA) portfolio showcasing core Python fundamental architectures.

---

## 🛠️ Logic Breakdown & Architecture

### Module 1: Quiz Evaluator (`quiz_evaluator.py`)
* **Purpose:** Evaluates dynamic quiz performance against multi-tiered user membership access models.
* **Core Function:** `evaluate_quiz(correct_answers, total_questions, plan_type)`
* **Key Logic Systems:**
  * **Relative Math:** Calculates percentage `(correct / total) * 100` instead of static bounds to support variable total questions.
  * **Compound Gate (`and` operator):** Requires high performance (≥ 80%) AND premium plan (`"Pro"`) simultaneously before granting honors.
  * **Branching Strategy:** Uses `if-elif-else` waterfall logic for clear evaluation boundaries.


----------------------------------------------------------------------------------------------------


---

### Module 2: Twin Age Calculator (`Average_Age_Calculator.py`)
* **Purpose:** Solves algebraic group-average isolation problems dynamically.
* **Core Function:** `calculate_twin_age(average_age, total_people, elder_age)`
* **Key Logic Systems:**
  * **Mathematical Reverse-Engineering:** Reconstructs the total sum of elements via Total = Average * Count.
  * **Variable Isolation:** Subtracts known outliers to isolate dynamic twin parameters.
  * **Equal Allocation:** Computes division step to resolve multi-variable constraints linearly.
----------------------------------------------------------------------------------------------------

---

### Module 3: Power Saver Engine (`battery_gate.py`)
* **Purpose:** Monitors energy thresholds to switch system execution modes dynamically.
* **Core Function:** `battery_gate(level)`
* **Key Logic Systems:**
  * **Boundary Logic ($\le$ Operator):** Evaluates inclusive critical limits ($\le 20\%$) to enforce low-power state transitions.
  * **Binary Decision States:** Operates a deterministic two-path state model (`if-else`) for predictable runtime behavior.

----------------------------------------------------------------------------------------------------

