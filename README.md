# Customer Support Ticket System  
---

## Overview

The **Customer Support Ticket System** is a data-structure–based application that manages incoming customer support tickets using **queues, stacks, and linked lists**.  
It supports dynamic ticket creation, prioritisation of urgent issues, undo operations, and fair ticket processing in a **round-robin** manner.

This lab assignment focuses on implementing these data structures in **Python or C++** to simulate realistic customer support scenarios and to analyse their behaviour and performance.

---

## Objectives

- Design a simple system to manage customer tickets and their lifecycle.  
- Use **queues** to manage normal ticket flow.  
- Use **priority handling** (separate urgent queue or priority flag) for critical tickets.  
- Use a **stack** to implement undo operations (e.g., reverting last assignment or action).  
- Use **linked lists** for dynamic storage and traversal of tickets.  
- Simulate **round-robin ticket processing** among support agents.  
- Study and compare the behaviour of linear data structures in a real-world scenario.

---

## Data Structures Used

### 1. Queue  
Used for:  
- Managing incoming standard tickets in **FIFO** order.  
- Round-robin scheduling of tickets per agent.

### 2. Stack  
Used for:  
- Undoing the last ticket operation (e.g., last processed/assigned ticket).  
- Maintaining a history of actions.

### 3. Linked List  
Used for:  
- Dynamic storage of all ticket records.  
- Efficient insertion and deletion without shifting elements.

*(Optional)*  
- A separate **priority queue** or a high-priority linked list/queue for urgent tickets.

---

## Core Functionalities

### 1. Ticket Management
- Create a new ticket (ID, customer name, issue description, priority, timestamp).  
- View all open tickets.  
- Update ticket status (open, in-progress, resolved).  
- Close and archive tickets.

### 2. Queuing and Prioritisation
- Enqueue normal tickets into a standard ticket queue.  
- Enqueue urgent tickets into a priority queue or place them at the front.  
- Dequeue tickets when they are picked by support agents.

### 3. Round-Robin Assignment
- Maintain a list of support agents.  
- Assign tickets to agents in **round-robin** fashion (Agent1 → Agent2 → Agent3 → Agent1 → …).  
- Show which agent is handling which ticket.

### 4. Undo Operations (Stack)
- Record last actions (e.g., assignment, status change) on a stack.  
- Undo the last action by popping from the stack.  
- Restore the ticket to the previous state where possible.

### 5. Reporting (Optional)
- Show number of open, in-progress, and closed tickets.  
- Show tickets assigned per agent.  
- Show list of high-priority tickets.

---

## Implementation Steps

1. **Define Ticket Structure**  
   - Attributes: Ticket ID, customer name, issue summary, priority, status, timestamps, assigned agent.

2. **Implement Linked List / Storage**  
   - Store all tickets in a linked list or dynamic container.  
   - Provide operations for insertion, search by ID, and deletion/archiving.

3. **Implement Queues**  
   - Standard queue for normal tickets.  
   - Priority queue or separate urgent queue for high-priority tickets.

4. **Implement Stack for Undo**  
   - Push each critical action (e.g., assignment, status change) onto the stack.  
   - Provide function to undo last action by popping the stack.

5. **Round-Robin Scheduler**  
   - Maintain an array/list of agents.  
   - Use a circular index or queue to rotate through agents when assigning tickets.

6. **Menu-Driven Interface**  
   Example options:  
   - Add ticket  
   - View tickets  
   - Assign/Process next ticket  
   - Mark ticket as resolved  
   - Undo last action  
   - Show agent-wise ticket allocation  
   - Exit

7. **Testing & Analysis**  
   - Test with multiple normal and urgent tickets.  
   - Observe queue order, undo behaviour, and round-robin fairness.  
   - Discuss time complexity for enqueue, dequeue, push, pop, and list traversal.

---

## Technologies

You may implement this lab in:

- **Python** – using custom classes for queues, stacks, and linked lists (without relying solely on built-ins for logic).  
- **C++** – using classes/structs and manual implementation of core data structures (or STL as reference).

---

## Learning Outcomes

By completing this lab assignment, students will:

- Understand practical applications of **queues, stacks, and linked lists**.  
- Implement and use these structures in a real-world style scenario.  
- Learn how round-robin scheduling works in multi-agent systems.  
- Gain experience with undo functionality using stacks.  
- Improve skills in designing menu-driven, modular console applications.  
- Analyse the complexity and behaviour of fundamental data structures.

---

## Author

**Name:** Aditya Chouhan  
**Roll No:** 2401830001  
**Course:** B.Sc. (H) Cybersecurity  

---
