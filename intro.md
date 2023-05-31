# Ways to use this guide

Here are a few possible ways to read this, in ascending order of difficulty:

1. Just read it, don't run the code
2. Read it, and copy the Python snippets as you go to assemble a working DNS resolver
3. Translate the Python code into a different language (Javascript! Ruby!
   Go! Elixir! Rust! Your favourite language here!). I find translating working
   code into another language to be a really nice balance of difficulty.
4. Add extra features (there are some "extra fun" ideas at the end!)

## System requirements

You only need Python >= 3.8. No libraries.

The 3.8 requirement is because I've used dataclasses and the walrus `:=`
operator a little bit. But if you only have an older version of Python or if
you don't like those newer features it should also be pretty straightforward to
modify the code to make it run with any Python version, even Python 2. All you
really need are the `socket` and `struct` modules which have been in Python
forever.

I've tested this code on Mac and Linux, but not on Windows. It shouldn't be too hard to make it work on Windows too though.

## How long does it take?

Beta testers of this guide have reported that it takes around 2-4 hours to do
it in Python, and more if you're translating it to another language.

## Knowledge requirements

No specific requirements, other than being somewhat comfortable in Python! I'd
encourage you to try this out even if you're new to DNS and parsing binary
formats. I think writing code is a nice way to learn about some of the concepts.

If you get stuck or confused, here are some resources to learn a little more
about DNS:

free resources:

* my many [DNS blog posts](https://jvns.ca/#dns)
* my talk [Learning DNS in 10 Years](https://jvns.ca/blog/2023/05/08/new-talk-learning-dns-in-10-years/)
* this [dns comic](https://howdns.works/)

paid resources:

* my [How DNS Works](https://wizardzines.com/zines/dns) zine

## This is a toy

Finally: this is a toy implementation that barely works, not a guide to writing
production DNS software. I've never written production DNS software and don't
have any advice about how to do it well, but it's definitely not like this. A couple of links:

* [this long list of RFCs related to DNS](https://www.statdns.com/rfc/) gives you a sense for DNS's actual complexity
* [hello DNS from PowerDNS](https://powerdns.org/hello-dns/) has a teaching implementation that focuses more on standards compliance and correctness
