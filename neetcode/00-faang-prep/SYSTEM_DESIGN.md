# 🏗️ System Design for FAANG Interviews

**Master System Design: The Missing 30% for Senior Roles**

> System Design is what separates junior from senior engineers in FAANG interviews. This guide makes it easy to digest with visuals and real-world examples.

---

## 📚 Best Resources (Research-Backed 2025)

### Must-Have Resources:
1. **Grokking the System Design Interview** (DesignGurus.io)
   - 140,000+ learners
   - Best for FAANG prep
   - Clear, repeatable framework

2. **System Design Primer** (GitHub - free!)
   - 230k+ stars
   - Created by ex-Facebook engineer
   - Comprehensive collection

3. **Alex Xu's Books** (Volume 1 & 2)
   - 23 design problems
   - In-depth visual explanations
   - Great for deep understanding

4. **ByteByteGo** (Newsletter & Videos)
   - Weekly system design content
   - Visual-first approach
   - Real-world systems

### When You Need System Design:
```
Entry Level (L3):         Usually NOT tested ❌
Mid Level (L4):           LOW LEVEL Design ✅
Senior (L5+):             HIGH LEVEL Design ✅✅✅
Staff/Principal (L6+):    CRITICAL ✅✅✅✅
```

---

## 🎯 Quick Start: Your First Hour

### 1. Understand What System Design IS (10 minutes)

**System Design Interview =**
"Design Twitter/Instagram/Uber in 45 minutes"

**What they're REALLY testing:**
```
❌ NOT: Can you memorize architectures?
✅ YES: Can you think through trade-offs?
✅ YES: Do you understand scalability?
✅ YES: Can you communicate clearly?
✅ YES: Do you make pragmatic decisions?
```

### 2. The Interview Structure (5 minutes)

```
Step 1: CLARIFY (5 min)        → Ask questions
Step 2: SCOPE (3 min)           → Define what to build
Step 3: HIGH-LEVEL (15 min)     → Draw boxes
Step 4: DEEP DIVE (15 min)      → Pick components to detail
Step 5: DISCUSS (7 min)         → Trade-offs, bottlenecks
```

### 3. Core Concepts Overview (45 minutes)

Read sections 4-7 below to understand:
- Scalability basics
- Database choices
- Caching strategies
- Load balancing

---

## 📖 Complete System Design Roadmap

### Week 1-2: Foundation Concepts (10-15 hours)
- [ ] Scalability basics (vertical vs horizontal)
- [ ] Load balancing
- [ ] Caching
- [ ] Database basics (SQL vs NoSQL)
- [ ] API design (REST)

### Week 3-4: Advanced Concepts (15-20 hours)
- [ ] Database sharding
- [ ] Replication (master-slave, multi-master)
- [ ] CAP theorem
- [ ] Consistent hashing
- [ ] Message queues

### Week 5-6: Design Practice (20 hours)
- [ ] URL shortener (easiest)
- [ ] Pastebin
- [ ] Instagram/Twitter feed
- [ ] Design YouTube/Netflix
- [ ] Design Uber/Lyft

### Week 7-8: Mock Interviews (10 hours)
- [ ] Practice with peers
- [ ] Pramp (free)
- [ ] Interviewing.io
- [ ] Get feedback

**Total Time: 55-65 hours over 8 weeks**

---

## 🎓 Core Concepts Explained Visually

### 1. Scalability 101

#### Vertical Scaling (Scale UP)
```
Before:              After:
┌─────────┐         ┌─────────┐
│ Server  │    →    │ BIGGER  │
│ 4 GB    │         │ Server  │
│ 2 Cores │         │ 64 GB   │
└─────────┘         │ 32 Cores│
                     └─────────┘

Pros: ✅ Simple, no code changes
Cons: ❌ Limited (can't add infinite CPU)
      ❌ Expensive
      ❌ Single point of failure
```

#### Horizontal Scaling (Scale OUT)
```
Before:              After:
┌─────────┐         ┌─────────┐  ┌─────────┐  ┌─────────┐
│ Server  │    →    │ Server  │  │ Server  │  │ Server  │
│         │         │    1    │  │    2    │  │    3    │
└─────────┘         └─────────┘  └─────────┘  └─────────┘
                            ↑           ↑           ↑
                            └───────┬───────────────┘
                                Load Balancer

Pros: ✅ Infinite scaling (add more servers)
      ✅ Fault tolerant (one fails, others work)
Cons: ❌ More complex
      ❌ Data consistency challenges
```

**When to use:**
- Vertical: Starting out, simple apps, quick fix
- Horizontal: Production, high traffic, FAANG scale

---

### 2. Load Balancing

#### What is it?
Distributes incoming requests across multiple servers

```
                    LOAD BALANCER
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ↓                ↓                ↓
   ┌─────────┐      ┌─────────┐     ┌─────────┐
   │ Server 1│      │ Server 2│     │ Server 3│
   │ Load:20%│      │ Load:30%│     │ Load:50%│
   └─────────┘      └─────────┘     └─────────┘
```

#### Load Balancing Algorithms

**1. Round Robin** (simplest)
```
Request 1 → Server 1
Request 2 → Server 2
Request 3 → Server 3
Request 4 → Server 1  (cycles back)

Use when: Servers are identical, requests take similar time
```

**2. Least Connections**
```
Server 1: 10 active connections
Server 2: 5 active connections   ← Send here!
Server 3: 15 active connections

Use when: Requests vary in processing time
```

**3. Weighted Round Robin**
```
Server 1 (powerful):    Weight 5 → Gets 50% traffic
Server 2 (medium):      Weight 3 → Gets 30% traffic
Server 3 (small):       Weight 2 → Gets 20% traffic

Use when: Servers have different capacities
```

**4. IP Hash / Sticky Sessions**
```
User A (IP: 1.2.3.4) → Always Server 1
User B (IP: 5.6.7.8) → Always Server 2

Use when: Need session persistence (shopping cart, login)
```

---

### 3. Caching (CRITICAL for Performance)

#### Cache Hierarchy
```
Speed (Fastest → Slowest):

Browser Cache      [1 ms]       ← User's browser
    ↓
CDN Cache          [10 ms]      ← CloudFlare, Akamai
    ↓
Application Cache  [50 ms]      ← Redis, Memcached
    ↓
Database Query     [500 ms]     ← PostgreSQL, MySQL
    ↓
Disk Read          [5000 ms]    ← Slowest
```

#### Cache Strategies

**1. Cache-Aside (Lazy Loading)**
```
1. App checks cache
2. Cache MISS → Read from DB
3. Store in cache
4. Return to user

┌──────┐    ❌ Cache Miss?     ┌───────┐
│ App  │───────────────────→   │ Cache │
│      │    1. Check           └───────┘
│      │
│      │    ✅ DB Read         ┌───────┐
│      │←──────────────────    │  DB   │
│      │    2. Get data        └───────┘
│      │
│      │    3. Store           ┌───────┐
│      │───────────────────→   │ Cache │
└──────┘                       └───────┘

Pros: ✅ Only cache what's needed
Cons: ❌ Cache miss penalty
Best for: Read-heavy, data rarely changes
```

**2. Write-Through**
```
Every write → Update DB AND cache together

┌──────┐                       ┌───────┐
│ App  │    Write data         │ Cache │
│      │──────────────────→    └───────┘
│      │         │
│      │         └─────────→    ┌───────┐
│      │              Write     │  DB   │
└──────┘              Also      └───────┘

Pros: ✅ Cache always fresh
Cons: ❌ Every write is slower
Best for: Data must be consistent
```

**3. Write-Back (Write-Behind)**
```
Write to cache first, DB later (asynchronously)

┌──────┐    Fast write!        ┌───────┐
│ App  │──────────────────→    │ Cache │
│      │                       └───────┘
└──────┘                            │
                                    │ (later)
                                    ↓
                               ┌───────┐
                               │  DB   │
                               └───────┘

Pros: ✅ Super fast writes
Cons: ❌ Risk of data loss (cache dies before DB write)
Best for: High write throughput, can tolerate some loss
```

#### Cache Eviction Policies

**When cache is full, what do you remove?**

```
LRU (Least Recently Used):  ← Most common!
Remove item not accessed for longest time

Example:
Cache: [A, B, C, D]  (max size: 4)
Access: E
Remove: A (oldest access)
Cache: [B, C, D, E]

Use: General purpose, default choice

───────────────────────────────────────

LFU (Least Frequently Used):
Remove item accessed least often

Example:
A: 100 hits
B: 5 hits    ← Remove this!
C: 50 hits
D: 200 hits

Use: When some data is consistently popular

───────────────────────────────────────

FIFO (First In First Out):
Remove oldest entry

Example:
Cache: [A, B, C, D]  (added in this order)
Remove: A (first added)

Use: Simple, when all items equally important

───────────────────────────────────────

TTL (Time To Live):
Remove after X seconds

Example:
A: Added 100s ago (TTL: 60s)  ← Expired, remove!
B: Added 30s ago

Use: Time-sensitive data (stock prices, scores)
```

**Interview Answer Template:**
"I'd use Redis with LRU eviction. For this use case [explain why]."

---

### 4. Database Design

#### SQL vs NoSQL: The Decision Tree

```
START: What kind of data?

Structured with relationships?
│
├─ YES → Need ACID transactions?
│        │
│        ├─ YES → SQL (PostgreSQL, MySQL)
│        │        Use: Banking, Orders, User accounts
│        │
│        └─ NO → Could use either
│
└─ NO → Unstructured/Flexible schema?
         │
         ├─ YES → NoSQL
         │        │
         │        ├─ Document? → MongoDB
         │        │              (JSON-like, flexible)
         │        │
         │        ├─ Key-Value? → Redis, DynamoDB
         │        │              (Super fast, simple)
         │        │
         │        ├─ Wide Column? → Cassandra, HBase
         │        │                 (Time series, logs)
         │        │
         │        └─ Graph? → Neo4j
         │                    (Social networks, recommendations)
         │
         └─ NO → Re-evaluate your data model
```

#### SQL Example (Relational)
```sql
-- Users table
┌────────┬──────────┬───────────────────┐
│ user_id│   name   │      email        │
├────────┼──────────┼───────────────────┤
│   1    │  Alice   │ alice@email.com   │
│   2    │  Bob     │ bob@email.com     │
└────────┴──────────┴───────────────────┘
         │
         └─────────┐ (Foreign Key)
                   │
-- Posts table     ↓
┌────────┬────────┬─────────────────────┐
│ post_id│ user_id│     content         │
├────────┼────────┼─────────────────────┤
│  101   │   1    │ Alice's post        │
│  102   │   1    │ Another post        │
│  103   │   2    │ Bob's post          │
└────────┴────────┴─────────────────────┘

Pros: ✅ Relationships built-in (JOINs)
      ✅ ACID guarantees
      ✅ Mature, well-understood
Cons: ❌ Harder to scale horizontally
      ❌ Fixed schema
```

#### NoSQL Example (Document - MongoDB)
```javascript
// Each user document contains their posts
{
  "_id": 1,
  "name": "Alice",
  "email": "alice@email.com",
  "posts": [
    {"id": 101, "content": "Alice's post"},
    {"id": 102, "content": "Another post"}
  ]
}

Pros: ✅ Scales horizontally easily
      ✅ Flexible schema (add fields anytime)
      ✅ Fast for document retrieval
Cons: ❌ No built-in relationships
      ❌ Eventual consistency (trade-off)
```

#### When to use what in interviews:

```
"Design Twitter/Instagram/Facebook Feed"
→ SQL (Users, Follows, Posts are relational)
→ PLUS NoSQL for caching (Redis)

"Design Netflix/YouTube video metadata"
→ SQL (User accounts, subscriptions)
→ NoSQL (Video metadata, recommendations)

"Design Uber real-time tracking"
→ NoSQL (Cassandra for location data - time series)
→ SQL (User profiles, trip history)

"Design Analytics/Logs system"
→ NoSQL (Wide column store like Cassandra)

"Design Social Network connections"
→ Graph DB (Neo4j) for friend suggestions
→ SQL for user data
```

---

### 5. Database Sharding

#### What is Sharding?
Split one large database across multiple machines

**Before (Single DB):**
```
        Database (100 TB)  ← Too big! Slow!
┌──────────────────────────────────────┐
│ User 1, User 2, User 3, ... User 1M  │
└──────────────────────────────────────┘
```

**After (Sharded):**
```
Shard 1 (25 TB)     Shard 2 (25 TB)     Shard 3 (25 TB)     Shard 4 (25 TB)
┌────────────┐      ┌────────────┐      ┌────────────┐      ┌────────────┐
│ User 1-250k│      │ User 250k- │      │ User 500k- │      │ User 750k- │
│            │      │    500k    │      │    750k    │      │     1M     │
└────────────┘      └────────────┘      └────────────┘      └────────────┘
```

#### Sharding Strategies

**1. Hash-Based Sharding**
```python
# Shard number = hash(user_id) % number_of_shards

user_id = 12345
shard = hash(12345) % 4  # Result: 2
→ Store in Shard 2

Pros: ✅ Even distribution
      ✅ Simple
Cons: ❌ Hard to add/remove shards (re-hash everything!)
      ❌ Range queries difficult
```

**2. Range-Based Sharding**
```
User IDs 1-250,000      → Shard 1
User IDs 250,001-500,000 → Shard 2
User IDs 500,001-750,000 → Shard 3
User IDs 750,001-1M      → Shard 4

Pros: ✅ Range queries easy
      ✅ Easy to add shards
Cons: ❌ Uneven distribution (some ranges more popular)
```

**3. Geography-Based Sharding**
```
US users       → Shard in US
Europe users   → Shard in EU
Asia users     → Shard in Asia

Pros: ✅ Low latency (data close to users)
      ✅ Regulatory compliance
Cons: ❌ Uneven load
      ❌ Cross-region queries expensive
```

**4. Directory-Based Sharding**
```
Lookup table:
user_id → shard_id

User 1    → Shard 2
User 2    → Shard 1
User 3    → Shard 3
...

Pros: ✅ Flexible (any sharding logic)
      ✅ Easy to rebalance
Cons: ❌ Lookup overhead
      ❌ Lookup table is single point of failure
```

#### Sharding Challenges

```
Problem 1: Cross-Shard Queries
User A (Shard 1) wants to see posts from User B (Shard 3)
→ Need to query multiple shards!
Solution: Denormalize data, cache, or accept slower queries

Problem 2: Rebalancing
Shard 1: 80% full
Shard 2: 20% full
→ Need to move data around (expensive!)
Solution: Consistent hashing

Problem 3: Joins
Can't JOIN across shards easily
Solution: Denormalize, or do joins in application code
```

---

### 6. Replication

#### Master-Slave Replication
```
                    MASTER (Writes)
                         │
                    Write here
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ↓                ↓                ↓
   SLAVE 1          SLAVE 2          SLAVE 3
   (Read)           (Read)           (Read)

How it works:
1. All writes go to Master
2. Master replicates data to Slaves
3. Reads distributed across Slaves
4. If Master dies → Promote a Slave

Pros: ✅ Scales reads (add more slaves)
      ✅ Simple to implement
Cons: ❌ Writes don't scale (still one master)
      ❌ Replication lag (slaves may be slightly behind)

Use case: Read-heavy apps (e.g., news sites, blogs)
```

#### Master-Master Replication
```
    MASTER 1  ←──────────→  MASTER 2
    (R/W)      Sync data      (R/W)
      │                         │
      ↓                         ↓
   Slaves                    Slaves

Both masters accept writes!

Pros: ✅ No single point of failure
      ✅ Better write throughput
      ✅ Geographic distribution
Cons: ❌ Complex conflict resolution
      ❌ More difficult to maintain

Use case: Global apps, high availability
```

#### Replication Lag Problem
```
Time    Master          Slave
0:00    Write: X=5      X=1
0:01    X=5             X=1 (lag!)
0:02    X=5             X=5 (caught up)

User writes to Master, immediately reads from Slave
→ Gets stale data!

Solutions:
1. Read from Master after write (slower)
2. Session affinity (same user always same server)
3. Version numbers (check if data is fresh enough)
```

---

### 7. CAP Theorem (Critical for Distributed Systems)

```
         CAP THEOREM
        You can pick 2 of 3:

    C           A           P
Consistency  Availability  Partition
                           Tolerance

┌──────────────────────────────────┐
│                                  │
│    CONSISTENCY (C)               │
│    All nodes see same data       │
│    at same time                  │
│                                  │
└──────────────────────────────────┘

┌──────────────────────────────────┐
│                                  │
│    AVAILABILITY (A)              │
│    Every request gets response   │
│    (even if data is stale)       │
│                                  │
└──────────────────────────────────┘

┌──────────────────────────────────┐
│                                  │
│    PARTITION TOLERANCE (P)       │
│    System works even if network  │
│    splits (some nodes can't talk)│
│                                  │
└──────────────────────────────────┘
```

**In reality: Network partitions WILL happen**
**So you MUST have P (Partition Tolerance)**

**Real choice: CP or AP?**

#### CP (Consistency + Partition Tolerance)
```
Example: Banking systems

Scenario:
Network split! Nodes can't communicate
→ System refuses requests (unavailable)
→ Better than showing wrong balance

Databases: PostgreSQL, MongoDB (strong consistency mode)

Use when: Money, inventory, bookings
```

#### AP (Availability + Partition Tolerance)
```
Example: Social media feeds

Scenario:
Network split! Nodes can't communicate
→ System still responds (may show stale data)
→ Better than being down

Databases: Cassandra, DynamoDB, Riak

Use when: Feeds, likes, views, recommendations
```

#### Interview Answer Template:
```
"For this system, I'd prioritize [C/A] over [A/C] because:
- [Explain business impact]
- [Give example of what happens if you choose wrong]
- We can mitigate the trade-off by [solution]"

Example:
"For a payment system, I'd prioritize Consistency (CP).
It's better to show an error than to allow double-charging.
Users expect financial systems to be unavailable occasionally
but never incorrect. We can mitigate unavailability with
good retry mechanisms and clear error messages."
```

---

### 8. Message Queues (Asynchronous Processing)

#### Problem Without Queues:
```
User uploads video to YouTube
    ↓
Server must:
    - Transcode video (10 minutes!)
    - Generate thumbnails
    - Update database
    - Send notifications
    ↓
User waits 10 minutes! ❌
```

#### Solution With Message Queue:
```
User uploads video
    ↓
Server: "Got it! Processing..."  (instant response)
    ↓
Put task in QUEUE
    ↓
Background workers process when ready
    ↓
User gets notification when done ✅
```

#### Visual Architecture:
```
┌──────┐    1. Request     ┌─────────┐
│ User │──────────────────→│   API   │
└──────┘                   └─────────┘
                                 │
                         2. Publish job
                                 ↓
                    ┌────────────────────┐
                    │   MESSAGE QUEUE    │
                    │    (RabbitMQ,      │
                    │     Kafka, SQS)    │
                    └────────────────────┘
                         ↓       ↓       ↓
                    3. Workers pull jobs
                         ↓       ↓       ↓
                    ┌────────────────────┐
                    │  Worker 1  Worker 2│
                    │  Worker 3  Worker 4│
                    └────────────────────┘
                              ↓
                    4. Process & Update DB
                              ↓
                         ┌─────────┐
                         │   DB    │
                         └─────────┘
```

#### Popular Message Queues:

**RabbitMQ**
```
Pros: ✅ Easy to use
      ✅ Good for small/medium scale
      ✅ Reliable delivery
Use: Task queues, email sending, notifications
```

**Apache Kafka**
```
Pros: ✅ Massive throughput (millions msg/sec)
      ✅ Stores messages (replay capability)
      ✅ Stream processing
Use: Real-time analytics, logs, event sourcing
```

**AWS SQS**
```
Pros: ✅ Fully managed
      ✅ Auto-scales
      ✅ Pay per use
Use: AWS-based systems, simple queuing
```

#### Queue Patterns:

**1. Fanout (Pub/Sub)**
```
        Publisher
            │
            ↓
         Queue
    ┌───────┼───────┐
    ↓       ↓       ↓
 Sub 1   Sub 2   Sub 3

All subscribers get the message
Use: Notifications, broadcasts
```

**2. Work Queue**
```
Producer → Queue → [Worker1, Worker2, Worker3]
                    (only one worker gets each job)

Load balanced processing
Use: Video processing, image resizing
```

**3. Priority Queue**
```
High priority jobs    → Process first
Medium priority jobs  → Process next
Low priority jobs     → Process last

Use: Paid users get priority, critical alerts
```

---

### 9. CDN (Content Delivery Network)

#### Problem:
```
User in India requests image from US server
    ↓
Round-trip time: 300ms ❌ (Slow!)
```

#### Solution with CDN:
```
User in India → CDN server in India (cached)
    ↓
Round-trip time: 20ms ✅ (Fast!)
```

#### How CDN Works:
```
              ┌──────────────┐
              │  ORIGIN      │
              │  SERVER (US) │
              └──────────────┘
                      │
        First request │ (cache miss)
                      ↓
    ┌─────────────────────────────────┐
    │       CDN Edge Servers          │
    │  (Cached copies worldwide)      │
    └─────────────────────────────────┘
        │         │         │
      India      EU       Asia
        │         │         │
    ┌─────┐   ┌─────┐   ┌─────┐
    │User │   │User │   │User │
    └─────┘   └─────┘   └─────┘

Subsequent requests → Served from nearest CDN edge
```

#### What to Cache in CDN:
```
✅ Static files: images, CSS, JavaScript
✅ Videos
✅ HTML pages (if they rarely change)
✅ API responses (with short TTL)

❌ User-specific data
❌ Frequently changing data
❌ Sensitive data
```

#### Popular CDNs:
- CloudFlare
- AWS CloudFront
- Akamai
- Fastly

---

### 10. API Design

#### REST API Best Practices

**URL Structure:**
```
Good:
GET    /users              (list all users)
GET    /users/123          (get user 123)
POST   /users              (create user)
PUT    /users/123          (update user 123)
DELETE /users/123          (delete user 123)
GET    /users/123/posts    (get posts by user 123)

Bad:
GET    /getUsers           ❌
POST   /createUser         ❌
GET    /user?id=123        ❌ (use path param)
```

**HTTP Status Codes:**
```
200 OK              → Success
201 Created         → Resource created
204 No Content      → Success, nothing to return
400 Bad Request     → Client error (invalid input)
401 Unauthorized    → Not authenticated
403 Forbidden       → Authenticated but no permission
404 Not Found       → Resource doesn't exist
500 Internal Error  → Server error
503 Service Unavailable → Server overloaded
```

**Pagination:**
```
GET /users?page=2&limit=20

Response:
{
  "data": [...],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 1000,
    "total_pages": 50
  }
}
```

**Rate Limiting:**
```
Response Headers:
X-RateLimit-Limit: 1000      (max requests per hour)
X-RateLimit-Remaining: 999   (requests left)
X-RateLimit-Reset: 1640000000 (when limit resets)

When exceeded:
429 Too Many Requests
```

---

## 🎯 Common System Design Questions

### Easy: URL Shortener (bit.ly, tinyurl)

**Requirements:**
- Shorten long URLs
- Redirect to original URL
- Track click stats

**High-Level Design:**
```
User enters long URL
    ↓
API generates short code (e.g., "abc123")
    ↓
Store: {short_code: "abc123", long_url: "..."}
    ↓
User visits short URL
    ↓
Lookup long URL
    ↓
Redirect (302)
```

**Database:**
```
Table: urls
┌────────────┬─────────────────────────┬───────┐
│ short_code │      long_url           │ clicks│
├────────────┼─────────────────────────┼───────┤
│  abc123    │ https://very-long-url   │  150  │
└────────────┴─────────────────────────┴───────┘

SQL or NoSQL? Either works
- SQL (PostgreSQL): Good for analytics
- NoSQL (DynamoDB): Better for scale
```

**Short Code Generation:**
```python
Option 1: Hash (MD5/SHA) + Take first 7 chars
- Fast
- Need to check collisions

Option 2: Base62 encoding (a-z, A-Z, 0-9)
- auto_increment_id → base62 → "abc123"
- No collisions
- Can predict total URLs (security issue)

Option 3: Random + Check uniqueness
- Generate random string
- Check if exists, retry if collision
```

**Scale:**
```
7 characters, base62 (62 options per char)
62^7 = 3.5 trillion possible URLs ✅

Traffic: 1 million writes/day
        10 million reads/day (10:1 read/write ratio)

Solution:
- Cache popular URLs (Redis)
- Read replicas for database
- CDN for API responses
```

---

### Medium: Design Instagram/Twitter Feed

**Requirements:**
- Post photos/tweets
- Follow users
- See feed (posts from people you follow)
- Like, comment

**High-Level Design:**
```
┌──────────┐
│  Client  │
└─────┬────┘
      │
┌─────▼─────────────┐
│   API Gateway     │
└─────┬─────────────┘
      │
      ├──→ Post Service
      ├──→ Feed Service
      ├──→ Follow Service
      └──→ Like Service
           │
      ┌────▼────────┐
      │  Database   │
      └─────────────┘
```

**Database Schema (SQL):**
```sql
users:
┌─────────┬──────────┬───────┐
│ user_id │   name   │ email │
└─────────┴──────────┴───────┘

posts:
┌─────────┬─────────┬─────────┬────────────┐
│ post_id │ user_id │ content │  timestamp │
└─────────┴─────────┴─────────┴────────────┘

follows:
┌───────────────┬─────────────────┐
│ follower_id   │  following_id   │
└───────────────┴─────────────────┘

likes:
┌─────────┬─────────┐
│ post_id │ user_id │
└─────────┴─────────┘
```

**Feed Generation: Two Approaches**

**1. Pull (Fanout on Read):**
```
User requests feed
    ↓
Find all users they follow
    ↓
Get recent posts from those users
    ↓
Sort by timestamp
    ↓
Return top 50

Pros: ✅ Simple
      ✅ Consistent (always fresh)
Cons: ❌ Slow (query on every request)

Use when: Small scale, few followers
```

**2. Push (Fanout on Write):**
```
User posts content
    ↓
Find all followers (e.g., 1000 people)
    ↓
Write post to each follower's feed cache
    ↓
User requests feed
    ↓
Return pre-computed feed from cache (instant!)

Pros: ✅ Fast reads
Cons: ❌ Slow writes (if many followers)
      ❌ Lots of storage

Use when: Most users have < 10k followers
```

**3. Hybrid Approach (FAANG Answer):**
```
Normal users (< 10k followers):
    → Fanout on write (push)

Celebrities (> 10k followers):
    → Fanout on read (pull)

User requests feed:
    ↓
Get pre-computed feed (normal users)
    +
Fetch latest from celebrities they follow
    ↓
Merge and sort
```

**Caching Strategy:**
```
Redis Cache:
- User feed (last 1000 posts)
- Popular posts (trending)
- User profile data

TTL: 5 minutes for feeds
```

**Scale Numbers:**
```
100 million daily active users
500 million posts per day
Average: 500 followers per user

Storage:
- Posts: 500M × 1KB = 500 GB/day
- Feed cache: 100M users × 50 posts × 1KB = 5 TB

Solutions:
- S3 for images/videos
- CDN for media delivery
- Database sharding by user_id
- Read replicas (10 reads : 1 write)
```

---

### Hard: Design YouTube/Netflix

**Requirements:**
- Upload videos
- Stream videos
- Recommendations
- Search

**High-Level Architecture:**
```
┌─────────────────────────────────────────────────────┐
│                     CDN                             │
│              (Serve videos globally)                │
└──────────────────┬──────────────────────────────────┘
                   │
┌──────────────────┴──────────────────────────────────┐
│                  API Gateway                        │
└─────┬────────────┬────────────┬───────────┬─────────┘
      │            │            │           │
┌─────▼──────┐ ┌──▼──────┐ ┌───▼─────┐ ┌──▼──────────┐
│   Upload   │ │ Stream  │ │ Search  │ │Recommendation│
│  Service   │ │ Service │ │ Service │ │   Service    │
└─────┬──────┘ └──┬──────┘ └───┬─────┘ └──┬──────────┘
      │           │            │           │
┌─────▼───────────▼────────────▼───────────▼──────────┐
│              Distributed Storage                     │
│          (S3, HDFS for videos)                       │
└──────────────────────────────────────────────────────┘
```

**Upload Flow:**
```
User uploads video (2GB)
    ↓
1. Upload to S3 (original quality)
    ↓
2. Trigger transcoding job (message queue)
    ↓
3. Transcode to multiple formats:
   - 4K (high quality)
   - 1080p
   - 720p
   - 480p
   - 360p (mobile)
    ↓
4. Generate thumbnails
    ↓
5. Extract metadata (duration, size, etc.)
    ↓
6. Update database (video available)
    ↓
7. Push to CDN edge servers
```

**Streaming:**
```
Adaptive Bitrate Streaming (HLS/DASH):
- Divide video into small chunks (10 seconds each)
- Client starts with low quality
- Measure bandwidth
- Upgrade to higher quality if bandwidth allows
- Downgrade if buffering

Example:
User with slow connection → 480p
User with fast connection → 1080p
Connection gets worse → Auto-switch to 720p
```

**Storage Calculation:**
```
500 hours of video uploaded per minute
Average: 5 minutes per video
Size: 1 GB per video (original)
After transcoding (5 qualities): 5 GB total

Daily: 500 videos/min × 60 min × 24 hours
     = 720,000 videos/day
     = 3.6 PB per day! 😱

Solutions:
- Compress aggressively
- Delete unpopular videos after X months
- Use cold storage (S3 Glacier) for old videos
```

**Database Design:**
```sql
videos:
┌──────────┬─────────┬────────┬──────────┬───────┐
│ video_id │ user_id │ title  │ duration │ views │
└──────────┴─────────┴────────┴──────────┴───────┘

video_files:
┌──────────┬────────────┬───────────────────┐
│ video_id │ resolution │   file_url        │
├──────────┼────────────┼───────────────────┤
│   123    │   1080p    │ s3://bucket/...   │
│   123    │    720p    │ s3://bucket/...   │
└──────────┴────────────┴───────────────────┘

Use: SQL for metadata, S3 for actual videos
```

**Recommendations:**
```
Two approaches:

1. Collaborative Filtering:
   Users who watched video A also watched B

2. Content-Based:
   Video tags, categories, description similarity

Hybrid approach (Netflix does this):
   Combine both + add machine learning

Implementation:
   - Pre-compute recommendations (batch job nightly)
   - Store in cache (Redis)
   - Update as user watches
```

**Key Optimizations:**
```
✅ CDN for video delivery (99% of traffic)
✅ Cache popular videos at edge
✅ Adaptive bitrate streaming
✅ Pre-load next video (predict what user will watch)
✅ Thumbnail sprites (one image, multiple frames)
✅ Lazy loading (don't load entire feed at once)
```

---

## 🎯 Interview Framework (Use This Every Time)

### Step 1: Clarify Requirements (5 minutes)

**Functional:**
```
- What features exactly?
- Who are the users?
- How many users?
- What actions can they perform?
```

**Non-Functional:**
```
- Scale? (users, requests per second)
- Latency requirements?
- Consistency vs Availability?
- Read-heavy or write-heavy?
```

### Step 2: Back-of-Envelope Estimates (3 minutes)

```
Traffic:
- 100M daily active users
- Each user makes 10 requests/day
- Total: 1B requests/day
- Requests/second: 1B / 86400 ≈ 12,000 RPS

Storage:
- Each post: 1 KB
- 10M posts/day
- Total: 10 GB/day = 3.6 TB/year

Bandwidth:
- 12,000 RPS × 1 KB = 12 MB/s
```

### Step 3: High-Level Design (15 minutes)

**Draw boxes:**
```
Client → Load Balancer → API Servers → Database
                                    ↓
                                 Cache
```

**Explain:**
- What each component does
- How they communicate
- What technology choices

### Step 4: Deep Dive (15 minutes)

**Pick 2-3 components to detail:**
```
"Let me dive deeper into the feed generation algorithm..."
[Draw detailed diagram]
[Explain trade-offs]
```

### Step 5: Discuss Trade-offs (7 minutes)

```
- Bottlenecks?
- Single points of failure?
- How to scale each component?
- Monitoring and alerting?
```

---

## 📚 Study Plan: 8 Weeks to System Design Mastery

### Week 1: Foundation
- [ ] Read: System Design Primer (Scalability section)
- [ ] Watch: 5 system design intro videos
- [ ] Practice: Explain concepts to someone
- **Time: 10 hours**

### Week 2: Core Components
- [ ] Load balancing (2 hours)
- [ ] Caching (3 hours)
- [ ] Databases (SQL vs NoSQL) (3 hours)
- [ ] CDN (2 hours)
- **Time: 10 hours**

### Week 3: Advanced Concepts
- [ ] Sharding (3 hours)
- [ ] Replication (2 hours)
- [ ] CAP theorem (2 hours)
- [ ] Message queues (3 hours)
- **Time: 10 hours**

### Week 4: Practice Easy Problems
- [ ] URL Shortener (3 hours)
- [ ] Pastebin (3 hours)
- [ ] Instagram timeline (4 hours)
- **Time: 10 hours**

### Week 5: Practice Medium Problems
- [ ] Twitter feed (4 hours)
- [ ] Web crawler (3 hours)
- [ ] Notification system (3 hours)
- **Time: 10 hours**

### Week 6: Practice Hard Problems
- [ ] YouTube/Netflix (5 hours)
- [ ] Uber/Lyft (5 hours)
- **Time: 10 hours**

### Week 7: Mock Interviews
- [ ] Practice with peers (3 sessions × 2 hours)
- [ ] Pramp (3 sessions × 1.5 hours)
- **Time: 10 hours**

### Week 8: Review & Polish
- [ ] Review all designs
- [ ] Focus on weak areas
- [ ] Final mock interview
- **Time: 10 hours**

**Total: 80 hours over 8 weeks = 10 hours/week**

---

## ✅ Interview Checklist

Before the interview, can you explain:
- [ ] Horizontal vs vertical scaling
- [ ] Load balancing algorithms
- [ ] Caching strategies (cache-aside, write-through)
- [ ] SQL vs NoSQL (when to use each)
- [ ] Database sharding strategies
- [ ] CAP theorem (CP vs AP)
- [ ] Replication (master-slave, master-master)
- [ ] Message queues (when and why)
- [ ] CDN (how it works)
- [ ] Rate limiting

Can you design:
- [ ] URL shortener (easy)
- [ ] Twitter feed (medium)
- [ ] YouTube (hard)

Do you know:
- [ ] How to calculate storage requirements
- [ ] How to calculate bandwidth requirements
- [ ] How to estimate QPS (queries per second)

---

## 🎯 Quick Reference: Technology Choices

```
Load Balancer:
- Small: nginx, HAProxy
- Large: AWS ELB, Google Cloud Load Balancer

Cache:
- In-memory: Redis, Memcached
- CDN: CloudFlare, AWS CloudFront

Database:
- SQL: PostgreSQL (general), MySQL (read-heavy)
- NoSQL Document: MongoDB
- NoSQL Key-Value: Redis, DynamoDB
- NoSQL Wide Column: Cassandra, HBase
- NoSQL Graph: Neo4j

Message Queue:
- Simple: RabbitMQ, AWS SQS
- High-throughput: Apache Kafka

Search:
- Elasticsearch

Storage:
- Object storage: AWS S3
- Block storage: AWS EBS
- File storage: NFS, AWS EFS
```

---

## 💡 Pro Tips for Interviews

1. **Always start with clarifying questions** - Don't jump to solution
2. **Think out loud** - Interviewer wants to see your thought process
3. **Draw diagrams** - Visual communication is key
4. **Discuss trade-offs** - No perfect solution, show you understand compromises
5. **Consider scale** - Start simple, then discuss how to scale
6. **Use real numbers** - "1 billion users" not "lots of users"
7. **Ask for feedback** - "Does this approach make sense so far?"
8. **Don't over-engineer** - Start with simple solution, iterate

---

## 📖 Recommended Reading Order

**Week 1-2:**
1. System Design Primer (GitHub) - Foundation
2. Grokking the System Design Interview - First 5 chapters

**Week 3-4:**
3. Alex Xu Vol 1 - Chapters 1-7

**Week 5-6:**
4. Alex Xu Vol 1 - Chapters 8-15
5. Start Grokking problems

**Week 7-8:**
6. Alex Xu Vol 2
7. Mock interviews

---

**Next Steps:**
1. Read this guide completely (2-3 hours)
2. Start Week 1 of study plan
3. Move to BEHAVIORAL_PREP.md
4. Follow FAANG_ROADMAP.md for complete timeline

**You've got this! System Design is learnable with consistent practice.** 🚀
