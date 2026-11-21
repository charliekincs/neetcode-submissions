class Solution:


    def __init__(self):
        self.Parent = {}
        self.Size = {}

    def find(self, node):
        if node != self.Parent[node]:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]
    
    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:
            return False
        
        if self.Size[p1] > self.Size[p2]:
            self.Parent[p2] = p1
            self.Size[p1] += self.Size[p2]
        else:
            self.Parent[p1] = p2
            self.Size[p2] += self.Size[p1]
        return True

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        for i in range(len(accounts)):
            self.Parent[i] = i
            self.Size[i] = 1

        unions = {}
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in unions:
                    self.union(i, unions[accounts[i][j]])
                else:
                    unions[accounts[i][j]] = i

        emails = defaultdict(list)
        for email, idx in unions.items():
            parent = self.find(idx)
            emails[parent].append(email)
        
        res = []
        for idx, email_list in emails.items():
            res.append([accounts[idx][0]])
            res[-1].extend(sorted(email_list))
        
        return res
