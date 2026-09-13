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

---

### Module 4: Cart Discount Engine (`cart_discount.py`)
* **Purpose:** Automates dynamic price reductions based on order value thresholds.
* **Core Function:** `apply_discount(cart_total)`
* **Key Logic Systems:**
  * **Relational Threshold Checking ($\ge$):** Determines eligibility by evaluating minimum required order value ($100).
  * **Percentage Factor Calculation:** Dynamically computes discounted totals using fractional multipliers (`cart_total * 0.80`).

----------------------------------------------------------------------------------------------------

---

### Module 5: Central Dashboard Engine (`dashboard_engine.py`)
* **Purpose:** Orchestrates multi-system status evaluation through a single master control function.
* **Core Function:** `student_dashboard_engine(battery_level, plan_type, score, attendance)`
* **Key Logic Systems:**
  * **Modular System Architecture:** Integrates micro-functions (`battery_gate`, `check_plan`, `issue_certificate`) to achieve clean separation of concerns.
  * **Pipeline Parameter Delegation:** Forwards dynamic runtime arguments seamlessly to underlying conditional validation logic.

----------------------------------------------------------------------------------------------------

---

### Module 6: Subscription Entitlement Engine (`plan_gate.py`)
* **Purpose:** Controls feature availability and course access dynamically based on subscription tiers.
* **Core Function:** `check_plan(user_plan)`
* **Key Logic Systems:**
  * **String Equality Gates (`==` Operator):** Performs precise text evaluation to validate dynamic user privileges.
  * **Waterfall Decision Tree (`if-elif-else`):** Establishes explicit boundaries between premium, basic, and fallback account states.

----------------------------------------------------------------------------------------------------

---

### Module 7: Smart Admission Engine (`smart_admission.py`)
* **Purpose:** Streamlines enrollment eligibility and dynamic financial aid evaluation.
* **Core Function:** `calculate_admission(grade, score, fees)`
* **Key Logic Systems:**
  * **Categorical Qualification:** Maps dynamic user grades to educational tiers using string equality matching.
  * **Compound Aid Allocation:** Leverages dual boolean constraints (`score >= 90 and fees > 5000`) to trigger automated fee deductions.
  * **Formatted System Outputs:** Aggregates variable states into clean status reports using inline F-string interpolation.
