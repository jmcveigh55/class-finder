# Class Finder

| Author | Email |
| ------ | ----- |
| Jack McVeigh | <jmcveigh5@gmail.com> |

---

## Purpose
To quickly find a class that has been archived. Over the course of college,
I have taken many classes, and at times want to reference old materials to
copy code or understand a circuit. However, it can be hard to remember what quarter
I took a class in, making the task of finding the class harder than needed. This program
essentially walks the quarters/ directory to find the specified class or classes.

---

## Installation
To install, run the following:
```bash
git clone https://github.com/jmcveigh55/class-finder.git
cd class-finder
python3 setup.py install
```

---

## Use

* How classes are stored:
>```bash
>export QUARTERS_PATH="PATH/TO/WHERE/QUARTERS/ARE/>STORED"
>```
>Example class:
>```bash
>$QUARTERS_PATH/Quarter-XX-YYYY-Season/XXX-XX/
>```

>* To find a class:
>```bash
>class-finder ECE-101
>```

>* To find multiple class:
>```bash
>class-finder ECE-101 CHIN-101
>```