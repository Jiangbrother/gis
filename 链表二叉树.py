class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    new_node = TreeNode(value)
    if not self.root:
      self.root = new_node
      return
    queue = [self.root]
    while queue:
      current = queue.pop(0)
      if not current.left:
        current.left = new_node
        return
      elif not current.right:
        current.right = new_node
        return
      queue.append(current.left)
      queue.append(current.right)

pre = []
mid = []
bfs = []
def prev_create(root):
  if root is not None:
    pre.append(root.value)
    prev_create(root.left)
    prev_create(root.right)

def mid_create(root):
  if root is not None:
    mid_create(root.left)
    mid.append(root.value)
    mid_create(root.right)

def level_traversal(root):
  if root is None:
    return
  queue = [root]
  while len(queue) != 0:
    cur = queue.pop(0)
    bfs.append(cur.value)
    if cur.left is not None:
      queue.append(cur.left)
    if cur.right is not None:
      queue.append(cur.right)

tree = Tree()
data = [31, 23, 12, 66, None, 5, 17, 70, 62, None, None, 88, None, 55, None]
for i in data:
  tree.insert(i)

prev_create(tree.root)
pre = [x for x in pre if x is not None]
print(f'先序遍历：{pre}')

mid_create(tree.root)
mid = [x for x in mid if x is not None]
print(f'中序遍历：{mid}')

level_traversal(tree.root)
bfs = [x for x in bfs if x is not None]
print(f'层次遍历：{bfs}')