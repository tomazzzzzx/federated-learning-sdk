class FederatedServer:
    def __init__(self, model, n): self.model, self.updates = model, []
    def receive(self, cid, u): self.updates.append(u)
    def aggregate(self):
        if not self.updates: return
        avg = {k: sum(u[k] for u in self.updates)/len(self.updates) for k in self.updates[0]}
        self.updates = []; return avg
