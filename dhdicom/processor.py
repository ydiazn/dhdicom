# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-


class DHDicomHandler:

    def __init__(self, data_handler=None, hider_handler=None):
        self.data_handler = data_handler
        self.hider_handler = hider_handler

    def process(self, image):
        '''
        handler.process(image), oculta registros del EPR en la imagen y
        los anonimiza. Los registros se especifican en el data_handler
        '''
        import json

        # anonimización
        epr = self.data_handler.anonimize(image)
        # Ocultacion del EPR y autenticacion
        msg = self._get_message(epr)
        self.hider_handler.process(image.read(), msg)
        image.write()

    def authenticate(self, image):
        return self.hider_handler.authenticate(image.read())

    def _get_message(self, data):
        import json

        return json.dumps(data)
