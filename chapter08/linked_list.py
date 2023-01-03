class Node:
    def __init__(self, name: str = "") -> None:
        self.prev: Node = None
        self.next: Node = None
        self.name: str = name


class LinkedList:
    def __init__(self) -> None:
        """ダミーノードnilを作成する"""
        self.nil = Node()
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def insert(self, v: Node, p: Node = None) -> None:
        """ノードpの直後にノードvを挿入する

        Args:
            v (Node): 挿入するノード
            p (Node): すでにリスト内に存在するノード
        """

        if p is None:
            p = self.nil

        v.next = p.next
        v.next.prev = v
        v.prev = p
        p.next = v

    def erase(self, v: Node) -> None:
        """ノードvを削除する

        Args:
            v (Node): 削除対象ノード
        """

        if v == self.nil:
            return
        v.next.prev = v.prev
        v.prev.next = v.next

    def print_list(self):
        cur = self.nil.next
        while cur is not self.nil:
            print(cur.name, "->", end=" ")
            cur = cur.next
        print()


def main():
    linked_list = LinkedList()
    name_list = ["yamamoto", "watanabe", "ito", "takahashi", "suzuki", "sato"]
    watanabe_node: Node  # 削除用のノードを保持する
    for i, name in enumerate(name_list):
        node = Node(name)
        linked_list.insert(node)
        print(f"step {i}: ", end="")
        linked_list.print_list()

        if name == "watanabe":
            watanabe_node = node

    # watanabeノードを削除する
    print("before: ")
    linked_list.print_list()
    linked_list.erase(watanabe_node)
    print("after: ")
    linked_list.print_list()


if __name__ == "__main__":
    main()
