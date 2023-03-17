ticks = {0:'|',
           1:'/',
           2:'—',
           3:'\\'}

def loading_str(i:'int', t:'int', verbose = False, text = 'iteration') -> 'str':
    '''Returns a string with a loading bar for iteration i out of t.'''
    progress = (10 * i)//t
    tick = ticks[i%4]
    to_go = 10 - progress
    output = f'[{progress * "*"}{tick}{to_go * "."}]'
    if verbose: output += f' {text} {i}/{t}'
    return output
    
def loading(i:'int', t:'int', verbose = False, text = 'iteration') -> 'str':
    '''Prints a loading bar for iteration i out of t'''
    print(loading_str(i,t,verbose,text), end = '\r')
    if i == t:
        print()
    
class LoadingBar:
    def __init__(self, t, verbose = False, text = 'iteration'):
        self.t = t
        self.i = 1
        self.verbose = verbose
        self.text = text
        
    def display(self):
        self.i += 1
        loading(self.i, self.t, self.verbose, self.text)
