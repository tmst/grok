import grok

class Pebbles(grok.Application, grok.Container):
    def __init__(self):
        super(Pebbles, self).__init__()
        self.gifts = []
    
class Index(grok.View):
    pass

class Edit(grok.View):
    def update(self, text=None):
        if text is None:
            return
        # this code has a BUG!
        self.context.incomes.append(text)
        self.redirect(self.url('index'))