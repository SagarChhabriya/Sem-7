
<img width="538" height="227" alt="image" src="https://github.com/user-attachments/assets/4f726801-3232-43e6-824f-de9708de94cd" />


## 🧩 Step 1: List vertices and edges (with weights)

Edges (bidirectional):

| Edge | Weight |
| ---- | ------ |
| A–B  | 5      |
| A–C  | 9      |
| A–D  | 6      |
| B–C  | 5      |
| C–D  | 4      |
| C–F  | 18     |
| D–E  | 7      |
| E–F  | 4      |
| F–G  | 6      |
| G–H  | 7      |
| F–H  | 12     |
| E–H  | 10     |

---

## 🧮 Step 2: Find degree of each vertex

| Vertex | Connected to | Degree | Parity |
| ------ | ------------ | ------ | ------ |
| A      | B, C, D      | 3      | Odd    |
| B      | A, C         | 2      | Even   |
| C      | A, B, D, F   | 4      | Even   |
| D      | A, C, E      | 3      | Odd    |
| E      | D, F, H      | 3      | Odd    |
| F      | C, E, G, H   | 4      | Even   |
| G      | F, H         | 2      | Even   |
| H      | F, G, E      | 3      | Odd    |

**Odd-degree vertices:** A, D, E, H

---

## 🧠 Step 3: Find shortest paths between all odd vertices

We need shortest distances among A, D, E, H.

| Pair | Shortest Path      | Distance            |
| ---- | ------------------ | ------------------- |
| A–D  | Direct             | 6                   |
| A–E  | A–D–E              | 6 + 7 = **13**      |
| A–H  | A–D–E–H or A–C–F–H | 6 + 7 + 10 = **23** |
| D–E  | Direct             | 7                   |
| D–H  | D–E–H              | 7 + 10 = **17**     |
| E–H  | Direct             | 10                  |

---

## ⚖️ Step 4: Pair the odd vertices (minimum-weight matching)

We need to pair A, D, E, H into two pairs with minimum total distance.

Possible pairings:

| Pairing       | Total Distance    |
| ------------- | ----------------- |
| (A–D) + (E–H) | 6 + 10 = **16** ✅ |
| (A–E) + (D–H) | 13 + 17 = 30      |
| (A–H) + (D–E) | 23 + 7 = 30       |

✅ **Minimum pairing** = (A–D) and (E–H)

---

## 🛠️ Step 5: Duplicate edges along shortest paths

We’ll duplicate edges:

* A–D (6)
* E–H (10)

This makes all vertices even-degree.

---

## 📏 Step 6: Total Chinese Postman route length

Sum of all edges =
5 + 9 + 6 + 5 + 4 + 18 + 7 + 4 + 6 + 7 + 12 + 10 = **93**

Add duplicated edges (6 + 10 = 16):
Total route = **93 + 16 = 109**

---

✅ **Final Answer:**

* **Chinese Postman (minimum closed route) = 109**
* **Duplicated edges:** A–D and E–H
* **Graph becomes Eulerian after duplication.**



<img width="576" height="301" alt="image" src="https://github.com/user-attachments/assets/71707e48-c9cc-4d21-a6df-62d478ca099d" />



## 1) Edges and weights

Left side:

* (AB=8, AC=6, AD=5, BC=7, CD=4)

Middle (parallel edges):

* (CE=12) and another (CE=15)

Right side:

* (EF=11, FH=10, EH=9, EG=14, GH=13)

**Sum of all edge weights**
(8+6+5+7+4+12+15+11+10+9+14+13= \mathbf{114}).

## 2) Vertex degrees → odd vertices

* (A:3) (odd), (B:2) (even), (C:5) (odd; counts both (CE) edges),
  (D:2) (even), (E:5) (odd), (F:2) (even), (G:2) (even), (H:3) (odd).

Odd set: **({A, C, E, H})**.

## 3) Shortest distances among the odd vertices

* (d(A,C)=6) (edge (AC))
* (d(E,H)=9) (edge (EH))
* (d(A,E)=6+12=18) (via (A!-!C!-!E))
* (d(C,H)=12+9=21) (via (C!-!E!-!H))
* (d(A,H)=27) (via (A!-!C!-!E!-!H))
* (d(C,E)=12) (direct (CE))

## 4) Minimum-weight perfect matching on the odd set

Test the three possible pairings:

* ((A,C)+(E,H)=6+9=\mathbf{15})  ✅ minimal
* ((A,E)+(C,H)=18+21=39)
* ((A,H)+(C,E)=27+12=39)

So, **pair (A) with (C)** and **(E) with (H)**, and duplicate those shortest paths:

* duplicate (AC) (cost (6))
* duplicate (EH) (cost (9))

Now all degrees are even.

## 5) Minimum postman length

$$
\text{CPP length} = 114 + (6+9) = \boxed{129}.
$$

## 6) One valid Eulerian circuit (on the augmented graph)

Starting/ending at (A):

$$
A \to C \to E \to H \to F \to E \to G \to H \to E \to C \to B \to A \to D \to C \to A.
$$

This uses each original edge once, plus the duplicated (AC) and (EH) once more (total length (129)).




<img width="529" height="309" alt="image" src="https://github.com/user-attachments/assets/839de793-c3b1-4aac-bc75-2138a80d48f3" />


## 1) List the edges (undirected)

(AB=8,; BC=6,; AC=7,; AD=9,; CD=10,; CE=12,; CE'=13) (a 2nd parallel edge),
(DE=11,; DF=12,; EF=7,; EG=9,; FG=8,; FH=11,; GH=10,; DH=25).

**Sum of all edge weights**
(8+6+7+9+10+12+13+11+12+7+9+8+11+10+25= \mathbf{158}).

## 2) Odd-degree vertices

Degrees:
A=3, B=2, C=5, D=5, E=5, F=4, G=3, H=3.
Odd set = **{A, C, D, E, G, H}**.

## 3) Shortest distances among odd vertices

(Using the graph’s weights.)

* (d(A,C)=7)
* (d(D,E)=11)
* (d(G,H)=10)

(For completeness: (d(A,D)=9,; d(C,E)=12,; d(E,G)=9,; d(D,H)=23,; d(E,H)=18,; d(A,E)=19,; d(C,H)=30,; d(A,G)=28).)

## 4) Minimum-weight perfect matching on the odd set

Try pairings; the cheapest is

$$
(A,C) ;+; (D,E) ;+; (G,H) = 7 + 11 + 10 = \mathbf{28}.
$$

So we **duplicate** the edges (or any shortest paths) for **AC, DE, GH**.

This makes every vertex even → the graph is Eulerian.

## 5) Chinese-Postman length

$$
\text{Minimum tour length} = \text{sum of all edges} + \text{added cost}
= 158 + 28 = \boxed{186}.
$$

## 6) Example Euler circuit (on the augmented graph)

Starting at (A):

$$
A!\to!C!\to!E!\to!D!\to!H!\to!G!\to!E!\to!C!\to!D!\to!F!\to!G!\to!H!\to!F!\to!E!\to!D!\to!A!\to!C!\to!B!\to!A.
$$

(Any Euler tour on the augmented graph will have the same length, **186**.)

