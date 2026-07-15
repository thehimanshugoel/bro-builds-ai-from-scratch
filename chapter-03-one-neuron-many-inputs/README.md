# Chapter 3 - One Neuron, Many Inputs

**Computer:** Bro...

**Bro:** Yes?

**Computer:** I think I'm getting smarter.

**Bro:** You are.

**Computer:** Then give me something harder.

**Bro:** Alright.

**Computer:** Another equation?

**Bro:** Better.

**Computer:** Bigger numbers?

**Bro:** Better.

**Computer:** A real-world problem?

**Bro:** Exactly.

---

## Looking Back

In Chapter 1, we built our very first neuron.

The neuron learned to predict:

```
y ≈ 2x
```

In Chapter 2, we improved the way it learned.

Instead of randomly adjusting its weights, it learned using Gradient Descent.

The neuron could now:

- Make a prediction
- Measure how wrong it was
- Calculate the direction that reduces the error
- Improve itself step by step

Pretty impressive.

But there was still one huge limitation.

---

## The Problem

**Bro:** Let me ask you something.

**Computer:** Go ahead.

**Bro:** Last chapter your prediction looked like this:

```python
prediction = weight * x + bias
```

**Computer:** Right.

One input.

One weight.

One prediction.

**Bro:** Do you think every real-world problem depends on just one number?

**Computer:** Probably not.

**Bro:** Let's imagine we're trying to predict someone's salary.

Would you only look at their years of experience?

**Computer:** No.

I'd also look at:

- Education
- Skills
- Certifications
- Projects

**Bro:** Exactly.

Real life is rarely that simple.

---

## A Bigger Challenge

Instead of one input:

```
Experience = 5
```

Suppose we have several:

```
Experience = 5

Education = 4

Projects = 12

Certifications = 3
```

**Computer:** Wait...

Which one is `x`?

**Bro:** None of them.

Your neuron isn't built for this yet.

---

## One Weight Isn't Enough

**Computer:** Can't I use the same weight for everything?

**Bro:** Think about it.

Should one extra year of experience affect someone's salary the same way as completing one extra project?

**Computer:** Probably not.

**Bro:** Exactly.

Different inputs have different importance.

Each input needs its own weight.

---

## A Smarter Neuron

Instead of this:

```python
prediction = weight * x + bias
```

Our neuron now thinks like this:

```
Experience     × Weight₁

Education      × Weight₂

Projects       × Weight₃

Certifications × Weight₄
```

Then it adds everything together.

Finally, it adds the bias.

Our prediction becomes:

```python
prediction = (
    w1 * x1 +
    w2 * x2 +
    w3 * x3 +
    w4 * x4 +
    bias
)
```

Congratulations.

You've just built a neuron that can look at multiple pieces of information before making a decision.

---

## Building It In Python

Instead of passing a single value:

```python
prediction = neuron.predict(5)
```

We'll pass a list of inputs:

```python
inputs = [5, 4, 12, 3]

prediction = neuron.predict(inputs)
```

Instead of storing one weight:

```python
weight
```

We'll store multiple weights:

```python
weights = [
    w1,
    w2,
    w3,
    w4
]
```

Now the neuron will multiply every input by its corresponding weight and add everything together.

---

## How Does It Work?

Imagine:

```
Inputs:

[5, 4, 12, 3]

Weights:

[0.8, 1.2, 0.3, -0.5]
```

The neuron calculates:

```
(5 × 0.8)
+
(4 × 1.2)
+
(12 × 0.3)
+
(3 × -0.5)
+
bias
```

That final number becomes the prediction.

---

## Python Makes This Easy

We'll pair each input with its matching weight.

```python
prediction = bias

for x, w in zip(inputs, weights):
    prediction += x * w
```

It may look simple...

But this tiny loop is doing something incredibly important.

In mathematics, this operation is called the **dot product**.

Almost every modern neural network performs this operation millions—or even billions—of times during training.

Today, you've built it yourself.

No AI libraries.

Just Python.

---

## What You'll Learn

In this chapter we'll build:

- Multiple inputs
- Multiple weights
- Predictions using many features
- Dot product intuition
- A more realistic neuron

Still no AI libraries.

Still just Python.

Still building everything from scratch.

---

## Run It

```bash
python main.py
```

---

## Expected Result

**Computer:** Bro...

**Bro:** Yes?

**Computer:** I don't just look at one thing anymore.

**Bro:** What do you mean?

**Computer:** Before making a prediction, I can consider multiple pieces of information.

**Bro:** Exactly.

**Computer:** That feels much closer to how humans think.

**Bro:** And much closer to how real neural networks work.

---

## What We Learned

In this chapter, we upgraded our neuron.

Instead of making decisions using only one input, it can now combine multiple features to make a prediction.

Each feature has its own weight because not every piece of information is equally important.

Although our neuron is still very simple, it now resembles the basic building block used inside modern neural networks.

Today, our neuron learned to see more of the world.

---

## Next Chapter

**Computer:** Bro...

**Bro:** Yes?

**Computer:** I can now understand many inputs.

**Bro:** You can.

**Computer:** So I can solve any problem now?

**Bro:** Not quite.

**Computer:** Why not?

**Bro:** Because every prediction you make is still a straight line.

**Computer:** And the real world isn't made of straight lines?

**Bro:** Exactly.

Next Chapter:

# Chapter 4 - When Straight Lines Aren't Enough