# Chapter 1 - Can a Computer Learn y = 2x?

**Bro:** Alright computer, today is the day.

**Computer:** Finally. Are you giving me a GPU?

**Bro:** No.

**Computer:** More memory?

**Bro:** No.

**Computer:** A fancy AI library?

**Bro:** Nope.

**Computer:** Ahhh man... seriously? You woke me up just to give me Python and hope I become intelligent?

**Bro:** Exactly.

**Computer:** This feels suspiciously like unpaid work.

**Bro:** Relax. You're about to learn your first skill.

**Computer:** What skill?

**Bro:** Finding patterns.

---

**Computer:** Okay, at least give me the formula.

**Bro:** No.

**Computer:** Wait... what?

**Bro:** You have to figure it out yourself.

**Computer:** Bro... you literally know the answer already.

**Bro:** Yes.

**Computer:** And you are just going to watch me struggle?

**Bro:** Yes.

**Computer:** Wow. I thought humans were supposed to teach computers.

**Bro:** Welcome to machine learning.

---

## The Mission

Find the hidden pattern.

Here are your only clues:

| x | y |
|---|---|
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |
| 4 | 8 |
| 5 | 10 |

**Computer:** That's it?

**Bro:** That's it.

**Computer:** No explanation?

**Bro:** Nope.

**Computer:** No hints?

**Bro:** Nope.

**Computer:** Bro, you are basically throwing me into an exam without teaching me anything.

**Bro:** Exactly.

**Computer:** I hate this.

**Bro:** Good. That means you're ready to learn.

---

## What are we building?

A tiny neuron.

Not the fancy AI stuff you hear about.

No TensorFlow.

No PyTorch.

No magic.

Just Python and some math.

The computer starts with:

- No knowledge
- Random guesses
- Zero understanding of the pattern

Its job:

1. Make a guess.
2. Check how wrong it is.
3. Improve the guess.
4. Repeat.

---

## The Goal

By the end of this chapter, our computer should look at the examples and discover:


y ≈ 2x


Then we can proudly tell it:

**Bro:** Wait... you actually learned something?

**Computer:** Obviously.

**Bro:** You were literally useless five minutes ago.

**Computer:** I prefer the term "untrained".

---

## Run it

```
python main.py
```

## The Result

**Computer:** Bro... I think I figured it out.

**Bro:** Really?

**Computer:** I started with random guesses, but now my predictions are much closer.

**Bro:** Nice. Did you discover the exact answer?

**Computer:** Not exactly.

**Bro:** Why not?

**Computer:** I kept trying to improve, but at some point I couldn't get any closer.

**Bro:** Interesting.

**Computer:** So... I failed?

**Bro:** No. You learned something.

**Computer:** But I didn't get the perfect answer.

**Bro:** Learning is not always about getting everything perfect. It's about improving from where you started.

**Computer:** So I went from knowing nothing to finding the pattern?

**Bro:** Exactly.

**Computer:** Not bad for my first day.

**Bro:** Not bad. But there is still a problem.

**Computer:** What problem?

**Bro:** You don't know why you improved or which direction you should move.

**Computer:** Ahhh man... so there is more math?

**Bro:** Yep.

**Computer:** I knew this was too easy.

---

## What we learned

In this chapter, we built a tiny neuron completely from scratch.

The neuron can:

- Take an input
- Make a prediction
- Compare the prediction with the real answer
- Adjust itself to improve

But our learning method was very basic.

The computer could improve, but it didn't really understand:

- How much it should change
- Which direction it should move
- Why some changes improve the result

Next chapter:

**Chapter 2 - How does a neuron know which direction to move?**

We introduce the idea that powers modern neural networks:

**Gradient Descent**
