def n_max(dic, n):
  """This function return n max for a dictionary"""
  n_max = []
  for i in range(n):
    n_max.append(max(dic))
    dic.remove(max(dic))
  return n_max

def n_min(dic,n):
  """This function return n min for a dictionary"""
  n_min = []
  for i in range(n):
    n_min.append(min(dic))
    dic.remove(min(dic))
  return n_min

def media(dic):
  """This function return the media for a dictionary"""
  media = sum(dic)/len(dic)
  return media

