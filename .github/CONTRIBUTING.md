<small><a href="../README.md">Back to README</a></small>

# Contributing Guidelines

We appreciate contributions from everyone! 🎉

![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat "Contributions Welcome")

The following is a set of guidelines for contributing to this project, which is hosted on GitHub. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

**Table of Contents**

- [Contributing Content](#contributing-content)
- [Tackling an Issue](#tackling-an-issue)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Pull Requests](#pull-requests)

---

## ✨ Contributing Content

This project shares interview prep code challenges and resources for the YearOne community, prompting daily prep topics and grouping resources by difficulty level. 

**To contribute**, you'll find all of the contributed resources in the `topics.yaml` file of the repository. Topics entered into this file are checked on a cron schedule using Github Actions. 

- Daily topics are randomly chosen, for all topics that have a difficulty level of `Beginner` or `Medium`, and posted straight to the YearOne community platform in the #Daily Challenge page. 
- A scheduled cron will run every few hours to scan for new entries and post them to the corresponding difficulty page in the YearOne community. 

### What makes a good topic?

A good topic can be a coding question or challenge from a popular site, a technical article or tutorial that teaches a skill, or a link to a video that you found handy for interview prep. 

Please check that all links provided are accessible for **free**. To do this, take the link and run it in an incognito window, if it's viewable, then it's accessible to all. 

### Formatting a Topic

Follow the formatting of the existing yaml file and the details below. Find out more about yaml files and their structure [here](https://yaml.org/).

```yaml
'1': #Represents the topic number, these should be sequential with the newest topic on the top of the file
  title: 'Common Prefix Problem' #The title of the topic or post
  difficulty: 'Beginner' #The difficulty should be Beginner, Medium or Advanced only, to make for easier parsing
  source: 'Leetcode' #The name of where the question/article or resource came from
  # Make sure to leave the pipe after the body key, to have Yaml recognize the next indented block as multi-line.
  # The Body text is written with HTML tags, for proper rendering to the community. Make sure to use break <br> tags to 
  # indicate new lines, and <a> tags to insert links!
  body: | 
    <strong>Beginner-level algorithm focused on strings!</strong><br>
    Write a function to find the longest common prefix string amongst an array of strings. <br>
    If there is no common prefix, return an empty string "".<br>
    <br>
    <a href="https://leetcode.com/problems/longest-common-prefix/" target="_blank">🎄Tree Algo Link!</a>
  author_name: 'Kristal' # (Optional) We shout out the contributor when the topic is posted, include your name if you'd like
  author_email: 'kristal@joinyearone.io' # (Optional) When we post in circle, we can change the author of the post by supplying
  # a members email address

```

---

## Tackling an Issue

As an open-source project, we'll have open [issues](https://github.com/YearOne-Prep/YearOne-prep-challenges/issues) that list out our enhancement and bug-fixes that need support. If you see one that you'd be willing to help with, here are the steps you should take:

- Step 1:
  - Find the ticket that you'd like to handle. 
- Step 2:
  - Make sure the ticket has all the information you need to get started. Post comments if you need more clarity or direction. 
- Step 3:
  - When you're ready to take on the ticket, comment that you're working on it. The ticket will then get assigned to you by a maintainer. 
- Step 4:
  - When your code or solution is ready, open your pull request for review. 
  - (optional) Link the Issue to your Pull Request in the right side-bar of the issue itself. 
- Step 5:
  - Merge that PR when it's approved and we'll close out the issue! 

---

## Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers and the community understand your report , reproduce the behavior, and find related reports.

Before creating bug reports, please do a quick search of existing issues as you might find out that you don't need to create one.

When you are creating a bug report, please include as many details as possible. Fill out the required template, the information it asks for helps us resolve issues faster.

### How Do I Submit A (Good) Bug Report?

Bugs are tracked as GitHub issues. Create an issue and provide the following information by filling in the provided template which appears when you try and open an issue.

Explain the problem and include additional details to help maintainers reproduce the problem:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible. For example, start by explaining how you started. When listing steps, **don't just say what you did, but explain how you did it**.
* **Provide specific examples to demonstrate the steps**. Include links to files or copy/pasteable snippets, which you use in those examples. If you're providing snippets in the issue, use Markdown code blocks.
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Include screenshots and animated GIFs** where possible. Show how you follow the described steps and clearly demonstrate the problem.
* **If the problem wasn't triggered by a specific action**, describe what you were doing before the problem happened and share more information using the guidelines below.
* **Can you reliably reproduce the issue?** If not, provide details about how often the problem happens and under which conditions it normally happens.
Include details about your configuration and environment:

---

## Suggesting Enhancements

This section guides you through submitting a suggestion, including completely new features and minor improvements to existing functionality. Following these guidelines helps maintainers and the community understand your suggestion and find related suggestions.

Before creating a suggestion, please do a quick search of existing issues as you might find out that you don't need to create one.

### How Do I Submit A (Good) Enhancement Suggestion?

Enhancement suggestions are tracked as GitHub issues. Create an issue and provide the following information by filling in the provided template which appears when you try and open an issue.

* **Use a clear and descriptive title** for the issue to identify the suggestion.
* **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
* **Provide specific examples to demonstrate the steps**. Include copy/pasteable snippets which you use in those examples, as Markdown code blocks.
* **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
* **Explain why this enhancement would be useful** to most users.

---

## Pull Requests

Please follow these steps to have your contribution considered by the maintainers:

1. Follow all instructions in the template.
2. After you submit your pull request, verify that all [status checks](https://help.github.com/articles/about-status-checks/) are passing.

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.