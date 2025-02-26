---
---

<blockquote markdown="1">

A week of hard work can sometimes save an hour of thought.

--- <span i="Wilson, Robert">Robert Wilson</span>

</blockquote>

Building large programs with other people is different from building small
programs on your own in two important ways. The first is communication: in order
for you and your teammates to collaborate, you need to agree about what you're
collaborating *on*, which means you need to tell each other how you are breaking
the problem up into pieces and how those pieces will interact <span
x="communicate"/>.

The second difference between programming in the small and <span i="programming
in the large">programming in the large</span> is that while you can hack your
way from an empty `.js` or `.py` file to a hundred-line program in a reasonable
time, the re-work required by that strategy becomes unaffordable when your final
product is a thousand lines long.

To see why, suppose the final program is $$N$$ lines long and is made up of
chunks that are each $$L$$ lines long, so there are $$C = N/L$$ chunks in total.
You write chunks one by one; each time you add one, there is a probability $$p$$
that each of the chunks already written needs to be rewritten.  How many chunks
do you actually wind up writing?

-   The first chunk always needs to be written, so that's 1.

-   When you write the second chunk you need to rewrite the first chunk with
    probability $$p$$, so the likely cost of the second chunk is $$1+p$$.

-   The likely cost of the third chunk is $$1+2p$$, since you might have to
    rewrite either or both of the first two chunks.

-   In general, the cost of adding chunk $$i$$ is $$1+(i-1)p$$, so the total cost
    of writing $$C$$ chunks is $$C + p\sum_{i=0}^{C-1}{i}$$, which is
    $$C + p(C-1)(C-2)/2$$ or $$pC^{2}/2 + (1-p)C + 1$$.

This <span i="model!of software development">model</span> is unrealistic in
every way---the odds of rewriting old code is lower than the odds of rewriting
recent code, for example---but it captures a key point: the cost of rework grows
faster than the number of pieces of work.  You can't lower $$C$$ by increasing
$$L$$ (since as <span x="thinking"/> explains, there's a limit to how much you
can hold in your mind at once), so your goal when designing software is to lower
$$N$$ by re-using code from libraries or to reduce the cost of reworking things
by lowering $$p$$.

I can't tell you how to design software, and I don't know anyone who can. I can
*show* you by working through examples on a whiteboard, asking rhetorical
questions, and setting problems for you to think about, but that doesn't
translate well to print.  I can also tell you how to describe designs and how to
tell a good design from a bad one, so we'll start with that.

<div class="callout" markdown="1">

### Learning by example

The best way to learn design in any field is to study examples
<cite>Schon1984,Petre2016</cite>, and some of the best examples of software
design come from the tools programmers use in their own work.
<cite>Kernighan1979,Kernighan1981,Kernighan1983</cite> introduced the Unix
philosophy to an entire generation of programmers;
<cite>Brown2011,Brown2012,Brown2016</cite> and [Mary Rose
Cook][cook-mary-rose]'s [Gitlet][gitlet] take this approach as well.  There is
also *[Software Tools in JavaScript][stjs]*, which was developed in tandem with
this material and can be used as a starting point for many different class
projects.

The discussion of how to design for test in <span x="testing"/> is another
example of teaching by example. A general rule like, "Building components that
can easily be replaced makes testing easier," would only have been meaningful if
you already understand the point; explaining it with a specific example (testing
an MVC application) made it more relatable.

</div>

## Describing Designs

<cite>Cherubini2007</cite> found that developers usually don't draw <span
i="software design!role of diagrams">diagrams</span> to create a permanent
record of design. Instead, they use diagrams as an aid to conversation in the
moment---essentially, as a temporary store for ideas that they wouldn't
otherwise be able to keep track of (<span x="thinking"/>). In many cases, the
people who drew the diagrams couldn't make sense of them a day later; it could
be that the benefit of diagrams therefore comes from the act of drawing, not
from having them to study.

When experienced developers *do* draw something for later use, they generally
draw the following:

<span i="diagrams!data structure; data structure diagrams">Data structures</span>.
:   These are blob-and-arrow pictures of the objects and containers that make up
    the program and the references that stitch them together. The more
    experience someone has, the fewer of these they need to draw, but everyone
    falls back on them eventually (particularly during difficult debugging
    sessions).

The systems' <span g="conceptual_architecture" i="conceptual architecture!diagram; diagrams!conceptual architecture">conceptual architecture</span>.
:   This shows how the important parts of the system fit together. It's also
    the least constrained, since it can include everything from specific
    sections of configuration files to class hierarchies to replicated web
    servers. What qualifies as "important" depends on what aspect(s) of the
    system you're currently concerned with. If I'm trying to explain a bug that
    only arises when the application is configured incorrectly, I might draw its
    configuration files, and the database tables that store user preferences,
    but leave out the password database and log files entirely. If we're trying
    to figure out a better load balancing strategy, on the other hand, I would
    draw most of what would go into a physical architecture diagram, plus just
    enough of the class inheritance hierarchy to show how the servers will load
    user request handlers dynamically.

The system's <span i="physical architecture!diagram; diagrams!physical architecture">physical architecture</span>.
:   This is the files, processes, sockets, database tables, etc., that make it
    up. In most cases, this consists of a bunch of boxes representing the
    machines the application's components run on, trees showing files and
    directories, and circles showing running processes. A lot of this stuff can
    show up in the conceptual architecture as well.

<span g="workflow_diagram" i="workflow diagram; diagrams!workflow">Workflow diagrams</span> that show how users accomplish things.
:   Workflows are almost always drawn as <span g="fsm" i="finite state
    machines!use in software design">finite state machines</span>. Each node
    represents a state the user and the system can be in, while the arcs show
    how to get from one state to another.

Schemas or data models.
:   These can be fairly literal pictures of the tables in a database, possibly
    augmented with arrows to show what's a foreign key for what, or <span
    g="er_diagram" i="entity-relationship diagram;
    diagrams!entity-relationship">entity-relationship diagrams</span> that also
    show which relationships are one-to-one, one-to-many, and so on (<span
    f="er-diagram"/>).

{% include figure
   id="er-diagram"
   img="er-diagram.svg"
   alt="Entity-relationship diagram"
   cap="An example of an entity-relationship diagram for students, instructors, and courses." %}

The two kinds of diagram that I find most useful are ER diagrams and a
combination of conceptual and <span g="use_case_map" i="use-case map;
diagrams!use-case map">use-case maps</span> <cite>Reekie2006</cite>.  The
background of a use-case map is the system's conceptual architecture; the
overlay traces what happens during a particular workflow (<span
f="use-case-map"/>).  I find these particularly useful for checking the behavior
of systems built from lots of <span g="microservice"
i="microservice">microservices</span>.

{% include figure
   id="use-case-map"
   img="use-case-map.png"
   alt="Use case maps"
   cap="An example of a use case map (from Reekie2006)." %}

<div class="callout" markdown="1">

### UML and why not

I'm not a fan of the <span g="uml" i="Unified Modeling Language">Unified
Modeling Language</span> (UML). It defines over a dozen different types of
diagrams for showing the relationships between classes, the order in which
things happen when methods are invoked, the states a system goes through when
performing an action, and so on.  Hundreds of books and thousands of articles
have been written about UML, but in all the years I've been programming, I've
only ever met one person who drew UML diagrams of his own free will on a regular
basis. I've known a handful of other people who occasionally sketched class
diagrams as part of a larger description of a design, and that's pretty much
it. Unlike blueprints in architecture or flow diagrams in chemical engineering,
UML doesn't actually seem to help practitioners very much
<cite>Petre2013</cite>.

If you have to use UML because it's a course requirement, [PlantUML][plantuml]
will convert specially-formatted text into diagrams for you, and the former are
much easier for version control systems to work with.  In my opinion, though,
you'll get more out of investing time in the modeling tools described at the end
of <span x="tooling"/>.

One often-overlooked finding about visualization is that people understand <span
i="flowchart">flowcharts</span> better than pseudocode *if both are equally well
structured* <cite>Scanlan1989</cite>.  Earlier work showing that pseudocode
outperformed flowcharts used structured pseudocode and tangled flowcharts; when
the playing field was leveled, novices did better with the graphical
representation.

</div>

## Getting Started

Suppose you're starting with a blank sheet of paper (or an empty whiteboard):
how do you describe something that doesn't exist yet? The best way to start is
to write your <span i="elevator pitch">elevator pitch</span> (<span
x="starting"/>). Next, write one or two point-form <span g="user_story" i="user
story!use in software design">user stories</span> describing how the
application, feature, or library would be used. Be as concrete as possible:
instead of saying, "Allows the user to find overlaps between their calendar and
their friends' calendars," say:

1.  The user selects one of her friends' calendars.

1.  The system displays a page showing how the busy/not-busy times in that
    person's calendar overlaps with the user's.

1.  The user can then add more of her friends' calendars one by one or remove
    any calendars except her own. The system updates the display after each
    action to show how many people overlap where.

As short as it is, this story tells us that:

-   People have friends.

-   Calendars are added one at a time rather than in a batch.

-   The user's own calendar is always displayed.

-   We need to decide how to show the density of overlaps, not just all-or-none.

Once you have half a dozen of these stories, go through and highlight the key
things and relationships you have described. In the example above, you would
highlight "user", "friend", "calendar", and "page". As soon as you try to draw a
diagram showing how these are related to one another, you'll have to start
making design decisions: for example, is "friend" an entity, or a relationship
between two entities (i.e., is it a blob or an arrow)?

If you hear yourself say, "We'll use a linked list to…"  step back and catch
your breath. Details like that do need to be worked out at some point, but:

-   you're probably worrying about that as a way to *not* think about the bigger
    design questions (which are scarier for beginners);

-   you probably don't know enough yet about your design to make the right
    decision; and

-   you're probably a good enough coder by now that you can worry about that
    when the time comes to actually write the code. Remember, not everything
    actually needs to be designed.

Once you have a diagram---any kind of diagram---start iterating around it. Pick
one open problem like, "How do users control who can see their calendars?"),
think of a way to solve it ("they can mark them as 'public', or invite specific
people to view them"), figure out how to implement your solution, then revisit
any previous decisions that your most recent decisions affect. Design is a very
cyclic process: every time you add or change one thing, no matter how small, you
may need to go back and re-design other things.

There are three traps here for the inexperienced. The first is <span
g="analysis_paralysis" i="analysis paralysis">analysis paralysis</span>, where
you find yourself revisiting issues over and over again without ever making any
decisions that stick. The second is <span g="nih" i="not invented here
syndrome">not invented here</span> syndrome, which leads people to say, "Sure,
there's a library that does that, but I didn't write it so I'm not going to use
it."  Its complement is <span g="aih" i="already invented here syndrome">already
invented here</span> syndrome, in which someone says, "Look, we've already made
a decision about that, let's not reopen the debate." Any of these can sink a
project; together, they show why it's so hard to teach design, since what I'm
basically saying is, "Argue enough, but not too much."

<div class="callout" markdown="1">

### How experts do it

One of the biggest differences between <span i="expert">experts</span> and
non-experts in any field is how quickly experts can rule out possibilities
<cite>Schon1984</cite>. Whether it is software design, chess, or medical
diagnosis, <span i="novice">novices</span> check to see if their plan will work;
experts, on the other hand, search for a refutation---a reason why it won't---so
that they can narrow their focus as early as possible. One way to do this is to
jump back and forth between a high-level plan and its low-level consequences; if
one of those consequences reveals a flaw in the plan, they go back to the high
level and make a correction. Doing this efficiently depends on having experience
of past failures so that you know how a good idea might fail in practice.

</div>

## Design for Evolution

How easily we can swap one component for another in order to test a system is
one way to tell how well designed that system is (<span x="testing"/>). Another
is how easily we can modify or <span i="software design!evolution">extend</span>
the system to do new things. If our design is perfect, we can implement changes
by adding code without modifying what's already there.  This is called the <span
g="open_closed_principle" i="Open-Closed Principle">Open-Closed
Principle</span>: systems should be open for extension, but closed for
modification.

For example, suppose that we are simulating a hospital emergency room. We could
write the function that simulates someone's response to a cardiac arrest like
this:

```py
def handle_cardiac_arrest(all_actors):
    for actor in all_actors:
        if actor.kind == 'nurse':
            ...do something...
        elif actor.kind == 'doctor':
            ...do something else...
        else:
            ...do some default action...
```

{: .continue}
(The term <span g="actor">actor</span> is often used in simulations to mean
"anything that can take actions".) If we want to add another kind of actor, we
need to modify this code to add another `elif` clause, and if we want to add
another kind of event, we have to write another function *and* make sure we
have an `if` or `elif` for kind of actor.

A better design is to create a base class that defines a generic behavior for
all actors:

```py
class Actor:
    def __init__(...):
        ...do generic setup...
    def handle_cardiac_arrest(self):
        pass # by default, don't do anything
```

{: .continue}
and then derive one class for each type of actor:

```py
class Nurse(Actor):
    def handle_cardiac_arrest(self):
        ...do something...

class Doctor(Actor):
    def handle_cardiac_arrest(self):
        ...do something else...
```

We can then ask each actor to handle the cardiac arrest however they're supposed
to:

```py
def handle_cardiac_arrest(all_actors):
    for actor in all_actors:
        actor.handle_cardiac_arrest()
```

{: .continue}
If we want to add another kind of actor, we derive another class from `Actor`
and override methods to give it the behaviors we want: the general
`handle_cardiac_arrest` function doesn't need to change.

This design isn't perfect, though.  If we want to add another kind of event, we
need to define a default response to it by adding a method to `Actor`, then
override that method for the specific kinds of actors that have different
behaviors. A more sophisticated design would define classes to represent events
and select a method to call based on the event:

```py
class Actor:
    def __init__(...):
        ...do generic setup...
    def handle_event(self, event):
        if self.has_handler_for(event):
            handler = self.get_handler_for(event)
            handler(event)
        else:
            self.default_action(event)
```

This design makes it harder to figure out exactly who's doing what, but ensures
that we can add new actors *and* new events without having to go back and change
old code.

But how can we be sure that our new code is going to do what the old code
expects? The answer is a technique called <span g="design_by_contract" i="design
by contract">design by contract</span>. Every function or method specifies <span
g="pre_condition" i="pre-condition">pre-conditions</span> that must be true of
its inputs in order for it to run successfully and <span g="post_condition"
i="post-condition">post-conditions</span> that are guaranteed to be true of its
results. <span g="type_declaration" i="type declaration!use in software
design">Type declarations</span> are the most common kind of pre-condition and
post-condition: they say things like, "The input must be a list of strings,"
and, "The output is a single string." More sophisticated pre-conditions and
post-conditions can be written as assertions that (for example) check that all
the input strings are at least one character long or that the output is one of
the input strings.

Design by contract gets its name from the fact that a function's pre-conditions
and post-conditions work like a business contract: if the caller guarantees that
the inputs meet the pre-conditions, then the function guarantees that the output
meets the post-conditions. Contracts like these are particularly useful when
overriding methods or when software evolves:

Pre-conditions can only be made <span i="pre-condition!weakening">weaker</span>.
:   This rule is another way of saying that the new version of the code can only
    put *fewer* restrictions on the inputs it accepts, or equivalently, it must
    handle everything the old version could, but may handle more. If code breaks
    this rule, then it might fail in cases where the old code ran.

Post-conditions can only be made <span i="post-condition!strengthening">stronger</span>.
:   This rule ensures that the new function can't produce anything that the old
    function might not have produced, and ensures that anything using the
    function's output will be able to handle everything the new version gives
    it.

A programming language called <span i="Eiffel">[Eiffel][eiffel]</span>
demonstrated how powerful design by contract can be. Most other languages don't
support it directly; we can emulate it by putting assertions at the start and
end of our functions and methods, but there's no guarantee they'll be checked or
enforced in derived versions.

## Design for Accessibility

Close your eyes and try to navigate this website. Now imagine having to do that
all day, every day. Imagine trying to use a computer when your hands are
crippled by arthritis.  Better yet, don't imagine it: have one of your teammates
tape some popsicle sticks to your fingers so you can't bend them and then see
how easy it is to use something like Slack.

Making software <span i="accessibility; software
design!accessibility">accessible</span> doesn't just help people with obvious
disabilities: as <cite>Johnson2017</cite> points out, the population is aging,
and everything you do to help people who are deaf also helps people who are
gradually losing their hearing.

The best short guide I have found for accessible design is [this set of posters
from the UK Home Office][uk-home-office-a11y]. Each one lays out a few simple
do's and don'ts that will help make your software accessible to people who are
neurodivergent, use screen readers, are dyslexic, have physical or motor
challenges, or are hard of hearing. You can also use tools like <span
i="accessibility!WebAIM WAVE; WebAIM WAVE">[WebAIM WAVE][webaim-wave]</span> to
check for common problems, most of which are easy to fix. It only takes a few
minutes, it's the compassionate thing to do, and almost every change you make
will also make the software easier to test and maintain.

## Scriptability

Rule #3 of <cite>Taschuk2017</cite> is, "Make common operations easy to
control."  Like testing, it's a lot easier to do if you design programs with
this goal in mind, and programs that are designed to do this tend to be
easier to understand, test, and extend.

You can make programs controllable in at least three different ways:

Command-line options.
:   Enable users to run it and control its operation from the command line. For
    example, the `-a` or `--all` option could tell the program to process all
    files even if there are errors, while `-o` or `--output` could specify the
    name of the output directory.

Configuration files.
:   Have the program load settings from one or more configuration files.  This
    option saves them typing in common settings over and over, and also provides
    a record of exactly what the settings were (which can be helpful when
    testing).
    <br/>
    Configuration files are often <span i="configuration!layered"
    g="layered_configuration">layered</span>: the program reads a global
    configuration file with general settings, then a user-specific configuration
    file (typically in the user's home directory) with the user's preferences,
    and finally a project-specific file. Those settings can then often be
    overridden using command-line options.  And if you are going to *read*
    settings from files, do the compassionate thing and teach your programs how
    to *write* their complete settings to a file as well.  These files make it
    easier for people to reproduce their work and are an invaluable aid to
    debugging.

A programming interface.
:   If the application is written as a set of libraries, each with its own API,
    then the interface the general user sees can be written as a thin layer that
    combines those libraries. Users can then write code of their own to control
    the libraries if they want to extend the application's behavior.

The last of these is what we mean by saying that something is <span
g="scriptable" i="scriptability; software
design!scriptability">scriptable</span>.  One of the things that made Microsoft
Office so popular was users' ability to write scripts for Word, Excel, and other
tools in <span i="Visual Basic">[Visual Basic][visual-basic]</span>.  Today,
many games include a scripting language like <span i="Lua">[Lua][lua]</span> so
that users can write modifications right then and there.  Scripting is
particularly helpful when you want to test a user interface, since it allows you
to write short programs that trigger events like "click this button" or "enter
this password" and to interrogate the system's state afterward.

<div class="callout" markdown="1">

### Merely useful

Why do we call them scripts instead of programs, and why do we call it scripting
instead of programming? The answer, I think, is that if everyone can do it, it
can't be cool: as a computer science professor said to me once about something
similar, "I realize it's popular, but it's merely useful."

</div>

The other way to script something is through an external interface.  Most web
applications these days provide some sort of <span g="rest" i="Representational
State Transfer; REST">REST</span> API so that programs can send requests or post
data via HTTP to control the app's behavior. Many of these require programs to
authenticate in order to prove that they have a right to do what they want to;
as soon as we're thinking about that, we need to think about the topic of the
next chapter: security.

## Design for Packaging

Every language and operating system has its own rules for <span i="packaging;
package!building">building packages</span>; designing software with these rules
in mind makes packaging a lot easier.  In Python, for example, a package
consists of one or more Python source files in a specific directory structure
like this:

```txt
pkg_name
+-- pkg_name
|   +-- module1.py
|   +-- module2.py
+-- README.md
+-- setup.py
```

The top-level directory is named after the package.  It contains a directory
that is also named after the package, which contains the package's source files.
To turn this into an installable package, we put the following in `setup.py`:

```py
from setuptools import setup

setup(
    name='pkg_name',
    author='Some Name',
    version='0.1.0',
    packages=['pkg_name'])
```

{: .continue}
The `name` and `author` fields are self-explanatory; the `packages` field lists
the sub-directories containing packages (there may actually be several), and
we'll talk about versioning in <span x="delivery"/>.  Once you have this in
place, you can run:

```sh
$ pip install .
```

{: .continue}
to create a package.

## Find Your Current Comfort Zone

When we use a low-level language, we incur the cognitive load of assembling
micro-steps into something more meaningful (<span x="thinking"/>) When we use a
high-level language, we incur a similar load translating functions of functions
of functions (or meta-classes templated on object factories) into actual
operations on actual data.

More experienced programmers are more capable at both ends of the curve, but
that's not the only thing that changes.  <span f="comprehension-curves"/>
compares a <span i="code comprehension; novice!code
comprehension">novice</span>'s comprehension curve with an <span i="expert!code
comprehension">expert</span>'s.  Experts don't just understand more at all
levels of abstraction; their *preferred* level has also shifted so that
$$\sqrt{x^2 | y^2}$$ is actually more readable than the medieval expression "the
side of the square whose area is the sum of the areas of the two squares whose
sides are given by the first part and the second part".

{% include figure
   id="comprehension-curves"
   img="comprehension-curves.svg"
   alt="Comprehension curves"
   cap="How the relationship between abstraction and comprehension differs for novices and experts." %}

This difference implies that the software that is quickest for a novice to
comprehend will almost certainly be different from the software that an expert
can understand most quickly, which is why design rules like <span g="dry"
i="Don't Repeat Yourself">Don't Repeat Yourself</span> should be followed by the
word "however".  Duplicating some code so that it's right in front of the reader
may help people at one level of development, even if it makes long-term
maintenance more difficult for people at another level.  In the end, the only
correct answer to the question, "What's the best way to design this?" is, "For
whom?"
