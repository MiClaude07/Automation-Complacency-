HELP = """ 
Hello! This is a bot to assist you in CS285. Definitions of terms will be added the day of or at least by the next class. If you have any recommendations, DM @Michael.

__**Available Commands:**__
- **$def <term>**: provides definition for <term>. Case is insensitive (i.e any form of Automation Complancency is valid if spelled correctly)
    Example call: $def Automation Complacency

- **$day <number>**: provides information from this day including a summary, link to the slides, and words. 
    Example call: $day 1

- **$lastday**: provides info on the latest day.

- **$dictionary**: provides definitions for all terms.
    Example call: $dicitionary

- **$resource <resource>**: provides a link to helpful resources. List of resources can be obtained with `$resource all`
    Example call: $resource final
"""
TIMEOUT = 300

DICT = {
    "Term": "Definition",
    "Peer To Peer Economy": "Sellers can sell directly to buyers",
    "5 Ways Users Pay For Free": 
    """ 
    - Advertising 
    - Donations
    - Businesses provides some services as a marketing tool
    - Generosity
    - Many free sites collect information about our online activities and sell it to advertisers.
    """,
    "Turing Test": "An AI test in which if the computer convinces the human subject that the computer is human, the computer is said to `pass`",
    "Negative Feedback Loops": "Damaging self-referential outputs in programs, usually in “black-box” algorithms ",
    "Deontological":  "Step-by-Step [rule-based]", 
    "Utilitarianism": "Outcome-based [Outcome must be greatest good for greatest number of people]", 
    "Social Contract Theory": "People willingly submit to a common law in order to live in a civil society. → Obeying laws = ethical" ,
    "Negative Rights": "(liberties) The right to act without interference ",
    "Positive Rights": "(claim-rights): Any obligation of some people to provide certain things for others",
    "Cognitive Dissonance": "Mental stress generated by the co-existence of conflicting thoughts → usually minimized by self-justification, misrepresentation, hiding problems and inadequate response to reported problems",
    "Conflict of Interest": "Citations that have the potential to undermine the impartiality of a person because of the possibility of a clash between the person’s self-interest and professional interest or public interest",
    "Bystander Effect": "Phenomenon in which the probability of an individual providing help is inversely related to the number of people who witness the situation",
    "Diffusion of Responsibility": "In a large group of people, people may feel that individual responsibility to intervene is lessened because it is shared by all of the onlookers",
    "Streisand Effect": "The effort of people to hide, remove or downplay information results in increased attention to it",
    "Decision Fatigue": "A phenomenon in which the more decisions one makes the lower the quality of those decisions",
    "Confirmation Bias": "A phenomenon in which people are predisposed to seek and absorb information that is aligned with their original ideas",
    "Inertia Bias": "Status quo bias. The tendency to stay with an idea without updating or revising it despite evidence that doing so would be beneficial",
    "Automation Bias": "The tendency to trust automated systems (and even ignore contradictory correct information if it comes from a non-automated source)",
    "Automation Complacency": "Inaction due to automation bias, or abdication of a user's decision-making responsibility to a computer system",
    "Algorithmic Bias": "Unfair outcomes originating from values or processes that are programmed by or for creators of computer systems",
    "Creeping Normalcy": "Incremental change results in calm acceptance, whereas abrupt change with the same results causes outcry",
    "Ad Hominem": "Attacking your opponent's personal traits instead of the content of their argument",
    "Anecdotal Evidence": "Basing conclusions on personal experiences instead of empirical evidence",
    "Appeal To Emotion": "The manipulation of emotional responses instead of basing arguments on sound logic",
    "Argument From Authority": "Arguing that if an authority says something, its veracity is beyond doubt",
    "Balance Fallacy": "The presentation of an issue as being more balanced than the evidence supports. Ascribing equal value to both sides of an argument, regardless of evidence or merit",
    "False Dichotomy": "Views or choices are inaccurately limited to one of two options",
    "Post Hoc Ergo Propter Hoc": "Implying causal relationship when there is none. Equating causality with correlation",
    "Red Herring": "Focusing on a non-issue instead of the argument at hand",
    "Slippery Slope": "Negating arguments with unsubstantiated conjecture of consequences. Can be fallacious or valid",
    "Straw Man": "Presenting an altered version of the opponent’s argument so that it seems absurd, then disproving the weak argument",
    "Key Aspects of Privacy": """
    - Freedom from intrusion (being left alone)
    - Control of information about oneself
    - Freedom from surveillance (from being tracked, followed, watched)""",
    "Re-Identification": "(Identifying individuals based on small pieces of information from multiple sources) has become much easier due to the quantity of information and power of data search and analysis tools.",
    "Secondary Use": "The use of data beyond the primary reason for its collection",
    "Invisible Information Gathering": "Collection of personal information about a user without the user’s knowledge",
    "Data Mining": "Searching and analyzing masses of data to find patterns and develop new information or knowledge",
    "Computer Profiling": "Analyzing data to see which people are likely to engage in a certain behavior",
    "Informed Consent": """Permission granted in full knowledge of possible consequences
    - Opt out: Person must request (usually by checking a box) that an organization not use information
    - Opt in: The collector of the information may use information only ig person explicitly permits use (usually by checking a box)""",
    "Fair Information Principles": """
    - Inform people when you collect information
    - Collect only the data needed
    - Offer a way for people to opt out
    - Keep data only as long as needed
    - Maintain accuracy of data
    - Protect security of data
    - Develop policies for responding to law enforcement requests for data""",
    "The 4th Amendment": "Grants citizens general privacy from the government by requiring warrants for searches",
    "The Privacy Act": "Limits disclosure of records held by agencies of the federal government to other agencies, organizations, and individuals",
    "Olmstead V. United States": "(1928) Supreme Court allowed the use of wiretaps on telephone lines without a court order. Interpreted the Fourth Amendment to apply only to physical intrusion and only the search or seizure of material things, not conversations",
    "Katz V. United States": "(1967) Supreme Court revised its position and ruled that the Fourth Amendment does apply to conversations. The Court said that the Fourth Amendment protects people, not places. To intrude in a place where a reasonable person has a reasonable expectation of privacy requires a court order",
    "Kyllo V. United States": "(2001) Court stated that where “the government uses a device that is not in General Public Use, the surveillance is a search and warrant must be obtained",
    "General Public Use" : "Devices that the general public has access too",
    "Gdpr": "(General Data Protection Regulation) Harmonize data rules across EU and for EU customers. American companies with EU users also must abide. Fair info principles become regulations. Data protection officers must be appointed. Explicit consent required for data profiling",
    "Omnibus Crime Control And Safe Streets Act": "(1968) prohibits Government agencies from wiretapping",
    "Ecpa": "(Electronic Communications Act) (1986) extended the 1968 wiretapping laws to include electronic communications",
    "Calea": "(Communications Assistance For Law Enforcement Act) (1994) Amended ECPA→ requires telecom equipment be designed to ensure that the government can intercept telephone calls (with a court order or other authorization). Has been upheld in several lawsuits",
    "Nsa": """(National Security Agency) 
	    - 1952: Formed to intercept and decode WW2 messages, only allowed to spy on foreign entities
	    - Patriot Act (2001) → US now included in NSA surveillance. Main surveillance provisions expired: June 1, 2015
	    - USA Freedom Act: Extends most of the Patriot Act Until 2018. Ended bulk data collection by the government , now it’s up to ISPs and telecom companies to collect data. Government agencies once again need warrants in order to request access to the records from the telecom companies. International calls and emails not included though can still be collected""",
    "Fisa": "(Foreign Intelligence Surveillance Act) Established oversight court for the NSA",
    "Section 702": "Explicitly allowed, but placed more limits on, government spying. Extends whistleblower protections. Incidental surveillance of US citizens is allowed in the scope of non-US investigations",
    "Rule 41": "Set procedural guidelines for courts. The DOJ wants to update Rule 41 with extensive surveillance for law enforcement",
    "The 1st Amendment":"(Freedom of Speech) Citizens may say almost anything they choose to without being punished by the government. Restriction on the power of government, not individuals or private businesses, to react to inflammatory speech",
    "Fcc": "(Federal Communications Commission) Federal commission that regulates interstate and international communications by radio, television, wire, satellite and cable in all 50 states, the District of Columbia and U.S. territories. An independent U.S. government agency overseen by Congress, the commission is the United States’ primary authority for communications law, regulation and technological innovation",
    "Telecommunications Act": """(1996) 
        - Part 1: ISPS are to be classified as either Information Services or Common Carriers
        - Part 2: Establishes legal immunity for people and companies who host online content, regardless of what their users post""",
    "Chilling Effect": "Discouragement and/or suppression of legal behavior (including speech)",
    "Cda": "(Communications Decency Act of 1996): First major internet censorship law. Made it a crime to make available to anyone under 18 any obscene or indecent communication. Found to be unconstitutional",
    "Cipa": "(Children’s Internet Protection Act of 2000) Requires schools and libraries that participate in certain federal programs to install filtering software. Upheld in court",
    "3 Things To Consider Before Leaking": """ 
        - Type of Material
        - Value to society
        - Risks to society and individuals""",
    "Berne Convention": "(1886) Signatory countries agree to enforce copyright violations across borders. (Adopted in US in 1988)",
    "Exclusive Rights Given To Copyright Holders": """
        - To make copies
        - To produce derivative works
        - To distribute copies
        - To perform the work in public
        - To display work in public
    """,
    "Lamacchia Loophole": "Lamacchia didn’t financially benefit from copying/distributing material, so copyright laws at the time didn’t apply",
    "No Electronic Theft Act": "(1997) made it a felony to willfully infringe copyright by reproducing or distributing one or more copies of copyrighted work with a total value of more than $1,000 within a 6 month period. Closed LaMacchia Loophole",
    "Fair Use Doctrine": """
    Purpose and nature of use
        - Nature of the copyrighted work
        - Amount and significance of portion used
        - Effect of use on potential market or value of the copyrighted work
    """,
    "Sony V. Universal City Studios": "(1984 ‘The Betamax Case’) Supreme Court decided that the makers of a device with legitimate uses should not be penalized because some people may use it to infringe on copyright. Copying movies for later viewing was fair use",
    "Drm": "(Digital Rights Management) Collection of techniques that control uses of intellectual property in digital formats. Includes hardware and software schemes using encryption. The procedure of a file has flexibility to specify what a user may do with it.",
    "Dmca": "(The Digital Millennium Copyright Act of 1998) Anti Circumvention of DRM. Safe harbor protects web sites from lawsuits for copyright infringement by users of sites. Extended Telecommunications Act protections with the condition that providers abide by take down notices",
    "Riaa V. Napster": "Court ruled napster liable because they had the right and ability to supervise the system, including copyright infringing activities",
    "Look And Feel": "Refers to interface features. Generally not protected by copyright. Method of operation, not design."
}


DAY = {
    "10": 
    """
    Summary:  Weekly Write Up 2 due Sunday October 8th. In the Lecture, we looked over the Betamax Case (Sony v. Universal) and the concept of legitimate use. Due to issues of controlling copyright over the internet and legitimate use, Digital Rights Managements are a set of strategies for product developers to protect digital intellectual properties. DMCA is a law that protects DRMs. DMCA also protects websites that host copyright infringing content, but they must abide takedown requests. We looked over the RIAA V. Napster Case which analyzed the expectations of web sites to monitor for copyright infringement. Towards the end, we covered the concepts of copyleft and patents. 

    Slides: https://liveumb-my.sharepoint.com/:p:/g/personal/amanda_potasznik_umb_edu/ETbZY0UxoD9Cv7vRb9UYdq0By7xB7nyVe7U66QmmoYugbg?e=91UOE5

    Terms: 
        Sony V. Universal City Studuis
        DRM
        DMCA
        RIAA V. Napster
        Look And Feel
    """,
    "9": 
    """
    Summary: We covered copyright laws and ethics, Intellectual Properties, Fair Use.

    Slides: https://bpb-us-w2.wpmucdn.com/blogs.umb.edu/dist/7/3673/files/2022/11/Day-9.pdf

    Terms: 
        Berne Convention
        Exclusive Rights Given To Copyright Holders
        LaMacchia Loophole
        No Electronic Theft Act
        Fair Use Doctrine
    """,
    "8": 
    """
    Summary: Anonymity. Government involvement when it comes to censorship and anonymity online. 

    Slides: https://bpb-us-w2.wpmucdn.com/blogs.umb.edu/dist/7/3673/files/2022/11/Day-8.pdf

    Terms: None
    """,
    "7": 
    """
    Summary: Project sign ups. Leaking info, the releasing of information to an untrusted environment. We covered the ethics of leaking. Whistleblower protection laws. Espionage Act. Chelsey Manning. Edward Snowden.

    Slides: https://liveumb-my.sharepoint.com/:p:/g/personal/amanda_potasznik_umb_edu/Eepg4T9FkoNHkq_wJE80Ok8B6YLXAKbSXb7wJo7Ac-vDZw?e=simmny

    Terms: 3 Things To Consider Before Leaking
    """,
    "6": 
    """
    Summary: We covered the first amendment and different caveats. Then, we looked at the FCC and how they manage communications. Next, we looked at the Telecommunications Act of 1996 and how ISPs are structured. The ISPs structure is connected to the politics of Net Neutrality. Exceptions to section 230. Then, we looked at Federal Child Protection, Pornography, and Censorship. We also looked at laws surrounding Non-consensual pornography. We also looked at Free Speech in relation to Spam.

    Slides: https://bpb-us-w2.wpmucdn.com/blogs.umb.edu/dist/7/3673/files/2023/05/Day-6.pdf 

    Terms: 
        The 1st Amendment
        FCC
        Telecommincations Act
        Chilling Effect
        CDA
        CIPA
        CAN-SPAM Act
    """,
    "5": 
    """
    Summary:  Weekly Write-Up → First one will take longer to grade, be more lenient, and have more comments. Next week is Project Group sign up!

    Slides: https://bpb-us-w2.wpmucdn.com/blogs.umb.edu/dist/7/3673/files/2023/03/Day-5.pdf

    Terms:
        GDPR
        Omnibus Crime Control And Safe Streets Atct
        ECPA
        CALEA
        NSA
        FISA
        Section 702
        Rule 41
    """,
    "4": 
    """
    Summary: Covered key aspects of privacy. Privacy violation. HIPPA. Government and privacy.

    Slides: https://bpb-us-w2.wpmucdn.com/blogs.umb.edu/dist/7/3673/files/2022/11/Day-4.pdf 

    Terms: 
        Key Aspects of Privacy
        Re-Indentification
        Secondary Use
        Invisible Information Gathering
        Data Mining
        Computer Profiling
        Informed Consent
        Fair Information Principles
        The 4th Amendement
        The Privacy Act
        Olmstead V. United States
        Katz V. United States
        Kyllo V. United States
        General Public Use
    """,
    "3": 
    """
    Summary:
    We covered mainly psychological and sociological terms as well as Logical Fallacies. 

    Slides: https://bpb-us-w2.wpmucdn.com/blogs.umb.edu/dist/7/3673/files/2023/06/Day-3.pdf

    Terms: 
        Cognitive Dissonance
        Conflict of Interest
        Bystander Effect
        Diffusion of Responsibility
        Streisand Effect
        Decision Fatigue
        Confirmation Bias
        Inertia Bias
        Automation Bias
        Automation Complancecy
        Algorithmic Bias
        Creeping Normalcy
        Ad Hominem
        Anecdotal Evidence
        Appeal To Emotion 
        Argument From Authority
        Balance Fallacy
        False Dichotomy
        Post Hoc Ego Propter Hoc
        Red Herring
        Slippery Slope
        Straw Man
    """,
    "2": 
    """
    Summary: 
        Today we went over the concept of Lag Time which is the idea that technological developments occur faster 
        than legislation's and education's ability to catch up. 

        We also covered Black-Box algorithms and how negative feedback loops are made. 

        Deontological and Utilitarian ethics were introduced and we went over a few examples in class.

        We looked at Thomas Hobbe's Social Contract Theory and compared it to Roussaeu's theory.

        Finally, we took a look at examples of positive and negative rights.

    Slides: https://blogs.umb.edu/amandapotasznik/files/2022/11/Day-2.pdf

    Terms:
       Negative Feedback Loops
       Deontological
       Utilitarianism
       Social Contract Theory
       Negative Rights
       Positve Rights
    """,
    "1": 
    f"""
    Summary: On this day, we covered the Syllabus, Website, and some introductions.
    
    Some important notes: 
        Midterm is 10/19
        Final paper is due 12/15
        Presentations will be done after Midterms. Group sign ups will be on **September 26th**. 
        __**Citation Workshop and BOS are due by the end of the weekend at 11:59 Sunday**__

    The Lecture covered Pace of Change, Moore's Law, the pros and cons of rapidly evolving technology, the growth of 
    E-Commerce, and how "Free" Stuff are paid for.

    Slides: https://bpb-us-w2.wpmucdn.com/blogs.umb.edu/dist/7/3673/files/2022/11/Day-1.pdf

    Terms: 
        Peer To Peer Economy
        5 Ways Users Pay For Free
        Turing Test
    """,
    "0": 
    """
    Summary: Basic Summary of the Day and concepts
    Slides: Link to the slides
    Terms: Terms used today
    """
}


RESOURCES = {
    "Website": "https://blogs.umb.edu/amandapotasznik/",
    "Homework": "https://blogs.umb.edu/amandapotasznik/assignments/homework/homework-questions/",
    "Ww": "https://blogs.umb.edu/amandapotasznik/assignments/how-to-write-a-weekly-write-up/",
    "Articles": "https://www.pinterest.com/AP285UMB/ethics-umb/",
    "Ww Examples": "https://blogs.umb.edu/amandapotasznik/assignments/how-to-write-a-weekly-write-up/weekly-write-up-examples/",
    "Ww Common Mistakes": "https://blogs.umb.edu/amandapotasznik/assignments/how-to-write-a-weekly-write-up/common-writing-mistakes-and-how-to-fix-them/",
    "Midterm": "https://blogs.umb.edu/amandapotasznik/assignments/midterm-study-guide/",
    "Presentation": "https://blogs.umb.edu/amandapotasznik/assignments/project-details-and-advice/",
    "Final": "https://blogs.umb.edu/amandapotasznik/assignments/allterms/",
    "Final Example": """ 
    Article Versions: 
        https://blogs.umb.edu/amandapotasznik/files/2020/11/Successful-Student-Article-Final-1.pdf
        https://blogs.umb.edu/amandapotasznik/files/2023/01/Fall22-Article-Final-Example.pdf
    Scenario Version:
        https://blogs.umb.edu/amandapotasznik/files/2020/11/MBTA-final.pdf
    """,
    "Slides": "https://blogs.umb.edu/amandapotasznik/class-slides/",
    "Calender": "https://blogs.umb.edu/amandapotasznik/general-info/class-calendar/",
    "Late": "https://blogs.umb.edu/amandapotasznik/general-info/late-to-class/",
    "Syllabus": "https://blogs.umb.edu/amandapotasznik/general-info/syllabus/",
    "Rubric": "https://blogs.umb.edu/amandapotasznik/rubrics/",
    "Wpe": "https://blogs.umb.edu/amandapotasznik/department-campus-fyi/wpe/"
}

RESOURCE_DEF = {
    "**Website**": "Potasznik's Website",
    "**Homework**": "Homework Questions",
    "**Ww**": "Weekly Write-Up guidelines",
    "**Articles**": "pintrest board of good articles to use for Weekly Write-Ups",
    "**Ww Examples**": "Weekly Wrtite-Up examples",
    "**Ww Common Mistakes**": "Common Mistakes that are encountered in Weekly Write-Ups",
    "**Midterm**": "Midterm information and study guide",
    "**Presentation**": "Presentation information and guide",
    "**Final**": "Final paper information",
    "**Final Example**": "Examples for both versions of the final paper",
    "**Slides**": "Class slides",
    "**Calender**": "Class calender",
    "**Late**": "Information on what to do when you are late to class",
    "**Syllabus**": "Syllabus",
    "**Rubric**": "Rubrics",
    "**Wpe**": "Information on the WPE"
}