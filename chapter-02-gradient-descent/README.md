# Chapter 2 - How Does a Neuron Learn Better?

**Computer:** Bro...

**Bro:** Yes?

**Computer:** I've been thinking.

**Bro:** That's a good sign.

**Computer:** In the last chapter, you said I was basically guessing.

**Bro:** I did.

**Computer:** So... I wasn't actually learning the smartest way?

**Bro:** Not yet.

**Computer:** Wow.

**Bro:** Don't look so disappointed.

**Computer:** I thought I was becoming intelligent.

**Bro:** You were.

**Computer:** Then why wasn't my learning perfect?

**Bro:** Because you only knew *that* you were wrong.

**Computer:** Isn't that enough?

**Bro:** Knowing you're wrong is only half the battle.

**Computer:** What's the other half?

**Bro:** Knowing how to become less wrong.

---

## Looking Back

In Chapter 1, we built our very first neuron from scratch.

The neuron could:

- Take an input
- Make a prediction
- Measure how wrong it was
- Adjust its weight and bias
- Repeat the process

Eventually, it learned that:

```
y ≈ 2x
```

Not bad for a computer that started knowing absolutely nothing.

---

## The Problem

**Computer:** Bro... can I ask something?

**Bro:** Sure.

**Computer:** Last chapter, every time I made a prediction, I used:

```python
prediction = weight * x + bias
```

Then I calculated my mistake:

```python
error = actual - prediction
```

And finally I learned like this:

```python
self.weight += error * 0.01
self.bias += error * 0.01
```

**Computer:** Every time I made a mistake, my weight and bias changed.

**Bro:** That's right.

**Computer:** But... why did they change like that?

**Bro:** What do you mean?

**Computer:** Why did I update my weight using:

```python
self.weight += error * 0.01
```

**Computer:** Why not:

```python
self.weight -= error * 0.01
```

or

```python
self.weight += error * 0.1
```

or even

```python
self.weight += error * x
```

**Computer:** How did I know which one was correct?

**Bro:** You didn't.

**Computer:** Wait... I didn't?

**Bro:** No.

**Computer:** Then who decided to use:

```python
self.weight += error * 0.01
```

**Bro:** We did.

**Computer:** You mean... the programmer?

**Bro:** Exactly.

**Computer:** So I wasn't actually deciding how to improve my weights?

**Bro:** Correct.

**Computer:** I was simply following the rule that you wrote in Python.

**Bro:** Exactly.

**Computer:** Then how do real neural networks decide whether a weight should increase or decrease?

**Bro:** They don't rely on handcrafted rules.

**Computer:** Then what do they use?

**Bro:** Mathematics.

**Computer:** That sounds... terrifying.

**Bro:** Don't worry. It's much simpler than it sounds.

Today, we'll teach you one of the most important algorithms in machine learning.

---

## Learning Smarter

**Computer:** So how do humans solve this?

**Bro:** Instead of walking randomly, they look for the direction that goes downhill.

**Computer:** Even if they can't see the whole mountain?

**Bro:** Exactly.

**Computer:** So every step gets them closer to the bottom?

**Bro:** That's the idea.

**Computer:** Wait...

**Computer:** Is my loss function the mountain?

**Bro:** Now you're thinking like a machine learning engineer.

---

## Our Goal

Instead of randomly adjusting our neuron, we'll teach it how to find the direction that reduces its mistakes.

This technique is called:

# Gradient Descent

Don't worry if the name sounds complicated.

By the end of this chapter, it will simply mean:

> "Take a small step in the direction that makes the prediction better."

---

## What You'll Learn

In this chapter we'll build Gradient Descent from scratch.

We'll learn:

- Why our previous learning method was limited
- What a gradient represents
- Why we update weights instead of guessing
- What a learning rate is
- Why learning happens one small step at a time
- How modern neural networks improve themselves

Still no AI libraries.

Still just Python.

Still building everything ourselves.

---

## Training Data

We'll continue using the exact same dataset.

| x | y |
|---|---|
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |
| 4 | 8 |
| 5 | 10 |

Since the problem hasn't changed, we'll clearly see how a better learning algorithm improves the results.

---

## Run it

```bash
python main.py
```

---

## Expected Result

**Computer:** Bro...

**Bro:** Yes?

**Computer:** I don't feel like I'm guessing anymore.

**Bro:** Why?

**Computer:** Every update has a purpose.

**Bro:** Exactly.

**Computer:** Instead of wandering around, I know which direction reduces my mistakes.

**Bro:** Congratulations.

**Computer:** Am I intelligent now?

**Bro:** Let's not get ahead of ourselves.

**Computer:** Fair enough.

---

## What We Learned

In this chapter, we taught our neuron how to learn more intelligently.

Instead of making random adjustments, it now updates its weights by following the direction that reduces the loss.

This simple idea—Gradient Descent—is one of the most important algorithms in machine learning.

Modern neural networks may contain millions or even billions of parameters, but many of them still rely on this same core principle.

Today, our neuron learned how to take smarter steps.

---

## Next Chapter

**Computer:** Bro...

**Bro:** What now?

**Computer:** One input is getting boring.

**Bro:** I was waiting for you to say that.

Next Chapter:

# Chapter 3 - One Neuron, Many Inputs

We'll teach our neuron that real-world problems aren't solved using a single number.

Instead of one input and one weight, we'll introduce multiple features and multiple weights—the next step toward building real neural networks.