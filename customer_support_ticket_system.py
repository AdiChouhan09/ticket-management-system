class Ticket:
    def __init__(self, tid, customer, issue, priority):
        self.tid = tid
        self.customer = customer
        self.issue = issue
        self.priority = priority  # "NORMAL" or "URGENT"
        self.status = "OPEN"      # OPEN / IN_PROGRESS / RESOLVED
        self.assigned_agent = None

    def __str__(self):
        return (f"[{self.tid}] {self.customer} | {self.issue} | "
                f"Priority: {self.priority} | Status: {self.status} | "
                f"Agent: {self.assigned_agent}")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = node

    def find_by_id(self, tid):
        t = self.head
        while t:
            if t.data.tid == tid:
                return t.data
            t = t.next
        return None

    def delete_by_id(self, tid):
        prev = None
        cur = self.head
        while cur:
            if cur.data.tid == tid:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                return cur.data
            prev = cur
            cur = cur.next
        return None

    def traverse(self):
        t = self.head
        while t:
            yield t.data
            t = t.next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def is_empty(self):
        return self.head is None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def is_empty(self):
        return self.top is None


def read_int(prompt, mn=None, mx=None):
    while True:
        try:
            v = int(input(prompt))
            if mn is not None and v < mn:
                continue
            if mx is not None and v > mx:
                continue
            return v
        except:
            print("Invalid number. Try again.")


class TicketSystem:
    def __init__(self):
        self.tickets = LinkedList()
        self.normal_queue = Queue()
        self.urgent_queue = Queue()
        self.undo_stack = Stack()
        self.next_id = 1
        self.agents = ["Agent1", "Agent2", "Agent3"]
        self.agent_index = 0

    def _next_ticket_id(self):
        tid = self.next_id
        self.next_id += 1
        return tid

    def add_ticket(self):
        print("\n--- Add Ticket ---")
        customer = input("Customer name: ").strip()
        issue = input("Issue description: ").strip()
        pr = input("Priority (NORMAL/URGENT): ").strip().upper()
        if pr not in ("NORMAL", "URGENT"):
            pr = "NORMAL"
        tid = self._next_ticket_id()
        t = Ticket(tid, customer, issue, pr)
        self.tickets.append(t)
        if pr == "URGENT":
            self.urgent_queue.enqueue(tid)
        else:
            self.normal_queue.enqueue(tid)
        print(f"Ticket created with ID {tid}.")

    def view_tickets(self):
        print("\n--- All Tickets ---")
        found = False
        for t in self.tickets.traverse():
            print(t)
            found = True
        if not found:
            print("No tickets in the system.")

    def assign_next_ticket(self):
        print("\n--- Assign Next Ticket (Round Robin) ---")
        if not self.urgent_queue.is_empty():
            tid = self.urgent_queue.dequeue()
        else:
            tid = self.normal_queue.dequeue()
        if tid is None:
            print("No tickets in queue.")
            return
        ticket = self.tickets.find_by_id(tid)
        if ticket is None:
            print("Ticket not found in records.")
            return
        agent = self.agents[self.agent_index]
        self.agent_index = (self.agent_index + 1) % len(self.agents)
        prev_agent = ticket.assigned_agent
        prev_status = ticket.status
        ticket.assigned_agent = agent
        ticket.status = "IN_PROGRESS"
        self.undo_stack.push(("assign", ticket.tid, prev_agent, prev_status))
        print(f"Ticket {ticket.tid} assigned to {agent}.")

    def resolve_ticket(self):
        print("\n--- Resolve Ticket ---")
        tid = read_int("Enter ticket ID: ", 1)
        ticket = self.tickets.find_by_id(tid)
        if ticket is None:
            print("Ticket not found.")
            return
        prev_status = ticket.status
        ticket.status = "RESOLVED"
        self.undo_stack.push(("resolve", ticket.tid, prev_status))
        print(f"Ticket {ticket.tid} marked as RESOLVED.")

    def undo_last_action(self):
        print("\n--- Undo Last Action ---")
        action = self.undo_stack.pop()
        if action is None:
            print("No actions to undo.")
            return
        atype = action[0]
        if atype == "assign":
            tid, prev_agent, prev_status = action[1], action[2], action[3]
            ticket = self.tickets.find_by_id(tid)
            if ticket:
                ticket.assigned_agent = prev_agent
                ticket.status = prev_status
                if ticket.priority == "URGENT":
                    self.urgent_queue.enqueue(tid)
                else:
                    self.normal_queue.enqueue(tid)
                print(f"Undo: assignment of ticket {tid} reverted.")
        elif atype == "resolve":
            tid, prev_status = action[1], action[2]
            ticket = self.tickets.find_by_id(tid)
            if ticket:
                ticket.status = prev_status
                print(f"Undo: resolution of ticket {tid} reverted.")
        else:
            print("Unknown action type.")

    def view_tickets_by_agent(self):
        print("\n--- Tickets by Agent ---")
        mapping = {a: [] for a in self.agents}
        for t in self.tickets.traverse():
            if t.assigned_agent in mapping:
                mapping[t.assigned_agent].append(t)
        for agent in self.agents:
            print(f"\n{agent}:")
            if not mapping[agent]:
                print("  No tickets.")
            else:
                for t in mapping[agent]:
                    print(" ", t)


def main():
    system = TicketSystem()
    while True:
        print("\n====== CUSTOMER SUPPORT TICKET SYSTEM ======")
        print("1. Add Ticket")
        print("2. View All Tickets")
        print("3. Assign Next Ticket (Round Robin)")
        print("4. Mark Ticket as Resolved")
        print("5. Undo Last Action")
        print("6. View Tickets by Agent")
        print("7. Exit")
        choice = input("Select option: ").strip()
        if choice == "1":
            system.add_ticket()
        elif choice == "2":
            system.view_tickets()
        elif choice == "3":
            system.assign_next_ticket()
        elif choice == "4":
            system.resolve_ticket()
        elif choice == "5":
            system.undo_last_action()
        elif choice == "6":
            system.view_tickets_by_agent()
        elif choice == "7":
            print("Exiting Ticket System. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
