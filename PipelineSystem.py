import json


class Pipeline:
    def __init__(self, f, name, requiresText = False):
        self.func = f
        self.name = name
        self.text = ''
        self.model = ''
        self.requiresText = requiresText

    def set_text(self, text):
        self.text = text

    def set_model(self, model):
        self.model = model

    def activate(self):
        if self.text != '':
            if self.model != '':
                return self.func(self.model, self.text)
            return self.func(text=self.text)
        else:
            if self.model != '':
                return self.func(self.model)
            else:
                return self.func()


class PipelineSystem:
    data_loc = 'data.json'

    def __init__(self, gan_model="netG_checkpoint_009.pt", pipes=[]):
        with open(self.data_loc, 'r') as json_file:
            data = json.load(json_file)
            if 'active' not in data:
                data['active'] = -1
            with open(self.data_loc, 'w') as json_file:
                json.dump(data, json_file)
        self.pipelines = pipes
        self.gan_model = gan_model

    def set_active_pipeline(self, n_pipeline):
        with open(self.data_loc, 'r') as json_file:
            data = json.load(json_file)
            data['active'] = n_pipeline
            with open(self.data_loc, 'w') as json_file:
                json.dump(data, json_file)

    def get_active_pipeline(self, backend=False):
        with open(self.data_loc, 'r') as json_file:
            data = json.load(json_file)
            if data['active'] != -1:
                if backend:
                    return int(data['active'])
                return self.pipelines[int(data['active'])]
            else:
                return False
