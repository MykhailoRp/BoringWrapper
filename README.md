# BoringWrapper

Wrapper for boring_api

## Installation

Install dependencies from req.txt with:

    pip install -r req.txt

Run main.py

    python main.py

## Usage

Add a new activity to DB with 'new' and by providing required parameters, more info with 'python main.py -h'

    python main.py new --type education --participants 1 --price_min 0.1 --price_max 30 --accessibility_min 0.1 --accessibility_max 0.5

See the last 5 activities with 'list'

    python main.py list

## Running example

    (venv) E:\PythonProjects\bored_wraper>python main.py new
    Activity - Take a caffeine nap, type: relaxation, participants: 1, price: 0.1, link: , key: 5092652, accessibility: 0.08
    
    (venv) E:\PythonProjects\bored_wraper>python main.py new
    Activity - Visit your past teachers, type: social, participants: 1, price: 0, link: , key: 8238918, accessibility: 0.7
    
    (venv) E:\PythonProjects\bored_wraper>python main.py new
    Activity - Watch the sunset or the sunrise, type: recreational, participants: 1, price: 0, link: , key: 4748214, accessibility: 1
    
    (venv) E:\PythonProjects\bored_wraper>python main.py new
    Activity - Learn how to make a website, type: education, participants: 1, price: 0.1, link: , key: 9924423, accessibility: 0.3
    
    (venv) E:\PythonProjects\bored_wraper>python main.py list
    (21, 5092652, 'Take a caffeine nap', 'relaxation', 1, 0.1, '', 0.08)
    (22, 8238918, 'Visit your past teachers', 'social', 1, 0.0, '', 0.7)
    (23, 4748214, 'Watch the sunset or the sunrise', 'recreational', 1, 0.0, '', 1.0)
    (24, 9924423, 'Learn how to make a website', 'education', 1, 0.1, '', 0.3)
