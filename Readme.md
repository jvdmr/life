John Conway's Game of Life
==========================

As a tribute to [John H. Conway](https://en.wikipedia.org/wiki/John_Horton_Conway), who died April 11th, 2020 (yesterday), and as a simple exercise in Python programming, today I spent a few hours implementing his Game of Life and reflecting on his legacy.

This is the result.

How to run
----------

To run the famous (Gosper's Glider Gun) simulation:
```
./run.sh
```

To run a random simulation of 80x24 with 500 living cells to start with:
```
python src/life.py 24 80 500
```

Peculiarities
-------------

In my implementation, I decided to enable wrap-around calculation. This means that cells on the edge count the cells on the opposite edge as their neighbours. Because of this, patterns are not affected by the edges of the field and can simply pass through to the other side.

There is no speed limitation except for the one imposed by your CPU. This simulation runs single-threaded, so it can get quite slow if you try to run very large simulations and/or are working with an older CPU.
