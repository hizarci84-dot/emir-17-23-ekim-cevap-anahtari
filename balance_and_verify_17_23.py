# -*- coding: utf-8 -*-
import re
import random
from questions_17_23_data import QUESTIONS_17_23

# Fix Q90 first
for q in QUESTIONS_17_23:
    if q["no"] == 90:
        q["text"] = (
            "• Eski nesil bir fırın her bir saatte 9<sup>2</sup> Wh elektrik enerjisi tüketmektedir.<br/>"
            "• A++ enerji sınıfı yeni nesil fırın ise her bir saatte 2 · 3<sup>3</sup> Wh elektrik "
            "enerjisi tüketmektedir.<br/>"
            "<b>125 saatlik kullanımda eski fırın yerine yeni fırının tercih edilmesi toplam "
            "15<sup>n</sup> Wh enerji tasarrufu sağladığına göre n kaçtır?</b>"
        )
        q["options"] = [
            ("A", "2"),
            ("B", "3"),
            ("C", "4"),
            ("D", "5"),
            ("E", "6"),
        ]
        q["answer"] = "B"

letters = ["A", "B", "C", "D", "E"]

def make_window_around(correct_val, target_pos, q_no):
    """
    Given the correct answer string and desired index target_pos (0..4),
    generate 5 strictly ordered options where index target_pos is correct_val.
    """
    # Case 1: Pure integer string like "10", "144", "1500", "8000", "160", "300"
    if re.fullmatch(r"\d+", correct_val):
        val = int(correct_val)
        # Determine natural step based on value
        if val <= 15:
            # Ensure lowest option >= 1
            min_pos = 0
            while val - target_pos < 1 and target_pos > 0:
                target_pos -= 1
            step = 1
        elif val in (64, 128):
            # Powers of 2
            exps = [val // (2 ** (target_pos - i)) if i <= target_pos else val * (2 ** (i - target_pos)) for i in range(5)]
            if all(x >= 2 for x in exps):
                return [str(x) for x in exps], target_pos
            step = 16
        elif val == 81:
            step = 27
            while val - target_pos * step <= 0:
                target_pos -= 1
        elif val == 96:
            step = 16
        elif val in (144, 225, 400):
            step = 24 if val == 144 else (25 if val == 225 else 50)
        elif val in (90, 100, 300, 800):
            step = 10 if val == 90 else (50 if val == 100 else (50 if val == 300 else 100))
        elif val in (1250, 1500, 2000, 8000, 10000):
            step = 250 if val in (1250, 1500) else (500 if val == 2000 else 1000)
        else:
            step = 20
        vals = [str(val + (i - target_pos) * step) for i in range(5)]
        return vals, target_pos

    # Case 2: Base^exp like "2<sup>16</sup>", "10<sup>8</sup>", "3<sup>-2</sup>"
    m = re.fullmatch(r"(\d+)<sup>(-?\d+)</sup>", correct_val)
    if m:
        base = int(m.group(1))
        exp = int(m.group(2))
        # Special case: if base in (12, 15, 18) and exp in (2, 3), step base by 3
        if base in (15, 18) and exp in (2, 3):
            while base - target_pos * 3 <= 3:
                target_pos -= 1
            vals = [f"{base + (i - target_pos) * 3}<sup>{exp}</sup>" for i in range(5)]
            return vals, target_pos
        vals = [f"{base}<sup>{exp + (i - target_pos)}</sup>" for i in range(5)]
        return vals, target_pos

    return None, target_pos


random.seed(42)
for day in range(1, 7):
    day_qs = [q for q in QUESTIONS_17_23 if q["day"] == day]
    # Questions whose options are custom expressions/sentences keep their original option list
    # unless shifted by make_window_around
    fixed_qs = []
    shiftable_qs = []
    for q in day_qs:
        cur_ans = q["answer"]
        correct_val = q["options"][letters.index(cur_ans)][1]
        test_vals, _ = make_window_around(correct_val, 2, q["no"])
        if test_vals is None or q.get("options_vertical"):
            fixed_qs.append(q)
        else:
            shiftable_qs.append(q)

    # Count already used letters in fixed_qs
    target_counts = {L: 3 for L in letters}
    for q in fixed_qs:
        L = q["answer"]
        if target_counts[L] > 0:
            target_counts[L] -= 1

    pool = []
    for L in letters:
        pool.extend([L] * target_counts[L])
    while len(pool) < len(shiftable_qs):
        pool.append(random.choice(letters))
    random.shuffle(pool)

    for q, target_L in zip(shiftable_qs, pool):
        cur_ans = q["answer"]
        correct_val = q["options"][letters.index(cur_ans)][1]
        t_pos = letters.index(target_L)
        new_vals, actual_pos = make_window_around(correct_val, t_pos, q["no"])
        if new_vals is not None:
            q["options"] = [(letters[i], new_vals[i]) for i in range(5)]
            q["answer"] = letters[actual_pos]

for day in range(1, 7):
    day_qs = [q for q in QUESTIONS_17_23 if q["day"] == day]
    counts = {L: sum(1 for q in day_qs if q["answer"] == L) for L in letters}
    print(f"Day {day}: {counts}")
