#! /usr/bin/python

# Experimenting with the Jinja tutorial from
# https://medium.com/@jasonrigden/jinja2-templating-engine-tutorial-4bd31fb4aea3

from jinja2 import Environment, FileSystemLoader
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

""" template = env.get_template('base.html.jinja')

output = template.render(title='pretty standard')
 """
 
template = env.get_template('child.html.jinja')

output = template.render(title='A title', body='body under python control')
print(output)