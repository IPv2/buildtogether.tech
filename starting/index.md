---
---

Now that the most important stuff is out of the way, let's take a closer look at
what you're actually supposed to be doing.  On one side are homework
assignments, which typically include a handful of problems related to
recently-taught material that you are meant to solve in a week or two.  On the
other side are industrial <span i="internship">internships</span> or <span
i="co-op">co-op</span> terms in which you work full- or part-time for a company,
drawing a salary and suffering through quarterly PowerPoint presentations on
corporate strategy.  Lectures and exams usually aren't a part of these, though
if you're lucky (or if the company you're working for knows what it's doing)
you'll be paired with a mentor who will teach you some of the things in these
notes.

In between are courses with names like "Introduction to Software Engineering",
"Senior Thesis Project", or "Computer Science Capstone".  For the purposes of
this guide, these have <span i="project course!characteristics of">three
characteristics</span>.  First, learning how to work in a team is a goal of the
course.  This distinguishes these courses from (for example) upper-level courses
in operating systems or computer graphics, in which you're working in a team but
not being taught explicitly how to do so.

Second, your grade depends primarily on the software you build.  You may also
be required to write reports and sit an exam, but these are based on the
practical work---if you don't actually build some software, you can't pass the
course.

Finally, you are supposed to work as if you were trying to meet the needs of a
real customer.  You might start with a blank sheet of paper or have to fix and
extend an existing application; either way, you and your team are responsible
for some or all of requirements analysis, design, implementation, testing,
documentation, packaging, deployment, handoff, and review.

## Why Projects?

Project courses exist for several reasons:

To teach you things that can only be learned by doing.
:   If you pursue a career in industry, or if you go stay in academia and do
    anything other than pure theory, you will need to know how to build things.
    This is a craft, not a science: you can't learn how by listening to lectures
    any more than you can learn to ride a bike by watching the Tour de France on
    TV.

To tie everything you've learned together,
:   i.e., to demonstrate that the trees and pointers and joins and semaphores
    you've been wrestling with for the last two or three years are actually good
    for something.

Because they're fun.
:   At least, if they're done right.

One goal of project courses is to move learners from the left side of <span
f="four-models-of-instruction"/> to the right. Most of the learning will
take place in a team or on your own; the instructor's job is to mentor rather
than to lecture. Using the terms of <span x="thinking"/>, a project course
is where your school starts treating you like a competent practitioner rather
than like a novice.

{% include figure
   img="four-models-of-instruction.svg"
   id="four-models-of-instruction"
   alt="Four models of instruction"
   cap="Four models of instruction that shift control from instructors to learners." %}

There are as many ways to run a project course as there are instructors teaching
them <cite>Fincher2001</cite>.  The most important variable is whether your team
has a real customer or not.  Finding and interviewing people who actually want
software built and then meeting their needs is tremendously rewarding.  However,
it's also a lot of work and puts an extra burden on the instructor as well.  For
this reason, most team projects tend to be made up by instructors.

A third option is to use an open source project as a starting point.  Whether
it's an audio editor, a tool for displaying family trees, or control software
for the latest generation of electronic toys, the odds are pretty good that
there are bugs to fix and features to add.  Working on a project like this is
easier than finding a local company that wants its web site rejigged.  It's also
an opportunity for you to meet other developers who can mentor you, and create
something you can show off in a job interview.

## Grades

Many organizations make the mistake of focusing on outputs rather than on
outcomes <cite>Perri2018</cite>. In software companies, this usually takes the
form of measuring progress by the number of features added to a product rather
than by whether changes to the product are actually making people's lives
easier. Claims like "80% of people only use 20% of a product's features" are
largely anecdotal, but are probably also true: in most cases, people learn just
enough to accomplish the task at hand and only discover more intermittently and
accidentally if at all.

The equivalent mistake in a project course is to measure progress by the amount
of code you are writing rather than by how your work compares to the grading
scheme. Doing this doesn't mean you should only do things that are going to show
up on your transcript, but if you're going to, you should do so knowingly.

The first step in any project is therefore to figure out where the goalposts
are, so you know which way to kick the ball.  If you're an academic, this means
finding something that is interesting and challenging enough to be publishable,
but not intractable.  In a startup, it means figuring out what you can build
that people will pay for.  If you're working for someone else, your boss should
tell you what you're responsible for and the <span g="hr">HR department</span>
should tell you what the criteria are for performance evaluation and bonuses.
Again, you don't have to do only those things, but if you're going to drop any
or put time elsewhere, you should do it with your eyes open.

Your grade in a project course is typically based on:

The software you produce.
:   Does it build and run? Does it meet the customer's requirements (or the
    instructor's specifications if you don't have a real customer)?  Is the
    source code readable?  Is the program efficient?  (Using an exponential
    algorithm instead of one that runs in linear time certainly *ought* to cost
    you marks…)

The process you followed.
:   Some instructors insist you use a traditional analyze-design-code-test
    methodology.  Others structure the course around short sprints (typically a
    couple of weeks long) during which you refactor the application, extend it,
    test your changes, and deploy the new version.  Since instructors can't
    watch over your shoulder while you're working, they can't actually grade you
    on whether or not you follow a prescribed process.  The best they can do is
    grade you on the artifacts that process is supposed to produce (discussed
    below).  Since these can always be created after the fact, it's very
    tempting to just put your head down and code.  Resist---any process is
    better than chaos, and sticking to what the instructor asked for will at
    least save arguments within the team.

A final report.
:   This may be a handoff report (i.e., documentation to help whoever inherits
    the software from you get up to speed), a summary of your experiences, or
    some combination.

A final exam.
:   This may focus on the theoretical side of the course ("Describe the four
    main functions of Quality Assurance…")  but smart instructors will include
    some questions to test your understanding of the project in order to
    determine who actually did the work and who was just along for the ride.

Just like real development projects, course projects can and should produce a
lot more than just code.  For example, <cite>Spinellis2007</cite> looked at how
much content of different kinds went into the FreeBSD project in 2006.  <span
t="starting-spinellis-stats"/> doesn't divide "source code" into
"application code" and "tests", but it's still an eye-opener.

{% include table id="starting-spinellis-stats" file="spinellis-stats.tbl" cap="FreeBSD 2006" %}

Here are some of the things that you might be required to produce:

Requirements analysis
:   What the problem is, who the stakeholders are (i.e., who wants the problem
    solved), and what their needs are.

Design
:   What the user interface should look like, how data will flow through the
    system, what its major modules will be, and how they'll interact.

Application code
:   The software that will be delivered to the end user.  This is inextricably
    entangled with:

Test code
:   Coding and testing should not be separate activities: doing them
    concurrently greatly improves your project's chances of success.

Documentation
:   Human-readable explanations of the software's structure and use.  The first
    is intended for whoever inherits the software from you; the second, for its
    users.  It is almost always a mistake to try to combine the two or to write
    them as if they were going to be read by the same people.

Packaging
:   A program is a piece of software that runs for you on your machine.  A
    product is a piece of software that will run for anyone on *their* machine.
    Products take longer to build than programs: the packaging needed to let
    someone else download, install, configure, and run the program has often not
    been covered in software engineering courses, but good instructors will
    insist that you create it.

Deployment
:   These days the project's aim might not be to create something that can be
    downloaded and installed.  Instead, its aim might be to create a web site or
    web service or make something else directly available to users.  Like
    packaging, deployment can be a major development issue in its own right, and
    the effort required to do it is almost always underestimated.

Handoff
:   If you don't put effort into passing the project on to whoever comes after
    you, your hard work will almost certainly count for nought.  While it isn't
    usual for undergraduate projects to be handed on from one term to another,
    some courses require teams to swap code mid-term.  If this happens,
    instructors may grade you on how complete and up-to-date your wiki pages,
    bug database, and build scripts are at the time of handoff.

Review
:   The only way to get better at something is to reflect on how you've done and
    what you could have done better.  Every project should therefore end with a
    post mortem in which team members talk about what went right and what went
    wrong.  As mentioned earlier, this may then be the subject of the final
    report.

So much for generalities; the list below shows the grading scheme I've typically
used in project courses.

Warmup exercise (10%)
:   The warmup exercise is two weeks long; its purpose is to give students a
    chance to familiarize themselves with the problem domain, tools, and
    software they'll be using for the rest of the term.

Analysis and estimation (10%)
:   Two weeks spent figuring out what your customers actually want, what
    features will satisfy their needs, etc.

Code (10%)
:   Yes, that's right: the code is only worth 10% of the final grade, even
    though it's where students spend the bulk of their time.  I do this because
    (1) if you don't know how to program you shouldn't be in this course and (2)
    if you don't create some code you can't test, do a demo, or write your final
    report.

Testing (10%)
:   Testing is just as important as coding, so it's given the same weight.
    Note, though, that only automated tests count: if I can't check the project
    out of version control and re-run the tests (possibly after editing a
    configuration file) then as far as I'm concerned, the code hasn't been
    tested.  And it's no good saying, "But I can't write unit tests for my GUI"
    because it's simply not true: you can always test the core functionality,
    and if you design your program the right way you can test a lot more of your
    front end than you might think (<span x="testing"/>).

Demos (10%)
:   I used to require students to prepare a 20-minute lecture on a topic of
    their choosing and deliver it to their coursemates or a junior class.  It
    was a valuable experience, but it ate up a lot of time, so I switched to
    having students do 10-minute demos instead.  I usually give students two
    shots at this: one after which their peers give them feedback, and a second
    that's actually graded.  This is valuable practice for job interviews and a
    good reality check on how much progress has actually been made.

Teamwork (10%)
:   Everyone starts with 10 out of 10; marks come off if you always do your work
    at the last moment, check in code that breaks the build, or are
    disrespectful.

Final report (20%)
:   This describes the architecture of the code as it was actually built (rather
    than as it was designed) and summarizes the post mortem so that the next
    team can avoid any pitfalls this team ran into.

Final state of project (20%)
:   Most of my projects carry forward from term to term and team to team, so I
    award one fifth of the overall mark based on the state each team leaves the
    project in.  Does everything build?  Have issues been filed for all known
    bug?  Does the wiki explain how to install the code, and do those
    instructions actually work?

This grading scheme is labor-intensive: I probably spend 4--6 hours reading and
grading each project in a term.  I've thought several times about using peer
grading to reduce my load and give students some experience of what life is like
on the other side of the red pen, but I've never been able to convince myself
that it would actually work.

## Elevator Pitch

Once you know where the goalposts are, the next thing is to get everyone to
agree on what you're supposed to accomplish.  The best way to do this is write
an <span g="elevator_pitch" i="elevator pitch">elevator pitch</span> like the
one shown below to figure out what problem you're trying to solve, who it
affects, and why your solution is a good one.

<blockquote markdown="1">

**The problem of**
developing software in a predictable and reliable manner
**affects**
the management of software projects.
Developers are not able to predict reliably how long it takes them to complete tasks
which makes it impossible to effectively plan a project.
**As a result,**
users and managers are never sure whether the produced software will meet its requirements,
how reliable the software will be,
or whether the software will be delivered on time.

**A successful solution would**
help developers become more aware of what they do,
how they spend their time,
and the kinds of defects they find in their work.
**For**
software development teams
**who**
need to better understand how and when defects are introduced into their products,
**our product**
gathers and reports performance metrics
**in order to**
help developers track and analyze personal software development metrics.
**Unlike**
not gathering data or trying to gather it manually,
**our approach**
helps users gather data unobtrusively
and provides objective feedback that allows them to improve both individual and team performance.

</blockquote>

Have everyone on the team fill in the template independently and then compare
the results.  If your team is like most I've worked with, you'll be surprised by
how varied the answers are.  Once you have done that, pick one and turn it into
a short paragraph that everyone is happy with like the one below:

<blockquote markdown="1">

Most programmers can't predict how long it will take them to do things because
they don't know how long previous tasks have taken.  Gathering data manually is
annoying enough that programmers won't do it, so we're building a tool that will
monitor what applications they use and how long they use them.  This feedback
will help them improve their working habits and allow them to give their
managers more accurate input for scheduling.

</blockquote>

You now have the first paragraph for your project's home page and the abstract
for your final report.

An alternative to writing an elevator pitch is to build the product's home page,
i.e., to make up the website for your software as if it already existed.  What
catchphrase would you put across the top to catch people's eyes?  What features
would you list on the back to make your software more appealing than its
competitors?  What would its system requirements be?  Its license?  Its price?
Once your team agrees on these things, you're ready to start designing and
coding.

## Project Structure

All right: you have some idea of what you're going to build. How should you
organize the project itself?

Every language has its own conventions for what files should go where in a
project, for the simple reason that they all need different files.  In a Jekyll
website like this one, for example, the layout is:

`_config.yml`
:   A configuration file with the author's name, a list of any plugins that the
    site needs to build, the rules for generating URLs for blog posts, and so
    on.

`_layouts`
:   A directory containing templates for pages.

`_includes/`
:   A directory containing any snippets shared between those templates.

`_site`
:   The directory containing the generated web pages. If the site doesn't need
    any special plugins, this directory doesn't have to be included in version
    control: GitHub will re-create it automatically. If the site does use
    plugins, on the other hand, the authors have to generated the HTML and
    commit it themselves.

If your project's goal is to build a package, on the other hand, you will have
to organize your files according to the packaging system's rules; <span
x="design"/> gives an example.  In all cases, learning what goes where is like
learning when to signal when driving a car: the rules may vary from place to
place, but everywhere *has* rules, and knowing them will help prevent you from
crashing.

## Standard Files

Regardless of language or packaging system, every project should have a <span
i="standard project files; project organization!standard files">handful of
standard files</span> in its root directory.  These may have UPPERCASE names
without an extension, or may be plain text (`.txt)` or Markdown (`.md`) files.

<span i="README file">`README`</span>
:   A brief overview of the project that often serves as its home page on
    GitHub.

<span i="CONTRIBUTING file">`CONTRIBUTING`</span>
:   How to contribute to the project. Should people file an issue when they have
    a question, email a list, or post something on chat, and if so, where?  What
    code formatting conventions does the project use?  Research shows that clear
    contribution guidelines increase the odds of people contributing (<span
    x="fairness"/>); in my experience, they also reduce friction between team
    members.

<span i="CONDUCT file">`CONDUCT`</span>
:   The project's Code of Conduct, i.e., how people are required to treat one
    another.  As we'll discuss below, "be polite" or "use your common sense"
    aren't enough.

<span i="LICENSE file">`LICENSE`</span>
:   Describes who can do what with the project materials.  We discuss various
    licenses below as well.

## Code of Conduct

In order to get the most out of a team, it must do more than allow people to
contribute: it has to be clear that the teams *wants* contributions.  Saying
"the door is open" is not enough, since many people have painful personal
experience of being less welcome than others.  A project must therefore
acknowledge that some people are treated unfairly in society and actively take
steps to remedy this.  Putting a <span i="Code of Conduct">Code of
Conduct</span> in place isn't just compassionate: it also makes the team more
diverse, which in turn makes it more productive <cite>Zhan2020</cite>:

-   It reassures people who have experienced harassment or unwelcoming behavior
    before that this project takes inclusion seriously.

-   It ensures that everyone knows what the rules are.  What you think is polite
    or common sense depends on where you are from; since many projects have
    participants from different backgrounds, making the rules explicit avoids
    angry arguments starting with, "But *I* thought that…"

-   It prevents people who misbehave from <span g="feigning_ignorance">feigning
    ignorance</span>, i.e., claiming after they say or do something offensive
    that they didn't realize it was out of bounds or that they were "just
    kidding". (See also <span g="schrodingers_asshole">Schrödinger's
    asshole</span>.)

Having a Code of Conduct is an empty gesture if you don't also have a way to
respond to violation.  <cite>Aurora2018</cite> describes how, and learning the
basics is a good first step toward becoming an <span i="ally">ally</span> (<span
x="fairness"/>).

<div class="callout" markdown="1">

### What they really mean

In the early 2010s a lot of open source developers resisted the adoption of
codes of conduct, saying that they were unnecessary or that that they infringed
freedom of speech.  What they usually meant (and what the few people still
arguing against them usually mean) is that thinking about how they have
benefited from past inequity makes them feel uncomfortable.  If having a Code of
Conduct makes them decide to go elsewhere, your project will be better off.

</div>
