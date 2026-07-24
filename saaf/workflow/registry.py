class WorkflowRegistry:
    """
    Registry of all workflow nodes.

    Responsible for:
    - Registering nodes
    - Finding nodes
    - Listing available nodes
    """

    def __init__(self):

        self._nodes = {}


    def register(self, action, node):

        self._nodes[action] = node


    def get(self, action):

        return self._nodes.get(action)


    def exists(self, action):

        return action in self._nodes


    def list_nodes(self):

        return list(self._nodes.keys())