class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1

        # in_degrees represents how many people trust that person
        # out_degrees represents how many people a person trusts
        in_degrees = [0] * (n + 1)
        out_degrees = [0] * (n + 1)

        for a, b in trust:
            in_degrees[b] += 1  # b is trusted by someone
            out_degrees[a] += 1  # a trusts someone

        # judge is trusted by n - 1 people (everyone except self) AND
        # judge does not trust anyone else
        for person in range(1, n + 1):
            if in_degrees[person] == n - 1 and out_degrees[person] == 0:
                return person

        return -1

        """
        This approach with adjacency mapping is cumbersome and requires
        iterating through the mapping multiple times. The logic to verify
        if a person (node) does not have any outgoing edges (i.e., trusting someone
        else) is not too difficult, since it is identified by having an empty list
        in the mapping, but identifying that everyone else trusts them is cumbersome. 

        if n == 1 and not trust:
            return 1

        adj = {}
        for person, trusted_person in trust:
            adj.setdefault(person, [])
            adj[person].append(trusted_person)
            # add judge since they are never in the 'person' position
            adj.setdefault(trusted_person, [])

        # Iterate through adj mapping to identify potential judges (empty trust list)
        potential_judges = []
        for key, val in adj.items():
            if val == []:
                potential_judges.append(key)

        for judge in potential_judges:
            total = 0
            for key, val in adj.items():
                if key != judge and judge in val:
                    total += 1
            if total == n - 1:
                return judge
        return -1
        """