#!/usr/bin/env python
import invoke
import jinja2


@invoke.task
def configure(ctx):
    template = jinja2.Template(open('environment.j2').read())
    kwargs = {}
    with open('.environment', 'w') as dst:
        dst.write(template.render(**kwargs))
