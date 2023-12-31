HELP = """ 
Hello! This is a bot to assist you in CS285. Definitions of terms will be added the day of or at least by the next class. If you have any recommendations, DM @Michael.

__**Available Commands:**__
- **$def <term>**: provides definition for <term>. Case is insensitive (i.e any form of Automation Complancency is valid if spelled correctly)
    Example call: $def Automation Complacency

- **$day <number>**: provides information from this day including a summary, link to the slides, and words. 
    Example call: $day 1

- **$lastday**: provides info on the latest day.

- **$dictionary**: provides definitions for all terms. Typing **sort** after **$dictionary** will sort Terms alphabetically.
    Example call: $dicitionary

- **$resource <resource>**: provides a link to helpful resources. List of resources can be obtained with `$resource all`
    Example call: $resource final

- **$quiz**: Presents a quiz for the caller! Quiz yourself on class terms!
"""
TIMEOUT = 300

DICT = {
    "Peer To Peer Economy": {'def': 'Sellers can sell directly to buyers', 'day': '1'},
    "5 Ways Users Pay For Free": {'def': ' \n        1.) Advertising \n        2.) Donations\n        3.) Businesses provides some services as a marketing tool\n        4.) Generosity\n        5.) Many free sites collect information about our online activities and sell it to advertisers.\n    ', 'day': '1'},
    "Turing Test": {'def': 'An AI test in which if the computer convinces the human subject that the computer is human, the computer is said to pass', 'day': '1'},
    "Negative Feedback Loops": {'def': 'Damaging self-referential outputs in programs, usually in “black-box” algorithms ', 'day': '2'},
    "Deontological": {'def': 'Step-by-Step [rule-based]', 'day': '2'},
    "Utilitarianism": {'def': 'Outcome-based [Outcome must be greatest good for greatest number of people]', 'day': '2'},
    "Social Contract Theory": {'def': 'People willingly submit to a common law in order to live in a civil society. → Obeying laws = ethical', 'day': '2'},
    "Negative Rights": {'def': '(liberties) The right to act without interference ', 'day': '2'},
    "Positive Rights": {'def': '(claim-rights): Any obligation of some people to provide certain things for others', 'day': '2'},
    "Cognitive Dissonance": {'def': 'Mental stress generated by the co-existence of conflicting thoughts → usually minimized by self-justification, misrepresentation, hiding problems and inadequate response to reported problems', 'day': '3'},
    "Conflict Of Interest": {'def': 'Citations that have the potential to undermine the impartiality of a person because of the possibility of a clash between the person’s self-interest and professional interest or public interest', 'day': '3'},
    "Bystander Effect": {'def': 'Phenomenon in which the probability of an individual providing help is inversely related to the number of people who witness the situation', 'day': '3'},
    "Diffusion Of Responsibility": {'def': 'In a large group of people, people may feel that individual responsibility to intervene is lessened because it is shared by all of the onlookers', 'day': '3'},
    "Streisand Effect": {'def': 'The effort of people to hide, remove or downplay information results in increased attention to it', 'day': '3'},
    "Decision Fatigue": {'def': 'A phenomenon in which the more decisions one makes the lower the quality of those decisions', 'day': '3'},
    "Confirmation Bias": {'def': 'A phenomenon in which people are predisposed to seek and absorb information that is aligned with their original ideas', 'day': '3'},
    "Inertia Bias": {'def': 'Status quo bias. The tendency to stay with an idea without updating or revising it despite evidence that doing so would be beneficial', 'day': '3'},
    "Automation Bias": {'def': 'The tendency to trust automated systems (and even ignore contradictory correct information if it comes from a non-automated source)', 'day': '3'},
    "Automation Complacency": {'def': "Inaction due to automation bias, or abdication of a user's decision-making responsibility to a computer system", 'day': '0'},
    "Algorithmic Bias": {'def': 'Unfair outcomes originating from values or processes that are programmed by or for creators of computer systems', 'day': '3'},
    "Creeping Normalcy": {'def': 'Incremental change results in calm acceptance, whereas abrupt change with the same results causes outcry', 'day': '3'},
    "Ad Hominem": {'def': "Attacking your opponent's personal traits instead of the content of their argument", 'day': '3'},
    "Anecdotal Evidence": {'def': 'Basing conclusions on personal experiences instead of empirical evidence', 'day': '3'},
    "Appeal To Emotion": {'def': 'The manipulation of emotional responses instead of basing arguments on sound logic', 'day': '3'},
    "Argument From Authority": {'def': 'Arguing that if an authority says something, its veracity is beyond doubt', 'day': '3'},
    "Balance Fallacy": {'def': 'The presentation of an issue as being more balanced than the evidence supports. Ascribing equal value to both sides of an argument, regardless of evidence or merit', 'day': '3'},
    "False Dichotomy": {'def': 'Views or choices are inaccurately limited to one of two options', 'day': '3'},
    "Post Hoc Ergo Propter Hoc": {'def': 'Implying causal relationship when there is none. Equating causality with correlation', 'day': '3'},
    "Red Herring": {'def': 'Focusing on a non-issue instead of the argument at hand', 'day': '3'},
    "Slippery Slope": {'def': 'Negating arguments with unsubstantiated conjecture of consequences. Can be fallacious or valid', 'day': '3'},
    "Straw Man": {'def': 'Presenting an altered version of the opponent’s argument so that it seems absurd, then disproving the weak argument', 'day': '3'},
    "Key Aspects Of Privacy": {'def': '\n        1.) Freedom from intrusion (being left alone)\n        2.) Control of information about oneself\n        3.) Freedom from surveillance (from being tracked, followed, watched)', 'day': '4'},
    "Re-Identification": {'def': '(Identifying individuals based on small pieces of information from multiple sources) has become much easier due to the quantity of information and power of data search and analysis tools.', 'day': '4'},
    "Secondary Use": {'def': 'The use of data beyond the primary reason for its collection', 'day': '4'},
    "Invisible Information Gathering": {'def': 'Collection of personal information about a user without the user’s knowledge', 'day': '4'},
    "Data Mining": {'def': 'Searching and analyzing masses of data to find patterns and develop new information or knowledge', 'day': '4'},
    "Computer Profiling": {'def': 'Analyzing data to see which people are likely to engage in a certain behavior', 'day': '4'},
    "Informed Consent": {'def': 'Permission granted in full knowledge of possible consequences\n        1.) Opt out: Person must request (usually by checking a box) that an organization not use information\n        2.) Opt in: The collector of the information may use information only ig person explicitly permits use (usually by checking a box)', 'day': '4'},
    "Fair Information Principles": {'def': '\n        1.) Inform people when you collect information\n        2.) Collect only the data needed\n        3.) Offer a way for people to opt out\n        4.) Keep data only as long as needed\n        5.) Maintain accuracy of data\n        6.) Protect security of data\n        7.) Develop policies for responding to law enforcement requests for data', 'day': '4'},
    "The 4Th Amendment": {'def': 'Grants citizens general privacy from the government by requiring warrants for searches', 'day': '4'},
    "The Privacy Act": {'def': 'Limits disclosure of records held by agencies of the federal government to other agencies, organizations, and individuals', 'day': '4'},
    "Olmstead V. United States": {'def': '(1928) Supreme Court allowed the use of wiretaps on telephone lines without a court order. Interpreted the Fourth Amendment to apply only to physical intrusion and only the search or seizure of material things, not conversations', 'day': '4'},
    "Katz V. United States": {'def': '(1967) Supreme Court revised its position and ruled that the Fourth Amendment does apply to conversations. The Court said that the Fourth Amendment protects people, not places. To intrude in a place where a reasonable person has a reasonable expectation of privacy requires a court order', 'day': '4'},
    "Kyllo V. United States": {'def': '(2001) Court stated that where “the government uses a device that is not in General Public Use, the surveillance is a search and warrant must be obtained', 'day': '4'},
    "General Public Use": {'def': 'Devices that the general public has access too', 'day': '4'},
    "Gdpr": {'def': '(General Data Protection Regulation) Harmonize data rules across EU and for EU customers. American companies with EU users also must abide. Fair info principles become regulations. Data protection officers must be appointed. Explicit consent required for data profiling', 'day': '5'},
    "Omnibus Crime Control And Safe Streets Act": {'def': '(1968) prohibits Government agencies from wiretapping', 'day': '5'},
    "Ecpa": {'def': '(Electronic Communications Act) (1986) extended the 1968 wiretapping laws to include electronic communications', 'day': '5'},
    "Calea": {'def': '(Communications Assistance For Law Enforcement Act) (1994) Amended ECPA→ requires telecom equipment be designed to ensure that the government can intercept telephone calls (with a court order or other authorization). Has been upheld in several lawsuits', 'day': '5'},
    "Nsa": {'def': '(National Security Agency) \n\t    1.) 1952: Formed to intercept and decode WW2 messages, only allowed to spy on foreign entities\n\t    2.) Patriot Act (2001) → US now included in NSA surveillance. Main surveillance provisions expired: June 1, 2015\n\t    3.) USA Freedom Act: Extends most of the Patriot Act Until 2018. Ended bulk data collection by the government , now it’s up to ISPs and telecom companies to collect data. Government agencies once again need warrants in order to request access to the records from the telecom companies. International calls and emails not included though can still be collected', 'day': '5'},
    "Fisa": {'def': '(Foreign Intelligence Surveillance Act) Established oversight court for the NSA', 'day': '5'},
    "Section 702": {'def': 'Explicitly allowed, but placed more limits on, government spying. Extends whistleblower protections. Incidental surveillance of US citizens is allowed in the scope of non-US investigations', 'day': '5'},
    "Rule 41": {'def': 'Set procedural guidelines for courts. The DOJ wants to update Rule 41 with extensive surveillance for law enforcement', 'day': '5'},
    "The 1St Amendment": {'def': '(Freedom of Speech) Citizens may say almost anything they choose to without being punished by the government. Restriction on the power of government, not individuals or private businesses, to react to inflammatory speech', 'day': '6'},
    "Fcc": {'def': '(Federal Communications Commission) Federal commission that regulates interstate and international communications by radio, television, wire, satellite and cable in all 50 states, the District of Columbia and U.S. territories. An independent U.S. government agency overseen by Congress, the commission is the United States’ primary authority for communications law, regulation and technological innovation', 'day': '6'},
    "Telecommunications Act": {'def': '(1996) \n        1.) Part 1: ISPS are to be classified as either Information Services or Common Carriers\n        2.)  Part 2: Establishes legal immunity for people and companies who host online content, regardless of what their users post', 'day': '6'},
    "Chilling Effect": {'def': 'Discouragement and/or suppression of legal behavior (including speech)', 'day': '6'},
    "Cda": {'def': '(Communications Decency Act of 1996): First major internet censorship law. Made it a crime to make available to anyone under 18 any obscene or indecent communication. Found to be unconstitutional', 'day': '6'},
    "Cipa": {'def': '(Children’s Internet Protection Act of 2000) Requires schools and libraries that participate in certain federal programs to install filtering software. Upheld in court', 'day': '6'},
    "Can-Spam Act": {"def": "(Controlling the Assault of Non-Solicited Pornography and Marketing 2003) Sets rules for spam senders. Criticized for not banning all spam, legitimized commercial spam", "day": "6"},
    "3 Things To Consider Before Leaking": {'def': ' \n        1.) Type of Material\n        2.) Value to society\n        3.) Risks to society and individuals', 'day': '7'},
    "Berne Convention": {'def': '(1886) Signatory countries agree to enforce copyright violations across borders. (Adopted in US in 1988)', 'day': '9'},
    "Exclusive Rights Given To Copyright Holders": {'def': '\n        1.) To make copies\n        2.) To produce derivative works\n        3.) To distribute copies\n        4.) To perform the work in public\n        5.) To display work in public\n    ', 'day': '9'},
    "Lamacchia Loophole": {'def': 'Lamacchia didn’t financially benefit from copying/distributing material, so copyright laws at the time didn’t apply', 'day': '9'},
    "No Electronic Theft Act": {'def': '(1997) made it a felony to willfully infringe copyright by reproducing or distributing one or more copies of copyrighted work with a total value of more than $1,000 within a 6 month period. Closed LaMacchia Loophole', 'day': '9'},
    "Fair Use Doctrine": {'def': '\n    Purpose and nature of use\n        1.) Nature of the copyrighted work\n        2.) Amount and significance of portion used\n        3.) Effect of use on potential market or value of the copyrighted work\n    ', 'day': '9'},
    "Sony V. Universal City Studios": {'def': '(1984 ‘The Betamax Case’) Supreme Court decided that the makers of a device with legitimate uses should not be penalized because some people may use it to infringe on copyright. Copying movies for later viewing was fair use', 'day': '10'},
    "Drm": {'def': '(Digital Rights Management) Collection of techniques that control uses of intellectual property in digital formats. Includes hardware and software schemes using encryption. The procedure of a file has flexibility to specify what a user may do with it.', 'day': '10'},
    "Dmca": {'def': '(The Digital Millennium Copyright Act of 1998) Anti Circumvention of DRM. Safe harbor protects web sites from lawsuits for copyright infringement by users of sites. Extended Telecommunications Act protections with the condition that providers abide by take down notices', 'day': '10'},
    "Riaa V. Napster": {'def': 'Court ruled napster liable because they had the right and ability to supervise the system, including copyright infringing activities', 'day': '10'},
    "Look And Feel": {'def': 'Refers to interface features. Generally not protected by copyright. Method of operation, not design.', 'day': '10'},
    "Hacktivism": {"def": "Use of hacking to promote a political cause", "day": "12"},
    "Responsible Disclosure": {"def": "Process of reporting security vulnerabilities to someone who can fix them rather than sharing or profiting from them", "day": "12"},
    "Cfaa": {"def": "(Computer Fraud And Abuse Act) It is illegal to access a computer without authorization", "day": "12"},
    "Phishing": {"def": "Requests for personal and financial information disguised as legitimate business communications in the form of E-mail", "day": "13"},
    "Smishing": {"def": "Requests for personal and financial information disguised as legitimate business communications in the form of text messaging", "day": "13"},
    "Vishing": {"def": "Requests for personal and financial information disguised as legitimate business communications in the form of voice phishing", "day": "13"},
    "Pharming": {"def": "False Web sites fish for personal and financial information by planting false URLs in Domain Name Servers", "day": "13"},
    "Responsibility To Prevent Access": {"def": "Publishers must prevent material or services from being accessed in countries when they are illegal", "day": "13"},
    "Authority To Prevent Entry": {"def": "Government of Country A can act within Country A to try to block the entrance of material that is illegal there, but may not apply its laws to the people who create and publish the material, or provide a service, in Country B if it is legal there", "day": "13"},
    "RAWA": {"def": "(Restoration of America’s Wire Act) bans most forms of online gambling (whether such activity was legalized and regulated by state governments or not", "day": "15"},
    "Unlawful Internet Gambling Enforcement Act": {"def": "(2006) It is forbidden to accept “any financial instrument” for internet gambling. Includes games of chances. Allows fantasy sports, legal interstate gambling; does not mention state lotteries or horse racing.", "day": "15"},
    "Outsourcing": {"def": "Phenomenon in which a company pays another company services instead of performing those tasks itself", "day": "16"},
    "Offshoring": {"def": "The practice of moving business processes or services to another country, especially overseas, to reduce costs", "day": "16"},
    "Inshoring": {"def": "When another company employs thousands of people in the U.S (e.g. offshoring for a German company means inshoring for U.S.)", "day": "16"},
    "Wisdom Of The Crowd": {"def": "The more who contribute, the more accurate the results.", "day": "18"},
    "Abdication Of Responsibility": {"day": "Giving up control or authority. People may be willing to let computers do their thinking or decision-making", "day": "18"},
    "The Digital Divide": {"def": "The gap between people who have ready access to technology and the internet and those who do not", "day": "19"},
    "Neo Luddites": {"def": "(Neo Luddism) Believe that technology is more harmful to society than it is beneficial.", "day": "19"},
    "Digital Dementia": {"def": "Short term memory dysfunction caused by reliance on digital devices rather than memory.", "day": "19"},
    "Planned Obsolescence": {"def": "Designed a product with an artificially limited useful life, so it will become obsolete, that is, unfashionable or no longer function after a certain period of time.", "day": "19"},
    "Technological Singularity": {"def": "Point at which artificial intelligence or some combined human-machine intelligence advances so far that we cannot control it.", "day": "19"},
    "Legacy Systems": {"def": "Outdated computer systems, programming languages or application software that are used instead of available upgraded versions.", "day": "20"},
    "Nonlinear": {"def": "Changes in output are not proportional to changes in input", "day": "20"},
    "Therac 25": {"def": "Massive overdoses of radiation were given; the machine said no dose had been administered at all. Caused severe and painful injuries; plus the death of six patients. Manufacturers, computer programmers, and hospitals/clinics all have some responsibility.", "day": "21"},
    "High Reliability Organization": {"def": "Preoccupation with failure. Has a loose structure, so no strict or intimidating hierarchy between programmers and others). An HRO is an organization that avoids disasters in a setting where catastrophes would seem common due to high risk and complexity.", "day": "21"},
    "Iv&V": {"def": "Independent verification and validation.", "day": "21"},
    "Tcas": {"def": "(Traffic Collision Avoidance System) Automated system that directs pilots in case of imminent collision. Computers in some airplanes prevent certain pilot actions. Near misses and accidents.", "day": "21"},
    "Acm": {"day": "Association for Computing Machinery → Provides a general statement for ethical values. Reminds people in the profession that ethical behavior is an essential part of their job. Provides guidance for new or young members. See the term IEEE as well and look into the jointed adaption between the IEEE and ACM which is the Software Engineering Code of Ethics and Professional Practice", "day": "22"},
    "Ieee": {"day": "Institute for Electrical and Electronics Engineers → Provides a general statement for ethical values. Reminds people in the profession that ethical behavior is an essential part of their job. Provides guidance for new or young members. See the term ACM as well and look into the jointed adaption between the IEEE and ACM which is the Software Engineering Code of Ethics and Professional Practice", "day": "22"}
}

DAY = {
    "22": 
    """
    Summary: Today is the Withdrawal Deadline. Also, make sure to let Professor Potasznik on Day 23 your decision on whether or not you are doing the Final Paper or not. During the lecture we looked into Professional Ethics and different ethics codes. We also discussed the 9.3.1 methodology that will be used on the Final Paper as well as the steps to take while writing.

    Slides: https://bpb-us-w2.wpmucdn.com/blogs.umb.edu/dist/7/3673/files/2022/11/Day-22.pdf 

    Terms:
        ACM
        IEEE
    """,
    "21": 
    """
    Summary: Today we covered more impacts based on technology glitches, however we covered more fatal and dire scenarios. We looked into the Therac 25 and the pitfalls it had. We also looked into the Challenger and Columbia missions and the oversights that had occurred. Finally, we looked into airplane incidents due to oversights. The main one being the Uberlingen Crash which was caused by unfortunate circumstances, human error, and a distrust of the automated TCAS system. 

    Slides: https://bpb-us-w2.wpmucdn.com/blogs.umb.edu/dist/7/3673/files/2023/04/Day-21.pdf 

    Video: https://liveumb-my.sharepoint.com/:p:/g/personal/amanda_potasznik_umb_edu/EZTfb9z_BeZDnbwX-s921h0Bq98sYdmTfx7BcHoA3umpig?e=rSoAOp 

    Terms:
        Therac 25
        High Reliablity Organization
        IV&V
        TCAS
    """,
    "20": 
    """
    Summary: Today we discussed the bugs and glitches, what contributes to them, and their impacts and outcomes.

    Slides:https://bpb-us-w2.wpmucdn.com/blogs.umb.edu/dist/7/3673/files/2022/11/Day-20.pdf

    Terms:
        Legacy Systems
        Nonlinear
    """,
    "19": 
    """
    Summary: We discussed the impact of technology on global development and the divides it can cause. The digital divide isn’t fixed by just giving technology. Furthermore, we went over the possible harm of technology which may outweigh the benefits. We looked into some of the Neo-Luddite arguments.

    Slides:https://liveumb-my.sharepoint.com/:p:/g/personal/amanda_potasznik_umb_edu/EV19il-tOnVDif6a16lcbLMB9BMgyZwWLtkHMNdNG7r7Sw?e=mDiYr3

    Terms:
        The Digital Divide
        Neo Luddites
        Digital Dementia
        Planned Obsolescence
        Technological SIngularity
    """,
    "18": 
    """
    Summary: We looked into the Wisdom of the Crowd and its reliability, especially when in the context of the internet. Abdication of Responsibility is another aspect where computer systems are made to be fully trusted and given authority. 

    Slides: https://bpb-us-w2.wpmucdn.com/blogs.umb.edu/dist/7/3673/files/2022/11/Day-18.pdf

    Terms:
        Wisdom Of The Crowd
        Abdication Of Responsibility
    """,
    "17": 
    """
    Summary: Exceptions to ECPA. Rights as an employee are not protected over the employer rights, even as a government employee. Social media does not mean private. A person can be fired or judged by companies based on their Social media. Employee privacy is usually put to the side when it comes to businesses.

    Slides: https://bpb-us-w2.wpmucdn.com/blogs.umb.edu/dist/7/3673/files/2022/11/Day-17.pdf

    Terms:
        None
    """,
    "16": 
    """
    Summary: Second presentation. In the lecture, we went over the impact automation has on Employment, Job creation, and Job destruction. We then discussed Off/Inshoring.

    Slides: https://bpb-us-w2.wpmucdn.com/blogs.umb.edu/dist/7/3673/files/2022/11/Day-16.pdf

    Terms:
        Outsourcing
        Offshoring
        Inshoring
    """,
    "15": 
    """
    Summary: First Presentation. During the lecture, we looked into Gambling Legislation and different ways technology has had an effect. 

    Slides: https://liveumb-my.sharepoint.com/:p:/g/personal/amanda_potasznik_umb_edu/EcEGwTKcWhFOtE0DWGUAmx0BrnXhfuUcXEB8H2AxqAoS2Q?e=wGuPHO

    Terms:
        RAWA
        Unlawful Internet Gambling Enforcement Act
    """,
    "14": 
    """
    Summary: Midterm

    Slides: 

    Terms:
    """,
    "13": 
    """
    Summary:  Midterm Exam next Class. Inside of the lecture, we covered identity theft. We also looked at different ways identity theft are attempted and looked over some cases. We also looked over how laws regarding the internet can cross borders (Kim Dotcom, Silk Road, Pirate Bay, etc.)

    Slides: https://bpb-us-w2.wpmucdn.com/blogs.umb.edu/dist/7/3673/files/2022/11/Day-13.pdf

    Terms:
        Phishing
        Smishing
        Vishing
        Pharming
        Responsibility To Prevent Access 
        Authority To Prevent Entry
    """,
    "12": 
    """
    Summary:Reminder, Midterm is 1 week from today. Make sure to bring hand-written notes.
            In the lecture, we covered ethical and unethical hacking. We looked into Stuxnet and other government cyber attacks. We also looked into the CFAA and how unauthorized access to a computer system is regulated. We also discussed the Lori Drew and the Aaron Swartz Case (Aaron’s Law).

    Slides:  https://bpb-us-w2.wpmucdn.com/blogs.umb.edu/dist/7/3673/files/2022/11/Day-12.pdf 

    Terms:
        Hacktivism
        Responsible Disclosure
        CFAA
    """,
    "11": 
    """
    Summary:  https://bpb-us-w2.wpmucdn.com/blogs.umb.edu/dist/7/3673/files/2022/11/Day-11.pdf 
              WWA Link: https://blogs.umb.edu/amandapotasznik/2023/10/09/changes-based-on-survey-answers/ 
                
              Weekly Write Up Alternative. It is a quiz based Alternative to the Weekly Write Up. See more information on the website. 

              In the Lecture, we covered Photographic Copyright. Exceptions to Public Photography. Who “owns” a photo. Deep Fakes. Image and video editing ethics.  
    Terms:
        No Terms
    """,
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
    "Wwa": "https://blogs.umb.edu/amandapotasznik/2023/10/09/changes-based-on-survey-answers/",
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
    "**Wwa**": "Alternative Weekly Write Up guidelines",
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