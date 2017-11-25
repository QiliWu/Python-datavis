from vispy import scene
from vispy import app
import sys
import numpy as np

canvas = scene.SceneCanvas(keys='interactive')
canvas.size = 800, 800
canvas.show()

view = canvas.central_widget.add_view()
img_data = np.random.normal(size=(100,100,3), loc=128, scale=40).astype(np.ubyte)
image = scene.visuals.Image(img_data, parent=view.scene)
view.camera = scene.PanZoomCamera(aspect=1)

if __name__ == '__main__' and sys.flags.interactive == 0:
    app.run()