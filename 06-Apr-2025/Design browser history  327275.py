# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.forward_history = []
        self.back_history = [homepage]
    def visit(self, url: str) -> None:
        self.forward_history = []
        self.back_history.append(url)

    def back(self, steps: int) -> str:
        while(steps and len(self.back_history) > 1):
            self.forward_history.append(self.back_history.pop())
            steps -= 1
        return self.back_history[-1]

    def forward(self, steps: int) -> str:
        while(steps and self.forward_history):
            self.back_history.append(self.forward_history.pop())
            steps -= 1
        return self.back_history[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)