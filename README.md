# lofwyr

*Hey kids, here's some bullets! Don't spend them all in one place.*

## introduction

**heavy wip: this is basically a todo list**

lofwyr is a modular, pure-python tool intended to perform a lightweight security code review. it is completely free, easy to integrate into any existing continuous integration [lifecycle / toolchain](http://lmgtfy.com/?q=github+web+hook), and completely customizable.

note that this is a spare time project, written in desperation due to an unbelievably shit 'startup culture' market for this stuff. if you want a specific feature, let me know and i can look into it, but ::no promises::.

hatemail to lin\_s.

## how to use lofwyr
lofwyr is designed to be simple enough to use anywhere, against any target. just run:

./lofwyr target

the target can be any one of:

- URL (starting with http: or https:
- file
- path
- host

lofwyr will attempt to resolve in the above order: that is, if you call ./lofwyr abcd and you have a file abcd and a host abcd, it will attempt to scan the file instead of the host

## why should i use lofwyr?
lofwyr isn't as comprehensive as some of the commercial security offerings, but you should use it because:

* i'm not lying to you: other products will sell you some bong smoke pipe dream of "big data", "no false positives", "0day protection" and "cloud analytics". i am not financially incentvized to scam you: lofwyr is basically glorified grep, and does not pretend to be more.
* this isn't openly backdoored: other code review products will do everything from sending your code overseas to running unsigned http-fetched code updates. this code sits on github, you can review every socket call yourself, disable them all and check with wireshark.
* this isn't contrast security: from an ethical perspective, i didn't take over leadership of the owasp top ten project and then insert "A7 - Insufficient Application Protection" into the 2017 release candidate document, and then [use an industry best practice standard as advertising](http://www.skeletonscribe.net/2017/04/abusing-owasp.html). i won't claim to be the most morally upstanding person, but lofwyr isn't rancid with corruption.
* designed with compliance in mind: this tool is designed to fulfill corporate security policy compliance requirements - making it easy to tick that checkbox and never give a shit about security again, if you want.
* ez mode integration: most products require weeks of time and thousands of dollars of consulting investment to even get working. this is like owasp zap - just give it to your developers and it'll work standalone, or web hook this into your CI pipe and watch the magic.

