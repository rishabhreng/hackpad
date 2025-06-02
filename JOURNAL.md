---
title: "\"A\" 6-key macropad"
author: "rishabhreng"
description: "A 6-key macropad, in an \"A\" shape, with a 0.91\" OLED display, a rotary encoder, and an addressable LED"
created_at: "2025-05-28"
---
Total time spent: ~8.5 hours

## Day 0 – The Spark

**Time Spent:** ~0.5 hours

I’ve been relearning how to type—my speed is solid, but accuracy is poor. That got me thinking: why not build my own keyboard? Something I could customize, use in college, and evolve over time.

I rediscovered [Hack Club’s Hackpad](https://hackclub.com/hackpad/) project and remembered they offer support for exactly this kind of build. It felt like the right starting point.

---

## Day 1 – First Steps with KiCad  

**Time Spent:** ~1.5 hours  

I jumped into the beginner tutorial. Even though I didn’t fully understand what I was doing—especially with the LED wiring—it sort of made sense by the end. I customized the layout to be 4x1 instead of 2x2. Ugly? A bit. But it’s different, and that matters more right now.

Later that day, I started working in Fusion 360 for the first time. It was frustrating—I spent a good couple of days fighting with the UI trying to make a simple CAD model work.

---

## Day 2 + Day 3 – Expanding the Design  

**Time Spent:** ~2 hours  

I decided I wanted this to be more than just a tutorial clone. So I reviewed the approved parts list and committed to adding:

- A rotary encoder (for volume)
- A slightly unconventional but minimal key layout
- An OLED display (because it’s cool and versatile)

The layout took some work, especially balancing form with function, but the vision started to take shape.

---

## Day 4 – Wiring Woes  

**Time Spent:** ~1 hour  

Wiring got confusing fast. My layout meant I had to use a 3x3 matrix, which left the RP2040 with no free ports. At this point I realized: I was going to need to think like an engineer, not just a maker. I was also running into trouble keeping track of which pins went where.

---

## Day 5 – Matrix Fixes & Firmware Beginnings

**Time Spent:** ~2 hours  

More wiring hell. But something clicked: I could switch to a 3x2 matrix and wire the encoder’s push button directly to the microcontroller, freeing up a pin. I’m still not 100% sure how to process the encoder in firmware the “right” way, but I got the logic down well enough.

I also started working on the KMK firmware. At first, I had no idea how to read the encoder’s push switch—that’s what made me revisit and refine the matrix layout.

---

## Day 6 – Final Assembly in CAD

**Time Spent:** ~1.5 hours  

This was actually fun. I added in the keycaps, switches, rotary encoder, OLED display—even the LEDs—to make sure the full CAD assembly was realistic. Everything fits! It’s clean, functional, and ready to fabricate. KMK firmware done too.

---

## Done!

This project pushed me: KiCad was new, Fusion 360 was even newer, and solving firmware-level issues while managing hardware limitations was a real crash course. But now I have something custom, built for me, and flexible enough to grow with my needs. Next step-make a full keyboard like this, and using Bluetooth.
