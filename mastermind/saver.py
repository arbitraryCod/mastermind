import pickle
def save(name,thingy):
   with open(name+'.pickle', 'wb') as handle:
       pickle.dump(thingy, handle, protocol=pickle.HIGHEST_PROTOCOL)
def load(name):
   with open(name+'.pickle', 'rb') as handle:
      return(pickle.load(handle))
