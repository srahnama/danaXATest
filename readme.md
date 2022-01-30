## A Python Spline Flask App for DanaXA Test By Shahab Rahnama

It is a project that implemented for DanaXA qualification test.

```
.
├── app.py
├── readme.md
├── requirements.txt
├── engine
│   ├── 1.jpg
│   ├── __init__.py
│   └── spline.py
├── model
│   ├── model.py
│   └── __init__.py
├── routes
│   ├── __init__.py
│   └── request_api.py
├── static
│   ├── sample_file.json
│   └── uploads
│       └── 1.jpg
└── templates
    └── index.html

```

* Data save in `static/sample_file.json`.
* Spline implemented in `engine/spline.py`.
* Routes implemented in `routes/request_api.py`.
* Bootstarp used for UI.



## Run

```
Python3 app.py

or

export FLASK_APP=app
flask run
```

## Getting Started

### Example Inputs:

Open `http://127.0.0.1:5000` in your browser then complete the form.

```
t = [0.,   0. ,  0.,  0.,   0.25, 0.5,  0.75, 1.,   1.,   1.,   1.  ]
c = [(839 , 216), (588, 205), (427, 8), (304, 159),(265, 100), (203, 175),(0,135)]
k = 3

```

![alt text](https://github.com/srahnama/danaXATest/blob/main/engine/1.jpg)

## Result

![alt text](https://github.com/srahnama/danaXATest/blob/main/static/uploads/2.jpg?raw=true)

## Prerequisites

* flask
* matplotlib
* numpy
* scipy
* jinja2


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

by : [Shahab Rahnama](http://srahnama.ir/)
