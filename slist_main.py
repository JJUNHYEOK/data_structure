from slist import SList

if __name__ == '__main__':
    s = SList()
    s.insert_front('a')
    s.insert_front('b')
    s.insert_after('c',s.head.next)
    s.insert_front('d')
    s.print_list()

    print('c는 %d번째'%s.search('c'))
    print('e는',s.search('s'))

    print('다음 노드 삭제 후:\t\t', end = '')
    s.delete_after(s.head)
    s.print_list()

    print('첫 노드 삭제 후:\t\t', end = '')
    s.delete_front()
    s.print_list()

    print('첫 노드로 f,g 삽입 후:\t', end = '')
    s.insert_front('f')
    s.insert_front('g')
    s.print_list()
    s.delete_after(s.head.next.next)

    print('a 다음 노드 삭제 후:\t', end = '')
    s.print_list()

    