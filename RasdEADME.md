# Exercises and Answers

## Exercises

### Exercise 1: Liar’s Dice – Probability 🎲
Jack is playing a game of Liar’s Dice and rolls five dice. He gets five of a kind (all dice showing the same number).

💡 Hint: The formula for calculating the probability of rolling five of a kind is:

\[ P = \frac{\text{favorable outcomes}}{\text{total possible outcomes}} \]

where:

- The number of total possible outcomes is \( 6^5 \) (since each of the 5 dice has 6 sides).
- The number of favorable outcomes is 6 (since any of the 6 numbers could be the repeated one).

✏ Unfinished Code:
```python
total_possible_rolls = 6 ** 5  # 6 sides per die, 5 dice rolled
favorable_outcomes = 6  # Any of the 6 numbers can be the repeated one

probability = _______________  # Fill in the correct calculation

print("Chance of rolling five of a kind:", probability)
```

---

### Exercise 2: Movie Tickets – Discount Calculation 🎟️
Jack and his friends are buying movie tickets. The theater gives discounts:

- Student tickets get 20% off.
- Senior tickets get 30% off.
- Regular tickets have no discount.

The regular price of a ticket is $12. Jack’s group buys the following tickets:

- 2 regular
- 2 student
- 1 senior

✏ Unfinished Code:
```python
ticket_price = 12  # Regular ticket price
tickets = ["regular", "student", "regular", "senior", "student"]  # Types of tickets bought

total_cost = 0

for ticket in tickets:
    if ticket == "student":
        total_cost += _______________  # Apply student discount
    elif ticket == "senior":
        total_cost += _______________  # Apply senior discount
    else:
        total_cost += ticket_price  # Regular price

print("Total cost for movie tickets: $", round(total_cost, 2))
```

---

### Exercise 3: Factory Quality Check 🏭
A factory produces metal parts, each tested for quality. If a part has an even quality score and is below 100, it is considered defective.

Given a list of quality scores, count how many defective products exist.

✏ Unfinished Code:
```python
products = [102, 98, 110, 120, 85, 99, 105, 95]  # Quality scores of different products
passing_threshold = 100

defect_count = 0

for product in products:
    if _______________:  # Check for even quality scores below threshold
        defect_count += 1

print("Number of defective products:", defect_count)
```

---

### Exercise 4: The Physics of Free Fall 🌍
A scientist drops an object from rest (starting velocity = 0) and wants to calculate its velocity and distance fallen after 3 seconds.

💡 Hint: Use these physics formulas:

\[ v = v_0 + g t \]
\[ d = v_0 t + \frac{1}{2} g t^2 \]

where:

- \( v \) = final velocity (m/s)
- \( v_0 \) = initial velocity (m/s) (starts from rest)
- \( g \) = gravity (9.81 m/s²)
- \( t \) = time (seconds)

✏ Unfinished Code:
```python
import math

g = 9.81  # Gravity (m/s^2)
time = 3  # Time in seconds
initial_velocity = 0  # Starts from rest

final_velocity = _______________  # Apply velocity formula
distance_fallen = _______________  # Apply distance formula

print("Velocity after", time, "seconds:", round(final_velocity, 2), "m/s")
print("Distance fallen after", time, "seconds:", round(distance_fallen, 2), "meters")
```

---

## Answers

### Exercise 1: Liar’s Dice – Probability 🎲
📌 Completed Code:
```python
total_possible_rolls = 6 ** 5  # 6 sides per die, 5 dice rolled
favorable_outcomes = 6  # Any of the 6 numbers can be the repeated one

probability = favorable_outcomes / total_possible_rolls

print("Chance of rolling five of a kind:", probability)
```
📌 Expected Output:
```
Chance of rolling five of a kind: 0.004629629629629629
```

---

### Exercise 2: Movie Tickets – Discount Calculation 🎟️
📌 Completed Code:
```python
ticket_price = 12  # Regular ticket price
tickets = ["regular", "student", "regular", "senior", "student"]  # Types of tickets bought

total_cost = 0

for ticket in tickets:
    if ticket == "student":
        total_cost += ticket_price * 0.8  # Apply student discount (20% off)
    elif ticket == "senior":
        total_cost += ticket_price * 0.7  # Apply senior discount (30% off)
    else:
        total_cost += ticket_price  # Regular price

print("Total cost for movie tickets: $", round(total_cost, 2))
```
📌 Expected Output:
```
Total cost for movie tickets: $50.4
```

---

### Exercise 3: Factory Quality Check 🏭
📌 Completed Code:
```python
products = [102, 98, 110, 120, 85, 99, 105, 95]  # Quality scores of different products
passing_threshold = 100

defect_count = 0

for product in products:
    if product % 2 == 0 and product < passing_threshold:  # Check even quality scores below threshold
        defect_count += 1

print("Number of defective products:", defect_count)
```
📌 Expected Output:
```
Number of defective products: 3
```

---

### Exercise 4: The Physics of Free Fall 🌍
📌 Completed Code:
```python
import math

g = 9.81  # Gravity (m/s^2)
time = 3  # Time in seconds
initial_velocity = 0  # Starts from rest

final_velocity = initial_velocity + g * time
distance_fallen = initial_velocity * time + 0.5 * g * (time ** 2)

print("Velocity after", time, "seconds:", round(final_velocity, 2), "m/s")
print("Distance fallen after", time, "seconds:", round(distance_fallen, 2), "meters")
```
📌 Expected Output:
```
Velocity after 3 seconds: 29.43 m/s
Distance fallen after 3 seconds: 44.15 meters
```
