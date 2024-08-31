# Python Installation?

# Open Terminal or Command Prompt

# Run Your Python File
- Type os.py into cmd






This simulation provides a good basis for understanding how basic operating system functions such as file management, process management, and memory management work. It's not as complex as a real operating system, but it's useful for grasping the basic principles.

This example shows step by step how the simple operating system simulation you created can be used. I will explain what I did at each step.

![İmage](https://github.com/GNR051/OS/blob/main/images/image14.jpeg)

# 1. Creating Files and Writing Content
First of all, we create a file and write content to this file.
![İmage](https://github.com/GNR051/OS/blob/main/images/image1.jpeg)
- This command creates a file named notes.txt


![İmage](https://github.com/GNR051/OS/blob/main/images/image2.jpeg)
- Add "Python is great for learning OS concepts." to the notes.txt file writes the text.

# 2. Reading and Listing the File
Now let's read the contents of the file we created and list the existing files.
![İmage](https://github.com/GNR051/OS/blob/main/images/image3.jpeg)
- This command reads the contents of the notes.txt file and writes it to the screen.

![İmage](https://github.com/GNR051/OS/blob/main/images/image4.jpeg)
- It lists the available files and shows that only notes.txt is currently available.

# 3. Creating a Process and Updating its Status
Let's create a new process and change the state of this process.
![İmage](https://github.com/GNR051/OS/blob/main/images/image5.jpeg)
- A process named MyProcess is created and a unique ID is assigned to this process.

![İmage](https://github.com/GNR051/OS/blob/main/images/image6.jpeg)
- It lists current processes and shows MyProcess's status as "Running".

![İmage](https://github.com/GNR051/OS/blob/main/images/image12.jpeg)
- Updates the status of the process to "Waiting".

![İmage](https://github.com/GNR051/OS/blob/main/images/image13.jpeg)
- We check the updated status and see that MyProcess is now in the "Waiting" state.

# 4. Memory Allocation and Release
Let's allocate memory and then release that memory.
![İmage](https://github.com/GNR051/OS/blob/main/images/image7.jpeg)
- 200 MB memory is allocated and a unique ID is assigned to this allocation.

![İmage](https://github.com/GNR051/OS/blob/main/images/image8.jpeg)
- The current memory status is shown: There is a total of 1024MB of memory, of which 200MB is used, 824MB is free.

![İmage](https://github.com/GNR051/OS/blob/main/images/image9.jpeg)
- We release the allocated memory.

![İmage](https://github.com/GNR051/OS/blob/main/images/image10.jpeg)
 -When the memory status is checked again, we see that all memory is free.

# 5. Exit
Let's get out of the simulation.
![İmage](https://github.com/GNR051/OS/blob/main/images/image11.jpeg)
- The simulation is terminated.


