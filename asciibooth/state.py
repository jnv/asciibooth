from fysom import Fysom

def printstatechange(e):
    print(e.event, e.src, e.dst)

def State():
    return Fysom(initial='init',
                 events= [
                    # name, src, dest
                    ('done', 'init', 'ready'),
                    ('capture', 'ready', 'capturing'),
                    ('output', 'capturing', 'outputting'),
                    ('idle', '*', 'idling'),
                    ('done', ['capturing', 'outputting', 'idling'], 'ready'),
                ],
                #callbacks={'onchangestate': printstatechange}
                )


def set_callback(state, event):
    def decorator(f):
        setattr(state, event, f)
        return f

    return decorator
