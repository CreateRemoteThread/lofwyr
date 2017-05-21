# lofwyr

*Hey kids, here's some bullets! Don't spend them all in one place.*

## introduction

**heavy wip: this is basically a todo list**

lofwyr is a modular, pure-python tool intended to perform a lightweight security code review. it is completely free, easy to integrate into any existing continuous integration [lifecycle / toolchain](http://lmgtfy.com/?q=github+web+hook), and completely customizable.

note that this is a spare time project, written in desperation due to an unbelievably shit 'startup culture' market for this stuff. if you want a specific feature, let me know and i can look into it, but ::no promises::.

hatemail to lin\_s.

## why should i use lofwyr?
lofwyr isn't as comprehensive as some of the commercial security offerings, but you should use it because:
* i'm not lying to you: other products will sell you some bong smoke pipe dream of "big data", "no false positives", "0day protection" and "cloud analytics". i am not financially incentvized to scam you: lofwyr is basically glorified grep, and does not pretend to be more.
* this isn't openly backdoored: other code review products will do everything from sending your code overseas to running unsigned http-fetched code updates. this code sits on github, you can review every socket call yourself, disable them all and check with wireshark.
* this isn't contrast security: from an ethical perspective, i didn't take over leadership of the owasp top ten project and then insert "A7 - Insufficient Application Protection" into the 2017 release candidate document, and then [use an industry best practice standard as advertising](http://www.skeletonscribe.net/2017/04/abusing-owasp.html). i won't claim to be the most morally upstanding person, but lofwyr isn't rancid with corruption.
* designed with compliance in mind: this tool is designed to fulfill corporate security policy compliance requirements - making it easy to tick that checkbox and never give a shit about security again, if you want.
* ez mode integration: most products require weeks of time and thousands of dollars of consulting investment to even get working. this is like owasp zap - just give it to your developers and it'll work standalone, or web hook this into your CI pipe and watch the magic.

## how do i use lofwyr
using lofwyr is intended to be quite easy. basically, you fetch a copy of your latest source to given directory. let's call this "/code/repository1". to scan this repository, just call `./start.py /code/repository1`. this will generate a greppable report identifying the security vulnerabilities it found. it will return 0 if it finds no critical vulnerabilities.

if you're on windows, that isn't a problem: lofwyr will have py2exe windows binaries provided in time. 

