from typing import Any

class FixedStack: #고정길이 스택 클래스

    class Empty(Exception):
        pass #비어있는 스택에 팝 또는 피크할 때 내보내는 예외 처리
    class Full(Exception):
        pass #가득 찬 스택에 푸시할 때 내보내는 예외 처리

    def __init__(self, capacity: int = 256 ) -> None:
        #스택 초기화
        self.stk = [None]*capacity #스택 본체
        self.capacity = capacity #스택 크기
        self.ptr = 0 #스택 길이

    def __len__(self) -> int:
        #스택에 쌓여 있는 데이터 개수 반환
        return self.ptr
    
    def is_empty(self)->bool:
        #스택이 비어있는지 판단
        return self.ptr <=0
    
    def is_full(self) -> bool:
        #스택이 가득 차 있는지 판단
        return self.ptr >= self.capacity
    
    def push(self, value:Any) -> None:
        #스택에 value를 푸시
        if self.is_full(): #스택이 가득 차 있는지 판단
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        #스택에서 데이터를 팝
        if self.is_empty(): #스택이 비어있는 경우
            raise FixedStack.Empty # 예외처리 발생
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self) -> Any:
        #스택에서 데이터 피크
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]
    
    def clear(self) -> None:
        #스택을 비움
        self.ptr = 0
        
    
        
