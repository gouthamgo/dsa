# Greedy Algorithms - Complete Guide

## 🎯 What is Greedy?

Make the locally optimal choice at each step, hoping to find a global optimum.

**Think:** "What's the best choice RIGHT NOW?"

**Visual:**
```
Coin change: Make 67 cents
Coins: [25, 10, 5, 1]

Greedy approach:
1. Take 25 (largest) → 42 left
2. Take 25 → 17 left
3. Take 10 → 7 left
4. Take 5 → 2 left
5. Take 1 → 1 left
6. Take 1 → 0 left

Total: 6 coins ✓
```

...but change that coin set to `[1, 3, 4]` and ask for 6, and greedy takes
`4 + 1 + 1 = 3 coins` while the optimum is `3 + 3 = 2 coins`. **Same algorithm,
different data, wrong answer.** Greedy is a property of the *problem*, not of
the code — which is why the next section matters more than any template.

## 🔍 Trigger Phrases

| Phrase in the problem | What it suggests |
|-----------------------|------------------|
| "maximum / minimum number of ..." | Greedy or DP — check the exchange argument |
| "can you reach ...", "is it possible to ..." | Reachability greedy (Jump Game) |
| "fewest jumps / steps / arrows / removals" | Greedy with a running frontier |
| "as many as possible" | Sort, then take the least-blocking option |
| "at each step you may ..." | Local decision — try greedy first |
| "contiguous subarray with the largest sum" | Kadane |
| "circular route", "start anywhere" | Gas Station's skip-ahead greedy |
| constraints are huge (n ≤ 10⁵ or more) | O(n²) DP is out; greedy or a heap |

Conversely, **n ≤ 100 or n ≤ 1000 is a DP hint** — the setter is allowing an
O(n²) solution because a linear greedy doesn't exist.

## 🧠 When Greedy Works

Greedy works when problem has:
1. **Greedy choice property**: Local optimum → global optimum
2. **Optimal substructure**: Optimal solution contains optimal subsolutions

### The exchange argument (how you actually prove it)

This is the proof you should be able to say out loud in an interview:

```
1. Let OPT be ANY optimal solution.
2. Suppose OPT disagrees with the greedy choice g at the first step.
3. Swap g into OPT, evicting whatever OPT chose instead.
4. Show the result is still FEASIBLE and NO WORSE.
=> Some optimal solution contains g, so committing to g costs nothing.
   Induct on the rest.
```

**Worked instances:**

- **Activity selection** — greedy picks the earliest-finishing activity `g`.
  Any OPT picks some `x` with `end(x) ≥ end(g)`. Swap `g` for `x`: `g` starts
  no later and finishes no later, so nothing else in OPT conflicts. Still
  feasible, still the same size. ∎
- **Kadane** — a running prefix with negative sum can only reduce any sum it
  is attached to, so dropping it is never worse. ∎
- **Gas Station** — if you run dry between `s` and `i`, every station in
  `[s, i]` starts with a *non-negative* tank at or after `s`'s position, so
  each reaches `i` with no more fuel than you had. All of them fail. ∎

### When greedy fails — build the counterexample

If the exchange argument doesn't come out in one sentence, hunt for a case
where a locally good choice forecloses a better future:

| Problem | Greedy attempt | Why it breaks |
|---------|----------------|---------------|
| Coin Change `[1,3,4]`, target 6 | take the largest coin | 4+1+1 = 3 coins vs 3+3 = 2 |
| 0/1 Knapsack | best value-per-weight first | one heavy item can beat two light ones |
| Longest Increasing Subsequence | extend whenever possible | a small early element enables a longer tail |
| Word Break | match the longest prefix | a shorter split may be the only valid one |
| Min Path Sum in a grid | step toward the smaller neighbour | a cheap step can lead into an expensive region |

**Rule of thumb:** if you can't sketch the exchange argument *and* can't build
a counterexample, assume DP and let the constraints confirm it.

## 🔑 Common Greedy Patterns

### 1. Activity Selection
```python
def maxMeetings(intervals):
    # Sort by end time
    intervals.sort(key=lambda x: x[1])

    count = 1
    last_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= last_end:
            count += 1
            last_end = end

    return count
```

Sorting by **end** is load-bearing. Sorting by start or by duration both give
wrong answers — the earliest finisher leaves the most room for everyone else.

### 2. Jump Game
```python
def canJump(nums):
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])

    return True
```

### 3. Gas Station
```python
def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    tank = 0
    start = 0

    for i in range(len(gas)):
        tank += gas[i] - cost[i]

        if tank < 0:
            start = i + 1
            tank = 0

    return start
```

### 4. Kadane's Algorithm (Maximum Subarray)
```python
def maxSubArray(nums):
    best = current = nums[0]

    for num in nums[1:]:
        current = max(num, current + num)   # extend, or restart here
        best = max(best, current)

    return best
```

Seed with `nums[0]`, not `0` — otherwise an all-negative array returns 0
instead of its largest (least negative) element.

### 5. Jump Game II (BFS levels without a queue)
```python
def jump(nums):
    jumps = current_end = farthest = 0

    for i in range(len(nums) - 1):      # stop at n-2: standing on the
        farthest = max(farthest, i + nums[i])   # last index needs no jump

        if i == current_end:            # exhausted this level
            jumps += 1
            current_end = farthest

    return jumps
```

### 6. Partition Labels (last-occurrence sweep)
```python
def partitionLabels(s):
    last = {c: i for i, c in enumerate(s)}   # later writes win = last index

    result, start, end = [], 0, 0
    for i, c in enumerate(s):
        end = max(end, last[c])              # part must stretch this far
        if i == end:                         # nothing inside reappears later
            result.append(end - start + 1)
            start = i + 1

    return result
```

### 7. Task Scheduler (most-frequent-first, closed form)
```python
from collections import Counter

def leastInterval(tasks, n):
    counts = Counter(tasks)
    max_count = max(counts.values())
    num_max = sum(1 for c in counts.values() if c == max_count)

    return max((max_count - 1) * (n + 1) + num_max, len(tasks))
```

```
tasks = AAABBB, n = 2

The most frequent task builds the skeleton:
    A _ _ | A _ _ | A          (max_count - 1) frames of width (n + 1)
    A B _ | A B _ | A B        other tasks fill the idle slots
    ^^^^^^^^^^^^^^^^^^^        = 2*3 + 2 = 8 slots

If there are MORE tasks than idle slots, the CPU never idles
and the answer is just len(tasks) — hence the max().
```

## 🧭 Decision Guide: Greedy vs DP vs Heap

```
Does the answer depend on a choice made much earlier in a way you
can't summarise in O(1) state?
├── YES ──> DP (or backtracking). You must remember alternatives.
└── NO  ──> Can you order the input so the best next pick is obvious?
            ├── YES ──> Sort + greedy sweep      O(n log n)
            └── NO  ──> Is "best next" changing as you go?
                        ├── YES ──> Greedy WITH A HEAP    O(n log n)
                        │           (Task Scheduler, Hand of Straights,
                        │            Meeting Rooms II)
                        └── NO  ──> Single-pass running max/min   O(n)
                                    (Kadane, Jump Game, Gas Station)
```

**Greedy vs DP at a glance:**

| | Greedy | DP |
|---|---|---|
| Decisions | commit, never revisit | explore all, memoise |
| Typical time | O(n) or O(n log n) | O(n²), O(n·k) |
| Typical space | O(1) | O(n) or O(n·k) |
| Correctness | needs a proof | correct by construction |
| Failure mode | silently wrong answers | TLE / MLE |

**A useful escalation ladder:** try O(n) greedy → if you find a
counterexample, try greedy + heap → if that breaks too, write the DP.

## ⚡ Complexity Analysis

| Problem | Time | Space | Mechanism |
|---------|------|-------|-----------|
| Maximum Subarray (Kadane) | O(n) | O(1) | running sum, reset on negative |
| Jump Game | O(n) | O(1) | running max reach |
| Jump Game II | O(n) | O(1) | BFS levels, two boundaries |
| Gas Station | O(n) | O(1) | one pass + skip-ahead |
| Partition Labels | O(n) | O(1) | 26-letter last-index map |
| Task Scheduler (formula) | O(n) | O(1) | counting only |
| Task Scheduler (heap) | O(T log 26) | O(1) | simulation |
| Activity Selection / Min Arrows | O(n log n) | O(1) | sort by end |
| Hand of Straights | O(n log n) | O(n) | min-heap of distinct cards |

Anything with a sort is O(n log n); the greedy sweep itself is almost always
O(n) with O(1) extra space. That gap — linear scan, constant memory — is what
makes greedy worth proving.

## 🔬 Worked Example: Gas Station, Traced

```
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
net  = [-2, -2, -2, 3, 3]      net[i] = gas[i] - cost[i]
```

**Step 0 — feasibility:** `sum(gas) = 15`, `sum(cost) = 15`. Total net is 0
(≥ 0), so a solution exists. If it were negative, return -1 immediately.

**Step 1 — one pass, resetting whenever the tank goes negative:**

```
i=0: tank = 0 + (-2) = -2   <0  -> start = 1, tank = 0
     "station 0 can't even reach station 1"

i=1: tank = 0 + (-2) = -2   <0  -> start = 2, tank = 0
     "station 1 can't reach station 2 either"

i=2: tank = 0 + (-2) = -2   <0  -> start = 3, tank = 0
     "and neither can station 2"

i=3: tank = 0 + 3    =  3   ok  -> keep going, start stays 3

i=4: tank = 3 + 3    =  6   ok  -> keep going, start stays 3

Answer: start = 3
```

**Verify by walking the circle from station 3:**
```
station 3: tank 0 + 4 gas = 4, pay 1 cost  -> 3
station 4: tank 3 + 5 gas = 8, pay 2 cost  -> 6
station 0: tank 6 + 1 gas = 7, pay 3 cost  -> 4
station 1: tank 4 + 2 gas = 6, pay 4 cost  -> 2
station 2: tank 2 + 3 gas = 5, pay 5 cost  -> 0  ✓ back at start
```

**Why one pass is enough** (this is the exchange argument, concretely): when
the tank went negative at `i=2` having started at 2, we learned station 2
fails. But we *also* already knew stations 0 and 1 fail — a start at 0 arrives
at station 2 with a tank ≤ 0, so it can only do worse than starting fresh at 2.
Every station in `[start, i]` is eliminated by a single failure, which is why
we jump `start` all the way to `i + 1` instead of retrying `start + 1`.

## 🚨 Common Pitfalls

1. **Using greedy without proving it.** The failure mode is a *plausible wrong
   answer*, not a crash. Always test the adversarial case: what if one big
   early item blocks many small later ones?

2. **Kadane seeded with 0.** `best = current = 0` returns 0 for
   `[-3, -1, -2]`; the correct answer is -1. Seed with `nums[0]`.

3. **Jump Game II looping to `n-1`.** Iterating over the last index can add a
   phantom jump. Stop at `n-2`.

4. **Gas Station without the total check.** The skip-ahead loop always returns
   *some* index; only `sum(gas) >= sum(cost)` certifies it is valid.

5. **Sorting by the wrong key.** By start, by duration, by size — all feel
   reasonable and all break activity selection. Sort by **end**.

6. **Off-by-one in "touching" comparisons.** `start >= last_end` (half-open,
   back-to-back allowed) vs `start > last_end` (closed). Decide per problem.

7. **Task Scheduler forgetting the `max(..., len(tasks))`.** With many
   distinct tasks the CPU never idles and the formula under-counts.

8. **Partition Labels using first occurrence.** The dict comprehension
   `{c: i for i, c in enumerate(s)}` works precisely *because* later writes
   overwrite earlier ones, leaving the last index.

9. **Mutating while iterating in heap-based greedy.** In Hand of Straights,
   only the current minimum may legally hit zero mid-run; if a larger card
   runs out, the group is impossible — return False rather than popping.

10. **Assuming greedy is faster so it must be right.** Speed is the payoff,
    not the justification.

## ⚡ Key Problems

**Medium:**
- Maximum Subarray ⭐ — Kadane; the single most reused greedy in interviews
- Jump Game ⭐ — running max reach
- Jump Game II ⭐ — the same array, now counting BFS levels
- Gas Station ⭐ — skip-ahead greedy on a circular route
- Hand of Straights — forced grouping from the smallest card, min-heap
- Merge Triplets to Form Target Triplet — filter, then take the max per slot
- Partition Labels ⭐ — last-occurrence sweep

**Hard:**
- Valid Parenthesis String — track a *range* `[lo, hi]` of possible open counts
- Candy — two passes, left-to-right then right-to-left
- Minimum Number of Refueling Stops — max-heap of fuel passed but not used

⭐ = must-know. Maximum Subarray, Jump Game II, Gas Station, and Partition
Labels cover the four shapes: running accumulator, frontier expansion,
skip-ahead reset, and last-occurrence sweep.

## 🎨 How to Identify Greedy

Look for:
- ✅ "Maximum/Minimum number of..."
- ✅ Scheduling/interval problems
- ✅ Sorting helps
- ✅ Simple, intuitive optimal choice

## 💡 Greedy vs DP

**Greedy**: Make best local choice
- Faster: O(n) or O(n log n)
- Simpler code
- Doesn't always work!

**DP**: Consider all choices
- Slower: O(n²) or more
- Always correct
- More complex

## 💡 Pro Tips

1. **Try sorting first** (by start, end, value, etc.)
2. **Prove greedy works** before implementing
3. **If greedy fails, try DP**
4. **Draw examples** to verify
5. **Say the exchange argument out loud.** If you can't finish the sentence
   "swapping the greedy choice into any optimal solution keeps it optimal
   because...", you don't have a proof yet.
6. **Test three adversarial shapes**: all-negative input, one dominant early
   element, and many ties. Most broken greedies die on one of them.

Time: Usually O(n) or O(n log n)
Space: Usually O(1)

## 🚀 Next Steps

1. Study the `template.py` file — Kadane, both jump games, gas station, partition labels, task scheduler, activity selection
2. Start with **Maximum Subarray** (Kadane is the gateway greedy)
3. Then **Jump Game** → **Jump Game II** (reachability, then counting levels)
4. Then **Gas Station** and **Partition Labels** (the two cleverest one-passers)
5. Finish with **Valid Parenthesis String** — greedy over a *range* of states

---
**Greedy is simple and fast when it works!** 🎯
