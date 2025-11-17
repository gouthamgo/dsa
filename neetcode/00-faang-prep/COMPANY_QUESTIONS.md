# 🏢 Company-Specific Interview Questions

**What each FAANG company asks + How they evaluate + What they prioritize**

> Based on 2025 interview data, recent candidate experiences, and company-specific patterns.

---

## 🎯 Quick Company Comparison

```
Company      Difficulty  Focus Areas           Interview Style
──────────────────────────────────────────────────────────────
Google       ⭐⭐⭐⭐⭐  Algorithms            Very algorithmic
                       Complexity            Clean code critical
                       System design         Googleyness important

Meta         ⭐⭐⭐⭐    Graphs/Trees          Move fast mentality
                       System design         Product thinking
                       Behavioral            Impact-focused

Amazon       ⭐⭐⭐      Arrays/Strings        Leadership Principles
                       Basic DSA             Behavioral heavy (50%)
                       Bar raiser            Very structured

Apple        ⭐⭐⭐⭐    Domain-specific       Attention to detail
                       Low-level             Quality over speed
                       Design                Practical problems

Netflix      ⭐⭐⭐⭐⭐  Senior-focused        Freedom & Responsibility
                       Independent           Judgment critical
                       Context > Control      High bar

Microsoft    ⭐⭐⭐      DSA fundamentals      Growth mindset
                       System design         Collaboration
                       Behavioral            Learn-it-all culture
```

---

## 🔴 Google

### Interview Structure (L3-L5)
```
Phone Screen (1 round, 45 min):
└─ 1-2 DSA problems (medium difficulty)

Onsite (4-5 rounds, 45 min each):
├─ Coding Round 1: DSA problem
├─ Coding Round 2: DSA problem
├─ System Design (L4+): Design at scale
├─ Behavioral/Googleyness: Culture fit
└─ Optional: Leadership round (L5+)
```

### What Google Prioritizes

**1. Algorithmic Thinking**
```
They want to see:
✅ Optimal solution (not just working solution)
✅ Clean, production-quality code
✅ Edge case handling
✅ Complexity analysis (must be accurate!)
```

**2. "Googleyness"**
```
What it means:
- Comfort with ambiguity
- Collaborative
- Intellectually curious
- Conscientious
- Humble but confident
```

### Common Google Questions

#### **DSA (Phone + Onsite)**

**Easy-Medium (Phone Screen):**
```
1. Two Sum / Three Sum variations
2. Valid Parentheses
3. Merge Intervals
4. Binary Tree Level Order Traversal
5. Longest Substring Without Repeating Characters
```

**Medium-Hard (Onsite):**
```
1. Median of Two Sorted Arrays
   - They LOVE binary search problems
   - Expect O(log(min(m,n))) solution

2. Serialize and Deserialize Binary Tree
   - Multiple approaches discussion
   - Trade-offs between space and time

3. Word Ladder II
   - BFS + backtracking
   - Expect optimal solution

4. Regular Expression Matching
   - DP solution required
   - Must handle edge cases

5. Trapping Rain Water
   - Multiple approaches
   - Explain each approach's complexity
```

**Google-Specific Pattern: They love questions that have multiple solutions of increasing optimization**

Example - Container With Most Water:
```python
# Brute force: O(n²)
def maxArea_bruteforce(height):
    max_area = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)
    return max_area

# Optimized: O(n) - THIS IS WHAT THEY WANT
def maxArea_optimal(height):
    """
    Two pointers approach
    Key insight: Move the pointer with smaller height
    """
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        # Calculate current area
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)

        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# YOU MUST EXPLAIN WHY THIS IS OPTIMAL
```

#### **System Design (L4+ Onsite)**

Google focuses on:
- Scalability to billions of users
- Global distribution
- Consistency vs availability trade-offs

**Common questions:**
```
1. Design Google Drive / Dropbox
   Focus: File sync, conflict resolution, chunks

2. Design YouTube
   Focus: Video transcoding, CDN, recommendations

3. Design Google Search autocomplete
   Focus: Trie, caching, ranking

4. Design Google Maps
   Focus: Geospatial indexing, routing algorithms

5. Design Gmail
   Focus: Email storage, search, spam filtering
```

### Google Interview Tips

**DO:**
```
✅ Start with clarifying questions
✅ Discuss multiple approaches before coding
✅ Write clean, readable code (they care A LOT)
✅ Explain your complexity analysis clearly
✅ Test with multiple examples
✅ Show intellectual curiosity
```

**DON'T:**
```
❌ Jump straight to code
❌ Write messy code (even if correct)
❌ Ignore edge cases
❌ Give approximate complexity (must be exact!)
❌ Be arrogant or dismissive
```

### Real Google Behavioral Questions

**Googleyness Round:**
```
1. "Tell me about a time you had to work with ambiguous requirements"
   → Show comfort with uncertainty, clarifying questions

2. "Describe a situation where you had to learn something quickly"
   → Show intellectual curiosity, learning process

3. "Tell me about a time you helped a teammate"
   → Show collaboration, humility

4. "Describe a project where you took initiative"
   → Show proactive thinking

5. "Tell me about a technical decision you regret"
   → Show learning, humility, growth
```

**How to answer for Google:**
```
Focus on:
- How you think (process > outcome)
- Collaboration and teamwork
- Data-driven decisions
- Learning and growth
- Humility ("I learned...", not "I was right")
```

---

## 🔵 Meta (Facebook)

### Interview Structure
```
Phone Screen (1-2 rounds, 45 min each):
├─ Coding: 1-2 problems
└─ Behavioral: Quick culture questions

Onsite (4-5 rounds):
├─ Coding Round 1 (45 min)
├─ Coding Round 2 (45 min)
├─ System Design (45-60 min)
├─ Behavioral (30-45 min)
└─ Engineering Chat (informal)
```

### What Meta Prioritizes

**1. Move Fast**
```
They want:
✅ Working solution quickly
✅ Iterative approach (not perfect first time)
✅ Bias for action
✅ Pragmatic trade-offs
```

**2. Impact**
```
They want to hear:
✅ Metrics and measurable outcomes
✅ User impact
✅ Business value
✅ Scale of your work
```

### Common Meta Questions

#### **DSA - Meta Loves:**
- **Graphs** (especially BFS/DFS)
- **Trees** (all types)
- **Strings** (manipulation, parsing)
- **Medium difficulty** (not super hard)

**Top Meta Questions:**
```
1. Valid Parentheses (Easy warmup)

2. Binary Tree Right Side View ⭐⭐⭐
   - BFS level order traversal
   - Very common at Meta!

3. Clone Graph ⭐⭐⭐
   - DFS/BFS with hash map
   - Frequently asked

4. Minimum Remove to Make Valid Parentheses
   - Stack usage
   - String manipulation

5. Dot Product of Two Sparse Vectors
   - Optimize for sparse data
   - Real-world application

6. k Closest Points to Origin
   - Heap usage
   - Multiple approaches

7. Buildings With an Ocean View
   - Stack pattern
   - Linear scan optimization

8. Subarray Sum Equals K
   - Prefix sum + hash map
   - Common pattern at Meta
```

**Meta Pattern Example - Clone Graph:**

```python
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    """
    Meta loves this question!

    Approach: DFS with hash map to track cloned nodes

    Time: O(V + E)
    Space: O(V) for recursion + hash map
    """
    if not node:
        return None

    # Hash map: original node -> cloned node
    cloned = {}

    def dfs(node):
        if node in cloned:
            return cloned[node]

        # Clone current node
        copy = Node(node.val)
        cloned[node] = copy

        # Clone neighbors
        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node)

# YOU: "This uses DFS to traverse the graph.
#       The hash map prevents infinite loops and
#       ensures each node is cloned exactly once.
#
#       Time: O(V + E) - visit each vertex and edge once
#       Space: O(V) - hash map stores all vertices"

# INTERVIEWER: "Can you do BFS instead?"
# YOU: "Yes, let me show you..."

from collections import deque

def cloneGraph_bfs(node):
    """BFS approach - same complexity"""
    if not node:
        return None

    cloned = {node: Node(node.val)}
    queue = deque([node])

    while queue:
        curr = queue.popleft()

        for neighbor in curr.neighbors:
            if neighbor not in cloned:
                cloned[neighbor] = Node(neighbor.val)
                queue.append(neighbor)

            cloned[curr].neighbors.append(cloned[neighbor])

    return cloned[node]
```

#### **System Design**

**Meta-Specific Focus:**
```
They care about:
- Social graph problems
- Real-time updates
- News feed algorithms
- Content moderation at scale
```

**Common Questions:**
```
1. Design Facebook News Feed ⭐⭐⭐ (Most common!)
2. Design Instagram
3. Design Facebook Messenger
4. Design Facebook Groups
5. Design Notification System
```

### Meta Interview Tips

**DO:**
```
✅ Start coding quickly (after brief discussion)
✅ Show you can iterate (version 1, then improve)
✅ Talk about impact and metrics
✅ Demonstrate product thinking
✅ Show you can ship fast
```

**DON'T:**
```
❌ Over-engineer (they value pragmatism)
❌ Spend too long planning (bias for action!)
❌ Focus only on technical perfection
❌ Forget to mention user impact
```

### Real Meta Behavioral Questions

**Focus on Impact:**
```
1. "Tell me about your most impactful project"
   → Quantify: users affected, metrics improved, revenue impact

2. "Describe a time you moved fast and broke things"
   → Show iterative approach, learning from mistakes

3. "Tell me about a time you had to make a decision with incomplete information"
   → Bias for action, practical trade-offs

4. "What's the biggest technical risk you've taken?"
   → Innovation, measured risk-taking

5. "Tell me about a time you advocated for the user"
   → Product thinking, user empathy
```

**STAR Answer for Meta:**
```
Situation: "We were building a feature for 10M users..."
Task: "I needed to decide between perfect solution (3 months)
       vs good solution (3 weeks)..."
Action: "I chose to ship MVP in 3 weeks because [data/reasoning]
        - Built monitoring to track metrics
        - Set up A/B test
        - Iterated based on feedback"
Result: "Shipped in 3 weeks, reached 2M users in first month,
        95% satisfaction, added remaining features in next sprint.
        Total: 4 weeks vs originally planned 3 months."
```

---

## 🟠 Amazon

### Interview Structure
```
Phone Screen (1 round, 1 hour):
└─ 1-2 coding problems + LP questions

Onsite "Loop" (5-6 rounds, 1 hour each):
├─ Coding Round 1: DSA + LP
├─ Coding Round 2: DSA + LP
├─ System Design (L5+): LLD or HLD
├─ Behavioral/LP Round 1
├─ Behavioral/LP Round 2
└─ Bar Raiser: Toughest round (mixed)
```

### What Amazon Prioritizes

**1. Leadership Principles (50% of Interview!)**
```
THIS IS CRITICAL:
- Every answer MUST map to LPs
- Interviewers are assigned specific LPs to test
- You need 2-3 stories per LP
- "Bar raiser" looks for LP alignment
```

**2. Practical Coding**
```
Amazon DSA is easier than Google/Meta, but:
- Must work correctly
- Must handle edge cases
- Code quality matters
- Prefer practical solutions over clever ones
```

### Common Amazon Questions

#### **DSA - Amazon Favorites:**
```
Arrays and Strings (most common):
1. Two Sum
2. Best Time to Buy and Sell Stock
3. Merge Intervals
4. Longest Substring Without Repeating Characters
5. Valid Parentheses
6. Rotate Array
7. Product of Array Except Self

Trees and Graphs:
8. Lowest Common Ancestor of Binary Tree
9. Number of Islands
10. Binary Tree Level Order Traversal

Amazon Specific:
11. Amazon Fulfillment Center Problems
    - Optimize warehouse layout
    - Package delivery routes
    - Inventory management

12. Prime Video Problems
    - Content recommendation
    - Video quality optimization
```

**Amazon Pattern - They love practical problems:**

```python
# Example: "Design an inventory management system"
# This is more practical than theoretical

class InventorySystem:
    """
    Amazon loves this type of question - practical OOP

    YOU: "Let me design an inventory system that:
          - Tracks product quantities
          - Handles reservations (cart items)
          - Manages restocking
          - Thread-safe for concurrent access"
    """

    def __init__(self):
        self.inventory = {}  # product_id -> quantity
        self.reserved = {}   # product_id -> reserved_quantity
        from threading import Lock
        self.lock = Lock()

    def add_product(self, product_id, quantity):
        """Add stock - maps to 'Deliver Results' LP"""
        with self.lock:
            if product_id not in self.inventory:
                self.inventory[product_id] = 0
            self.inventory[product_id] += quantity

    def reserve(self, product_id, quantity):
        """
        Reserve items for cart
        Maps to: 'Customer Obsession' (don't sell what we don't have)
        """
        with self.lock:
            available = self.inventory.get(product_id, 0)
            currently_reserved = self.reserved.get(product_id, 0)

            if available - currently_reserved >= quantity:
                self.reserved[product_id] = currently_reserved + quantity
                return True
            return False

    def complete_order(self, product_id, quantity):
        """
        Complete purchase
        Maps to: 'Deliver Results'
        """
        with self.lock:
            if self.reserved.get(product_id, 0) >= quantity:
                self.inventory[product_id] -= quantity
                self.reserved[product_id] -= quantity
                return True
            return False

# YOU: "This design ensures:
#       - Thread safety (critical for production)
#       - Customer obsession (accurate inventory)
#       - Frugality (simple, no heavy database)
#       I would add monitoring for low stock alerts"
```

#### **Leadership Principles Questions**

**YOU MUST PREPARE FOR ALL 16 LPs!**

Most commonly tested (in Bar Raiser especially):
```
1. Customer Obsession ⭐⭐⭐⭐⭐
   "Tell me about a time you went above and beyond for a customer"

2. Ownership ⭐⭐⭐⭐⭐
   "Tell me about a time you took on something outside your scope"

3. Invent and Simplify ⭐⭐⭐⭐
   "Tell me about a time you simplified a complex process"

4. Deliver Results ⭐⭐⭐⭐⭐
   "Tell me about a time you delivered under tight deadline"

5. Have Backbone; Disagree and Commit ⭐⭐⭐⭐
   "Tell me about a time you disagreed with your manager"

6. Dive Deep ⭐⭐⭐⭐
   "Tell me about a time you had to dive into details"

7. Bias for Action ⭐⭐⭐
   "Tell me about a time you had to act quickly with incomplete data"

8. Earn Trust ⭐⭐⭐
   "Tell me about a time you made a mistake"

9. Learn and Be Curious ⭐⭐⭐
   "Tell me about a time you learned something new quickly"

10. Hire and Develop the Best ⭐⭐
    "Tell me about a time you mentored someone"
```

### Amazon Interview Tips

**DO:**
```
✅ Explicitly mention which LP your story demonstrates
✅ Have 2-3 stories per LP ready
✅ Quantify results (they love metrics!)
✅ Show ownership ("I did X" not "We did X")
✅ Demonstrate customer focus in every answer
```

**DON'T:**
```
❌ Skip mentioning LPs (they're scoring you on them!)
❌ Blame others or be negative
❌ Give vague answers without specifics
❌ Forget to show the result
❌ Be arrogant (they value "Learn and Be Curious")
```

### Amazon STAR Answer Template

```
SITUATION: [Set context with details]

TASK: "My responsibility was to... [connect to LP]"

ACTION: [Detailed steps YOU took]
"First, I... [LP: Dive Deep]
Then, I... [LP: Customer Obsession]
Finally, I... [LP: Deliver Results]"

RESULT: [Quantified outcome]
"As a result:
- [Metric 1]: X% improvement
- [Metric 2]: $Y saved
- [Metric 3]: Z customers impacted
- Leadership Principles demonstrated: [List them]"

LEARNING: [What you'd do differently - shows "Learn and Be Curious"]
```

---

## 🟣 Apple

### Interview Structure
```
Phone Screen (1-2 rounds):
└─ Domain-specific coding

Onsite (6-8 rounds):
├─ Coding (2-3 rounds): Practical problems
├─ System Design (1-2 rounds): Low-level design
├─ Domain Knowledge: Specific to role
├─ Behavioral: Culture fit
└─ Team Matching: Meet potential team
```

### What Apple Prioritizes

**1. Domain Expertise**
```
Apple hires for specific roles:
- iOS developer → Swift, iOS internals
- Systems engineer → C++, low-level
- ML engineer → ML algorithms, training

General SWE interviews are rare!
```

**2. Attention to Detail**
```
They want:
✅ Polished, production-ready code
✅ Edge case handling
✅ Memory management (especially for systems roles)
✅ Clean design
```

### Common Apple Questions

**Depends heavily on role:**

**iOS Developer:**
```
1. "Implement a custom UIScrollView"
2. "Design the camera app architecture"
3. "Handle memory warnings in an app"
4. "Implement animation system"
5. "Design offline-first sync system"
```

**Systems Engineer:**
```
1. Low-level memory management
2. File system design
3. Kernel-level programming
4. Optimization problems
5. Hardware-software interface
```

**ML Engineer:**
```
1. "Design Siri's voice recognition pipeline"
2. "Implement face detection algorithm"
3. "Optimize model for mobile device"
4. "Design A/B testing framework"
```

### Apple Interview Tips

**DO:**
```
✅ Show deep domain knowledge
✅ Focus on quality over speed
✅ Discuss memory management
✅ Consider battery/performance impact
✅ Show attention to UX details
```

**DON'T:**
```
❌ Rush through solution
❌ Ignore memory leaks
❌ Forget edge cases
❌ Dismiss design/UX considerations
```

---

## 🔴 Netflix

### Interview Structure
```
Phone Screen (2 rounds):
├─ Coding + Architecture discussion
└─ Cultural fit

Onsite (4-5 rounds):
├─ Coding/Architecture
├─ System Design
├─ Technical Leadership
├─ Culture/Values
└─ Team Fit
```

### What Netflix Prioritizes

**1. Senior-Level Thinking**
```
Netflix rarely hires junior engineers
They want:
✅ Independent problem-solvers
✅ Strategic thinking
✅ Judgment and decision-making
✅ Experience with production systems
```

**2. Culture of Freedom & Responsibility**
```
Can you handle:
✅ Minimal oversight
✅ Ambiguous problems
✅ High responsibility
✅ Direct feedback
```

### Netflix Interview Tips

**DO:**
```
✅ Show senior-level thinking
✅ Discuss production experiences
✅ Demonstrate independent problem-solving
✅ Show comfort with feedback
✅ Discuss context, not control
```

**DON'T:**
```
❌ Need hand-holding
❌ Avoid responsibility
❌ Struggle with ambiguity
❌ Take feedback personally
```

---

## 🟢 Microsoft

### Interview Structure
```
Phone Screen (1 round):
└─ Coding + behavioral

Onsite (4-5 rounds):
├─ Coding Round 1
├─ Coding Round 2
├─ System Design (L5+)
├─ Behavioral/Growth Mindset
└─ As Appropriate (AA) Round (only if passing)
```

### What Microsoft Prioritizes

**1. Growth Mindset**
```
They love:
✅ Learning from mistakes
✅ Continuous improvement
✅ Openness to feedback
✅ Collaboration and knowledge sharing
```

**2. Technical Fundamentals**
```
Similar to other companies but:
- Not as hard as Google
- More collaborative culture
- Focus on getting things done
```

### Common Microsoft Questions

**Similar to Google/Meta but slightly easier:**
```
1. Reverse Linked List
2. Validate Binary Search Tree
3. Merge Two Sorted Lists
4. Word Search
5. Design Excel (OOP design)
```

### Microsoft Interview Tips

**DO:**
```
✅ Show growth mindset
✅ Discuss learning experiences
✅ Demonstrate collaboration
✅ Show humility
✅ Mention helping others
```

**DON'T:**
```
❌ Know-it-all attitude
❌ Resist feedback
❌ Work in silos
❌ Blame others
```

---

## 📊 Difficulty Ranking

```
Hardest to Get Offer:
1. Netflix (highest bar, senior only)
2. Google (algorithmic difficulty)
3. Apple (domain expertise required)
4. Meta (competitive, high volume)
5. Amazon (behavioral heavy)
6. Microsoft (most approachable)

Interview Difficulty (DSA):
1. Google ⭐⭐⭐⭐⭐
2. Meta ⭐⭐⭐⭐
3. Apple ⭐⭐⭐⭐ (domain-specific)
4. Netflix ⭐⭐⭐⭐ (senior-level)
5. Amazon ⭐⭐⭐
6. Microsoft ⭐⭐⭐

Behavioral Difficulty:
1. Amazon (LP heavy) ⭐⭐⭐⭐⭐
2. Netflix (culture fit) ⭐⭐⭐⭐
3. Apple (detail-oriented) ⭐⭐⭐⭐
4. Google (Googleyness) ⭐⭐⭐
5. Meta (impact-focused) ⭐⭐⭐
6. Microsoft (growth mindset) ⭐⭐⭐
```

---

## 🎯 Strategy by Company

**Google:**
```
Months 1-3: Master algorithms and complexity
Month 4: Practice system design
Month 5-6: Mock interviews + Googleyness prep
```

**Meta:**
```
Months 1-3: Focus on graphs, trees, medium problems
Month 4: System design (social features)
Month 5-6: Practice talking about impact
```

**Amazon:**
```
Months 1-2: Basic DSA (not super hard)
Month 3-4: Write 2-3 stories PER LP
Month 5-6: Practice LP answers, bar raiser prep
```

**Apple:**
```
Depends on role:
- iOS: Master Swift, iOS frameworks
- Systems: Low-level programming
- ML: ML algorithms, mobile optimization
```

**Netflix:**
```
Need 5+ years experience minimum
Focus on:
- Production experience
- System architecture
- Leadership stories
```

**Microsoft:**
```
Months 1-3: Solid DSA fundamentals
Month 4: System design basics
Month 5-6: Growth mindset examples
```

---

**Next Steps:**
1. Identify your target company
2. Focus on their specific patterns
3. Practice their common questions
4. Tailor your behavioral stories
5. Do company-specific mocks

**Remember: Each company has its own culture and priorities. Tailor your preparation accordingly!**
