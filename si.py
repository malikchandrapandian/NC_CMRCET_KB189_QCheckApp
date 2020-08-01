from kivy.app import App
from kivy.lang import Builder
from PIL import Image
from kivy.uix.boxlayout import BoxLayout
import cv2
import time
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        capture: False
    Button:
        text: 'Capture'
        on_press: camera.capture = not camera.capture
        size_hint_y: None
        height: '68dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.jpg".format(timestr))
        print("Captured")
        

class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()

