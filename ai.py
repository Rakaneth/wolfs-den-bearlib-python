from typing import List
from commands import Command, OutOfWorldCommand


class AI:
    def enter(self):
        pass

    def exit(self):
        pass

    def take_action(self, actor) -> Command:
        return OutOfWorldCommand()


class AIStack:
    def __init__(self):
        self.ai_stack: List[AI] = []

    def __iter__(self):
        return iter(self.ai_stack)

    def push(self, ai: AI):
        ai.enter()
        self.ai_stack.append(ai)

    def pop(self) -> AI:
        leaving = self.ai_stack.pop()
        leaving.exit()
        return leaving

    def peek(self) -> AI:
        return self.ai_stack[-1]

    def take_action(self, actor) -> Command:
        return self.peek().take_action(actor)

    @property
    def empty(self) -> bool:
        return len(self.ai_stack) == 0

    def clear(self):
        while not self.empty:
            self.pop()
