<p align="center">
  <a href="" rel="noopener">
 <img src="https://cdn.discordapp.com/attachments/534693705442131988/738457979665252362/bannerbig.png" alt="Project logo"></a>
</p>
<h2 align="center">Thimathon - For Students</h2>

<div align="center">

[![Timathon](https://img.shields.io/badge/Timathon-For%20Students-blue.svg)](https://twtcodejam.net/)
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](./LICENSE.md)

</div>

---

My submission for the 2nd Timathon. I made a website around the "For Students" theme:

- an API
- a website around the API

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 Problem Statement <a name = "problem_statement"></a>](#-problem-statement-)
- [💡 Idea / Solution <a name = "idea"></a>](#-idea--solution-)
- [🎈 Usage <a name="usage"></a>](#-usage-)
- [🚀 Future Scope <a name = "future_scope"></a>](#-future-scope-)
- [🏁 Getting Started <a name = "getting_started"></a>](#-getting-started-)
  - [Prerequisites <a name = "prerequisites"></a>](#prerequisites-)
  - [Running the project <a name = "running"></a>](#running-the-project-)
- [⛏️ Built With <a name = "tech_stack"></a>](#️-built-with-)
- [✍️ Authors <a name = "authors"></a>](#️-authors-)

## 🧐 Problem Statement <a name = "problem_statement"></a>

The timathon theme is "For students". So I had to make something that could be useful for students and that could help them in their everyday life.

## 💡 Idea / Solution <a name = "idea"></a>

I thought about making an API for homeworks, timetables and other things useful to students. However an API alone isn't that easy to use, you would have to write code and not every student can do that, that's why I decided to make a website for it.

Students are able to add homeworks, timetables and more things that could help them at school.

## 🎈 Usage <a name="usage"></a>

Go on the [website](index), create your account, then you can use the following functionalities:

- [Create and manage homework](homework)
- [Create and manage your timetable](timetable)

## 🚀 Future Scope <a name = "future_scope"></a>

I'm going to add more endpoints to the API so more functionalities on the website. If you have any ideas/suggestions, you can leave an issue with a [feature request tag](https://github.com/takos22/timathon2-for-students/labels/feature%20request).

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites <a name = "prerequisites"></a>

To be able to run the website, you need to first install the required modules with:

```sh
pip install -r requirements.txt
```

### Running the project <a name = "running"></a>

To run the website you need to first add some environment variables:

- For shell

```sh
export DEBUG=1
export SECRET_KEY=secret_key_here
```

- For cmd

```cmd
set DEBUG=1
set SECRET_KEY=secret_key_here
```

Then do the database migrations:

```sh
py manage.py migrate
```

Then run the server:

```sh
py manage.py runserver
```

## ⛏️ Built With <a name = "tech_stack"></a>

- [Python](https://python.org/) - Language
- [Django](https://www.djangoproject.com/) - Backend for the API and website

## ✍️ Authors <a name = "authors"></a>

- [@takos22](https://github.com/takos22) - Idea & Coding
