## ✅ Quick Guide — Add New Problems & Sections (simple + copy-paste)

---

# 🎯 Add a NEW PROBLEM

### 🔹 1. Create folder

```
problems/MATH/problem-name/
```

Example:

```
problems/MATH/first-derivative/
```

---

### 🔹 2. Create files inside

```
index.html
solution.html
```

---

### 🔹 3. Add ONE card to main `index.html`

Paste inside the grid:

```html
<article class="card" data-tags="calculus math">
  <div class="folder-tag">MATH/FIRST-DERIVATIVE</div>

  <h3>Derivative from First Principles</h3>

  <p>Interactive derivative visualization.</p>

  <div class="btn-group">
    <a href="./problems/MATH/first-derivative/solution.html" class="btn btn-theory">Theory</a>
    <a href="./problems/MATH/first-derivative/index.html" class="btn btn-sim">Run Simulation</a>
  </div>
</article>
```

---

### 🔹 Done ✅

* Click **Calculus**
* Card appears automatically
  (because of `data-tags="calculus math"`)

---

# 🎯 Add a NEW SECTION (sidebar category)

### 🔹 1. Add sidebar button

```html
<li class="nav-item">
  <a href="#" class="nav-link js-filter" data-filter="quantum">
    <span class="ico">Ψ</span>
    <span>Quantum</span>
  </a>
</li>
```

---

### 🔹 2. Tag cards with same name

```html
<article class="card" data-tags="quantum physics">
```

---

### 🔹 Done ✅

Click **Quantum → only those cards show**

---

# 🎯 Folder template (copy each time)

```
problems/
  MATH/
    new-problem/
      index.html
      solution.html
```

---

# 🎯 Naming rules (important)

✅ use:

```
fourier-transform
laplace-solver
wave-equation
```

❌ avoid:

```
infinite well copy
test 1
problemA
```

---

# 🎯 Quick checklist

## New problem

* [ ] create folder
* [ ] add index.html
* [ ] add solution.html
* [ ] add card with correct links
* [ ] set data-tags

## New section

* [ ] add sidebar item with data-filter
* [ ] match same tag in cards

---

That’s it.
No JS edits needed — your filter system handles everything automatically.
