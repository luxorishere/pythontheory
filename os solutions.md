# OS Notes

## Part 1

1. **What is an Operating System?** \
   An Operating System (OS) is system software that acts as an intermediary between computer hardware and users. It manages hardware resources and provides an environment for applications to run. The OS handles tasks like executing applications, managing memory, and controlling peripherals.

2. **What are the Goals of OS?**
   - **Primary Goals:** Ensure that the system operates efficiently and reliably. This includes managing resources such as CPU, memory, and I/O devices to maximize performance and prevent conflicts.
   - **Secondary Goals:** Provide a convenient and user-friendly environment. This includes offering a graphical user interface (GUI), command-line interface (CLI), and other tools to make the system easy to use and interact with.

3. **Functions / Components of OS**
   - **Process Management:** Handles creation, scheduling, and termination of processes.
   - **Memory Management:** Manages the allocation and deallocation of memory space as needed by various programs.
   - **File System Management:** Organizes, stores, retrieves, and manages data on storage devices.
   - **Device Management:** Manages device communication via their respective drivers.
   - **Security and Access Control:** Protects data and resources from unauthorized access and ensures data integrity.

4. **What is a Batch Operating System?**
   A Batch Operating System processes jobs in batches without user interaction. Users submit jobs to a queue, and the system processes them one by one. This type of OS is efficient for long-running, non-interactive tasks where user input is not required during execution.

5. **What is Spooling?**
   Spooling (Simultaneous Peripheral Operations Online) is a process where data is temporarily stored to be used and executed by a device, such as a printer. It helps manage the job scheduling by allowing the system to queue tasks and process them sequentially, thus optimizing device usage and minimizing wait times.

6. **What is a Multiprogramming OS?**
   - **Advantages:**
     - Maximizes CPU utilization by running multiple programs concurrently.
     - Increases system throughput by keeping the CPU busy.
   - **Disadvantages:**
     - Complex implementation and management.
     - Difficulties in handling memory management and process synchronization.
   - **Non-Multiprogramming OS:**
     - **Advantages:** Easier to implement and manage.
     - **Disadvantages:** Inefficient CPU usage as the system runs one task at a time, leading to idle CPU time.

7. **What is a Multitasking System?**\
   A multitasking system allows multiple tasks or processes to run concurrently by rapidly switching between them. This improves user productivity and system efficiency, making it possible for users to perform multiple operations, such as browsing the web while editing a document.

8. **What is Multiprogramming with Round Robin?**\
   Multiprogramming with Round Robin scheduling assigns a fixed time slice or quantum to each process in a cyclic order. Once a process's time slice expires, the next process in the queue gets the CPU. This method ensures fairness and responsiveness, preventing any single process from monopolizing the CPU.

9. **What is Time Sharing?**\
   Time sharing allows multiple users to share system resources simultaneously by rapidly switching the CPU among them. It provides quick response times for interactive tasks, making it appear as though each user has their own dedicated system.

```
 _______  _______  _______  _______  _______  _______  _______  _______
|       ||       ||       ||       ||       ||       ||       ||       |
|  P1   ||  P2   ||  P3   ||  P4   ||  P5   ||  P6   ||  P7   ||  P8   |
|_______||_______||_______||_______||_______||_______||_______||_______|

 _______  _______  _______  _______  _______  _______  _______  _______
|       ||       ||       ||       ||       ||       ||       ||       |
|_______||_______||_______||_______||_______||_______||_______||_______|

 _______  _______  _______  _______  _______  _______  _______  _______
|       ||       ||       ||       ||       ||       ||       ||       |
|  CPU  ||  CPU  ||  CPU  ||  CPU  ||  CPU  ||  CPU  ||  CPU  ||  CPU  |
|_______||_______||_______||_______||_______||_______||_______||_______|

 _______  _______  _______  _______  _______  _______  _______  _______
|       ||       ||       ||       ||       ||       ||       ||       |
|_______||_______||_______||_______||_______||_______||_______||_______|

 _______  _______  _______  _______  _______  _______  _______  _______
|       ||       ||       ||       ||       ||       ||       ||       |
| Time  || Time  || Time  || Time  || Time  || Time  || Time  || Time  |
| Slice || Slice || Slice || Slice || Slice || Slice || Slice || Slice |
|_______||_______||_______||_______||_______||_______||_______||_______|
```

In this representation:

- Each "P" (P1, P2, P3, etc.) represents a different process.
- The "CPU" blocks represent the CPU time allocated to each process.
- The "Time Slice" blocks indicate the division of time allocated to each process in a time-sharing system.


10.  **What is a Multiprocessing System?**
    - **Tightly Coupled System:** Multiple processors share a common memory and are connected by a high-speed bus, working closely together.
    - **Symmetric Processing:** All processors are equal and share the same memory and I/O devices, enhancing reliability and performance.
    - **Asymmetric Processing:** One processor controls the system and assigns tasks to other processors, simplifying system design but potentially creating bottlenecks.

2.  **What is a Real-Time OS?**
    - **Hard Real-Time OS:** Guarantees strict timing constraints for task completion, essential for critical systems like medical devices or industrial controls.
    - **Soft Real-Time OS:** Less stringent timing constraints where delays are acceptable, used in applications like multimedia systems.

3.  **What is a Distributed OS?**\
    A Distributed Operating System manages a group of distinct computers and makes them appear as a single system to users. It enables resource sharing, load balancing, and fault tolerance across multiple machines, enhancing overall system performance and reliability.

4.  **What is the Structure of OS?**
    The structure of an OS typically includes:
    - **Hardware:** The physical components of the computer.
    - **Kernel:** The core part of the OS, managing hardware resources.
    - **System Calls:** Interfaces for applications to interact with the OS.
    - **Application Programs:** Software that performs specific tasks for users.

5.  **Define Micro Kernel?**
    A Micro Kernel is a minimalistic kernel design that only includes essential functions like process management, memory management, and IPC (Inter-Process Communication). Other services run in user space, improving system reliability and security by isolating critical components from non-essential services.

6.  **User and OS Interface**
    - **Command Line Interface (CLI):** A text-based interface where users type commands to interact with the OS. It is powerful for advanced users but has a steep learning curve.
    - **Graphical User Interface (GUI):** A visual interface with windows, icons, and menus, making it more intuitive and user-friendly for general users.

7.  **What is a System Call?**\
    A system call is a programmatic way for a process to request a service from the OS. It provides an interface between the user programs and the OS, allowing programs to perform tasks like reading a file, creating a process, or communicating with hardware devices.

8.  **What is Device Management?**\
    Device management involves managing the operation and control of peripheral devices such as printers, disk drives, and network cards. The OS uses device drivers to translate OS commands into device-specific operations, ensuring smooth communication between hardware and software.

9.  **What is Mode?**
    - **User Mode:** A restricted mode where applications run, preventing them from directly accessing hardware or critical OS areas.
    - **Kernel Mode:** A privileged mode where the OS operates, allowing unrestricted access to hardware and system resources.

10. **What is a Process?**\
    A process is an instance of a program in execution. It includes the program code, current activity, and associated resources such as memory and open files. The OS manages processes by allocating resources and scheduling CPU time.

11. **What is a Program?**\
    A program is a static set of instructions written in a programming language, stored on disk. It becomes a process when executed by the OS, transitioning from passive code to an active entity in the system.

12. **Program vs. Process**\
    - **Program:** A set of instructions stored on disk; static and passive.
    - **Process:** An executing instance of a program; dynamic and active, with associated resources.

13. **What is Process Control Block (PCB)?**\
    The PCB is a data structure used by the OS to store information about a process. It includes process state, process ID, CPU registers, memory management information, and I/O status, allowing the OS to manage and control processes effectively.

14. **What is Process State?**
    - **New:** The process is being created.
    - **Ready:** The process is ready to run but waiting for CPU time.
    - **Running:** The process is currently being executed by the CPU.
    - **Waiting:** The process is waiting for some event to occur (e.g., I/O completion).
    - **Terminated:** The process has finished execution and is being removed from memory.
  

### Hard Real-Time OS vs. Soft Real-Time OS

| Feature                  | Hard Real-Time OS                               | Soft Real-Time OS                                 |
|--------------------------|-------------------------------------------------|---------------------------------------------------|
| **Timing Constraints**   | Strict, guaranteed deadlines                    | Less strict, delays are acceptable                |
| **Use Cases**            | Critical systems (e.g., medical devices, industrial control) | Non-critical systems (e.g., multimedia, gaming)    |
| **Predictability**       | Highly predictable                              | Moderately predictable                            |
| **Failure Consequence**  | Catastrophic if deadlines are missed            | Degraded performance if deadlines are missed      |
| **Scheduling**           | Deterministic, real-time scheduling algorithms  | Generally real-time scheduling but less stringent |
| **Example**              | Airbag systems in cars                          | Video streaming applications                      |

### Command Line Interface (CLI) vs. Graphical User Interface (GUI)

| Feature                  | Command Line Interface (CLI)                   | Graphical User Interface (GUI)                    |
|--------------------------|------------------------------------------------|--------------------------------------------------|
| **Ease of Use**          | Steep learning curve, requires knowledge of commands | Intuitive, easy to use with visual elements       |
| **Efficiency**           | Fast for experienced users                     | May be slower due to graphical rendering          |
| **Resource Usage**       | Low, uses minimal system resources             | High, requires more memory and processing power   |
| **Flexibility**          | Highly flexible with powerful scripting        | Limited to predefined operations                  |
| **Accessibility**        | Can be accessed remotely via terminal          | Typically requires local access                   |
| **Examples**             | Bash, PowerShell                               | Windows, macOS, GNOME                             |

### Program vs. Process

| Feature                  | Program                                        | Process                                           |
|--------------------------|------------------------------------------------|--------------------------------------------------|
| **Definition**           | Static set of instructions                     | Dynamic instance of a program in execution       |
| **State**                | Passive, stored on disk                        | Active, running in memory                         |
| **Lifespan**             | Exists until deleted or modified               | Created, executed, and terminated by the OS       |
| **Resource Usage**       | Requires storage space                         | Requires CPU, memory, and other resources         |
| **Multiple Instances**   | One program can have multiple instances (processes) | Each instance is a separate process               |
| **Example**              | MS Word application file                       | MS Word running with a specific document open     |

