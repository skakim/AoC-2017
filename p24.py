class BinaryTree():
  def __init__(self,comp,prev_strength,prev_used,used_i,deep):
    self.comp = comp
    self.not_used_i = 1-used_i
    self.children = []
    self.acc_strength = prev_strength + sum(comp)
    self.acc_used = prev_used + [comp]
    self.deep = deep

components = []
for _ in range(57):
  components.append(list(map(int,input().split("/"))))
  
trees = [BinaryTree(comp,0,[],comp.index(0),1) for comp in components if 0 in comp]
max_strength = 0
max_deep = 0
max_deep_str = 0
t = 0
for tree in trees:
  t += 1
  queue = [tree]
  i = 0
  while queue:
    i += 1
    root = queue.pop()
    children = [BinaryTree(comp,root.acc_strength,root.acc_used,comp.index(root.comp[root.not_used_i]),root.deep + 1) for comp in components if root.comp[root.not_used_i] in comp and comp not in root.acc_used]
    if not(children) and root.acc_strength > max_strength:
      max_strength = root.acc_strength
      print("PART 1", t, i, max_strength)
    if not(children) and root.deep > max_deep:
      max_deep = root.deep
      max_deep_str = root.acc_strength
      print("PART 2", t, i, max_deep, max_deep_str)
    elif not(children) and root.deep == max_deep and root.acc_strength > max_deep_str:
      max_deep_str = root.acc_strength
      print("PART 2", t, i, max_deep, max_deep_str)
    queue += children
    del root #avoid "Out of Memory"
