HELP = """ 
Hello! This is a bot to assist you in CS285. Definitions of terms will be added the day of or at least by the next class. If you have any recommendations, DM Michael.

__**Available Commands:**__
- **$def <term>**: provides definition for <term>. 
    Example call: $def Automation Complacency

- **$day <number>**: provides information from this day including a summary, link to the slides, and words. 
    Example call: $day 1

- **$lastday**: provides info on the latest day.

- **$dictionary**: provides definitions for all terms.
    Example call: $dicitionary

- **$resource <resource>**: provides a link to helpful resources. List of resources can be obtained with `$resources all`
    Example call: $resource final
"""


DICT = {
    "Term": "Definition"
}


DAY = {
    "1": 
    """
    Summary: Basic Summary of the Day and concepts
    Slides: Link to the slides
    Terms: Terms used today
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
    "Rubric": "https://blogs.umb.edu/amandapotasznik/rubrics/"
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
}