---
---

Back in 2016 [I tweeted][excel-tweet], "If anyone has data showing <span
i="Excel">Excel</span> is *more* error-prone than <span
i="MATLAB">MATLAB</span>/<span i="Python">Python</span>/<span i="R (programming
language)">R</span> once you normalize for hours spent learning it, please
post."  It was clear from the responses and from other discussion online that
most programmers believe this, but I'm not really sure what "this" is:

There are more errors in published results created with Excel than in results created with scripting languages like MATLAB, Python, and R.
:   Given that many more people use Excel, that's like saying that people in
    China have more heart attacks than people in Luxembourg.

Results calculated with Excel are more likely to be wrong than results calculated with scripting languages.
:   This is what I had in mind when I tweeted, and I don't think the answer is
    obvious.  Yes, there are lots of examples of people botching spreadsheets,
    but there's also a lot of buggy code out there.  (<span i="Flon's
    Axiom">Flon's Axiom</span> states, "There is not now, nor has there ever
    been, nor will there ever be, any programming language in which it is the
    least bit difficult to write bad code.")
    <br/>
    And even if this claim is true, correlation isn't causation.  I think that
    people who do statistics programmatically have probably invested more time
    in mastering their tools than people who use spreadsheets.  Any differences
    in error rates could easily be due to differences in time spent in
    reflective practice.

People who are equally proficient in Excel and scripting languages are more likely to make mistakes in Excel.
:   This formulation corrects the flaw identified above, but is nonsensical,
    since the only meaningful definition of "equally proficient" is "use equally
    well".

Spreadsheets are intrinsically more error-prone than scripting languages
:   I have heard people claim that spreadsheets don't show errors as clearly,
    they're harder to test, it's harder to figure out what calculations are
    actually being done, or they themselves are buggier than scripting
    languages' math libraries.  These are all plausible, but may all be red
    herrings.  Yes, it's hard to write unit tests for spreadsheets, but it's
    possible: <cite>Hermans2016</cite> found that 8% of spreadsheets included
    tests like `if(A1<>5, "ERROR", "OK")`.  I'd be surprised if more than 8% of
    people who do statistics in Python or R regularly write unit tests for their
    scripts, so the fact that they *could* is irrelevant.

To be clear, I'm not defending or recommending spreadsheets.  But if programming
really is a better way to do crunch numbers, we ought to be able to use science
to prove it.  And to do that, we have to know what methods we have at our
disposal and what they're good for.

## Controlled Experiments

The first method that empirical research uses is <span i="controlled
experiments">controlled experiments</span>: subjects are given a task and some
aspect of their performance is measured.  Subjects are typically divided into a
<span g="control_group" i="control group">control group</span> (who do things as
normal) and a <span g="treatment_group" i="treatment group">treatment
group</span> (who do things in an alternative way). If the difference between
the groups is large enough statistically, the experimenter can say that the
treatment probably has an effect on outcomes.

There are several traps in this for the unwary <cite>DeOliveiraNeto2019</cite>:

<span i="experimenter bias">Experimenter bias</span>.
:   People have many biases, both conscious and unconscious.  In order to make
    sure that these don't inadvertently affect the results, subjects should be
    assigned to groups at random. Going even further, experiments in medicine
    are often <span g="double_blind" i="double blind experiments">double
    blind</span>: neither the subject nor the person administering the treatment
    knows which subjects are getting the new heart medication and which are
    getting a <span g="placebo" i="placebo">placebo</span>. It's usually not
    possible to achieve this when doing software engineering experiments.

<span i="significance hacking">Significance hacking</span>.
:   If you measure enough things and look for enough correlations, you will
    almost certainly find *something* that passes a test for statistical
    significance. For example, there is a strong correlation between the number
    of letters in winning words in spelling competitions and the number of
    people killed by venomous spiders <cite>Vigen2015</cite>. To guard against
    this, researchers should <span g="pre_registration" i="pre-registration of
    experiments">pre-register</span> their analyses, i.e., say in advance what
    they're going to compare against what, and then use various statistical
    techniques that require a higher standard of proof when they are checking
    more possible combinations.

<span i="negative results (failure to publish)">Failure to publish negative results</span>.
:   An experiment isn't a failure if it doesn't find something that is
    statistically significant: ruling something out is just as useful as finding
    something new. However, negative results are not as exciting (and not as
    beneficial to a researcher's career), so they often go unreported.

Getting a few undergraduates in a lab for an hour each is easy; getting
professional programmers to do something new or different for several months is
not, but this doesn't mean that controlled experiments have to be expensive.  If
you have an idea you want to test, gather a little data and use that to evaluate
the plausibility of your idea. If you need to be really confident, build up the
evidence base over time in multiple experiments, increasing the sample size and
improving the methodology each time to get a stronger answer for a more specific
question.

Researchers often rely on <span g="quasi_experiment"
i="quasi-experiment">quasi-experiments</span> when doing this, i.e., they look
at pre-existing groups like programmers who have decided for themselves to use a
new IDE against ones who have not. Quasi-experiments are cheaper and easier to
set up, but researchers must be careful to account for <span
g="confounding_variables" i="confounding variable">confounding
variables</span>. For example, are programmers who choose to use an IDE younger
and therefore less experienced than ones who use legacy text editors? If so, how
does that difference skew the results?

## Data Mining

Quasi-experiments blend into the second major research approach, which uses
statistics and machine learning to find patterns in whatever data the researcher
can get her hands on. Doing this is called <span g="data_mining" i="data
mining">data mining</span>, and most studies of this kind make use of the wealth
of information available online at sites like [GitHub]][github] and [Stack
Overflow][stack-overflow] or from millions of crash reports collected online
<cite>Glerum2009</cite>.  Data mining has produced many valuable insights, but
has challenges of its own.  The largest of these is that people who work in the
open aren't typical, so any results we get from studying them must be
interpreted cautiously.

One problem with data mining is that once again, correlation doesn't imply
causation.  Another is that we usually don't know whether the data we have
access to is representative.  In 2012, Scott Hanselman coined the term <span
g="dark_matter_developer" i="dark matter developer">dark matter
developers</span> to describe programmers who don't blog, don't answer questions
in online forums, don't have their work in public repositories, and so on. Just
as dark matter makes up most of the universe, dark matter developers make up
most of our industry, and just as the matter we can see is vanishingly atypical,
so too are developers who radiate information.

One reason for this is that the web ranges from unwelcoming to actively hostile
for people from under-represented groups <cite>Ford2016,May2019</cite>.
Unfortunately, in-person workplaces are often no better: many are filled with
small signs that make many people feel out of place <cite>Cheryan2009</cite>.
<span x="fairness"/> takes a closer look at these issues.

<div class="callout" markdown="1">

### A cautionary tale

<cite>Zeller2011</cite> did what too many researchers in too many fields do on a
regular basis: throw some data at some machine learning algorithms and then
claim that whatever comes out the other end is significant. Luckily for us, they
did it on purpose to make a point.

They took data on code and errors for the Eclipse IDE and correlated the two to
find good predictors of bugs. Which sounds sensible---except they did the
correlation at the level of individual characters. It turns out that 'i', 'r',
'o', and 'p' are most strongly correlated with errors. What is a sensible
researcher to do facing these findings? Take those letters out of the keyboard,
of course.  The authors then go over everything that's wrong with their
approach, from lack of theoretical grounding to dishonest use of
statistics. Before you read too much research, make sure to read this.

</div>

## Qualitative Methods

The third set of approaches are called <span g="qualitative_method"
i="qualitative methods">qualitative methods</span>, and involve close analysis
of a small number of cases to tease out common patterns.  Articles like
<cite>Sharp2016</cite> do an excellent job of explaining how these methods work
and what their strengths and limitations are.

<div class="callout" markdown="1">

### Wish I knew then what I know now

My classes in engineering taught me to look down on anything that wasn't a
controlled laboratory experiment whose results could be neatly displayed in a
scatterplot or bar chart.  It wasn't until I was in my thirties that I accepted
that the "fuzzy" methods of the social sciences were just as rigorous when used
properly, and the only ones that could produce certain valuable insights.

</div>

<cite>Washburn2016</cite> demonstrates the kinds of insights these methods can
produce. They analyzed 155 post mortem reviews of game projects to identify
characteristics of game development, link the characteristics to positive and
negative experiences, and distill a set of best practices and pitfalls for game
development. Their description of their method is worth repeating in full:

<blockquote markdown="1">

Initially, we started with 12 categories of common aspects of development…  In
order to identify additional categories, we performed 3 iterations of analysis
and identification.  The first week, we each read and analyzed 3 postmortem
reviews each, classifying the items discussed in each section into the 12
predetermined categories of common aspects that impact development.  While
analyzing these reviews, we identified additional categories of items that went
right or wrong during development, and revisited the reviews we had already
analyzed to update the categorization of items. For the next two weeks we
repeated this process of analyzing postmortems and identifying categories,
analyzing 10 postmortems each in week 2, and 15 postmortems each in week
3. After each iteration, we discussed the additional categories we identified,
and determined if they were viable.

After our initial iterations for identifying additional categories, we had
completed the analysis of 60 postmortem reviews.  We then stopped identifying
new categories, and began analyzing postmortems at a combined rate of about 40
postmortem reviews per week.  After each week we reviewed what we had done to
ensure we both had the same understanding of each category.  This continued
until we had analyzed all the postmortem reviews.

</blockquote>

## The Fourth Tradition

<blockquote markdown="1">

"Once the rockets are up, who cares where they come down?
<br/>
That's not my department!" says Wernher von Braun

--- <span i="Lehrer, Tom">Tom Lehrer</span>
</blockquote>

<cite>Tedre2008</cite> describes three traditions that have shaped how we think
about computing: the <span i="mathematical tradition in
computing">mathematical</span>, which focuses on algorithms and proofs; the
<span i="scientific tradition in computing">scientific</span>, which studies
programs and programmers empirically; and the <span i="engineering tradition in
computing">engineering tradition</span>, which centers the fact that computing
matters because we can actually build useful things.

That paper changed how I think about our field, but in the past few years I have
realized that <span i="humanist tradition in computing">another point of
view</span> is just as important, though not as well respected.  It draws on
humanities and social sciences to explore questions like, "Who does this help?",
"Who does this hurt?", and, "Who decides?"  Just as the most interesting
software engineering research these days is look at how the way we think
interacts with the way we program (<span x="research"/>), the most interesting
thinking about computing as a whole is coming from people who have outgrown the
"Wernher von Braun" mentality of Lehrer's song.
