import pandas

def create_subbox(tag, title, ingredients):
    """ Create and return a new container filling. """
    subbox = subbox(tag=tag, 
                    title=title, 
                    ingredients=ingredients) 
    return subbox

def get_subboxes():
    """ Return all filling options. """
    return subbox.query.all()

def get_subbox_by_tag(tag):
    """ Return container filling by tag. """
    return subbox.query.get(tag)
