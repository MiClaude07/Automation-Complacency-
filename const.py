HELP = """ 
Hello! This is a bot to assist you in CS285. Definitions of terms will be added the day of or at least by the next class. If you have any recommendations, DM @Michael.

__**Available Commands:**__
- **$def <term>**: provides definition for <term>. 
    Example call: $def Automation Complacency

- **$day <number>**: provides information from this day including a summary, link to the slides, and words. 
    Example call: $day 1

- **$lastday**: provides info on the latest day.

- **$dictionary**: provides definitions for all terms.
    Example call: $dicitionary

- **$resource <resource>**: provides a link to helpful resources. List of resources can be obtained with `$resource all`
    Example call: $resource final
"""


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
    "Turing Test": "An AI test in which if the computer convinces the human subject that the computer is human, the computer is said to `pass`"
}


DAY = {
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
        Turing Test
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