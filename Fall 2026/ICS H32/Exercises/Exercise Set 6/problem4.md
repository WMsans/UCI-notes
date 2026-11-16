# Problem 4

Without a virtual environment, `pip3 install` writes packages into the global
`site-packages` of the interpreter. Since I use Linux, it is not even allowed due to PEP 668. 

As soon as two projects need different versions of the same
library, I'm basically cooked. The problem gets worse with
upgrades, because `pip3 install --upgrade` replaces whatever version was there, 
refletced to every project on that machine.

A virtual environment solves this by giving each project its own
`site-packages`, so projects' dependencies are managed separately, with no conflict. 
It also makes the project's dependencies recordable in `requirements.txt`.
