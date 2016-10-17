import numpy as np
from vispy import app
from vispy import gloo
from dataprocess import rbt1

c = app.Canvas(keys = 'interactive')
vertex = """
attribute vec3 a_position;
void main (void)
{
    gl_Position = vec4(a_position, 0.0, 1.0);
}
"""
fragment = """
void main()
{
    gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0);
}
"""
program = gloo.Program(vertex, fragment)
program['a_position'] = rbt1.astype(np.float32)
@c.connect
def on_resize(event):
    gloo.set_viewport(0, 0, *event.size)
@c.connect
def on_draw(event):
    gloo.clear((1,1,1,1))
    program.draw('line_strip')
c.show()
app.run() 