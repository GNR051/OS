import uuid

class FileSystem:
    def __init__(self):
        self.files = {}
    
    def create_file(self, filename):
        if filename in self.files:
            return f"File '{filename}' already exists."
        self.files[filename] = ""
        return f"File '{filename}' created."

    def write_file(self, filename, content):
        if filename not in self.files:
            return f"File '{filename}' not found."
        self.files[filename] = content
        return f"Written to file '{filename}'."

    def read_file(self, filename):
        if filename not in self.files:
            return f"File '{filename}' not found."
        return f"Contents of '{filename}': {self.files[filename]}"

    def list_files(self):
        return "Files: " + ", ".join(self.files.keys()) if self.files else "No files available."

class Process:
    STATUS_RUNNING = "Running"
    STATUS_WAITING = "Waiting"
    STATUS_TERMINATED = "Terminated"

    def __init__(self, name):
        self.name = name
        self.id = uuid.uuid4()
        self.status = Process.STATUS_RUNNING
    
    def set_status(self, status):
        if status in [Process.STATUS_RUNNING, Process.STATUS_WAITING, Process.STATUS_TERMINATED]:
            self.status = status
        else:
            raise ValueError("Invalid status")
    
    def __str__(self):
        return f"Process ID: {self.id}, Name: {self.name}, Status: {self.status}"

class ProcessManager:
    def __init__(self):
        self.processes = []

    def create_process(self, name):
        new_process = Process(name)
        self.processes.append(new_process)
        return f"Process '{name}' created with ID {new_process.id}."

    def update_process_status(self, process_id, status):
        for process in self.processes:
            if process.id == process_id:
                process.set_status(status)
                return f"Process '{process_id}' status updated to '{status}'."
        return f"Process ID '{process_id}' not found."

    def list_processes(self):
        return "\n".join(str(process) for process in self.processes) if self.processes else "No processes running."

class MemoryManager:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.used_memory = 0
        self.allocations = {}

    def allocate(self, size):
        if self.used_memory + size > self.total_memory:
            return "Not enough memory."
        alloc_id = uuid.uuid4()
        self.allocations[alloc_id] = size
        self.used_memory += size
        return f"Allocated {size}MB, ID: {alloc_id}."

    def deallocate(self, alloc_id):
        if alloc_id in self.allocations:
            size = self.allocations.pop(alloc_id)
            self.used_memory -= size
            return f"Deallocated {size}MB, ID: {alloc_id}."
        return f"Allocation ID '{alloc_id}' not found."

    def status(self):
        return f"Total Memory: {self.total_memory}MB, Used Memory: {self.used_memory}MB, Free Memory: {self.total_memory - self.used_memory}MB"

class SimpleOS:
    def __init__(self):
        self.file_system = FileSystem()
        self.process_manager = ProcessManager()
        self.memory_manager = MemoryManager(1024)  # Total 1024MB of memory
    
    def run_command(self, command):
        parts = command.split()
        cmd = parts[0]

        if cmd == "createfile":
            return self.file_system.create_file(parts[1])
        elif cmd == "writefile":
            return self.file_system.write_file(parts[1], " ".join(parts[2:]))
        elif cmd == "readfile":
            return self.file_system.read_file(parts[1])
        elif cmd == "listfiles":
            return self.file_system.list_files()
        elif cmd == "createprocess":
            return self.process_manager.create_process(parts[1])
        elif cmd == "updateprocess":
            process_id = uuid.UUID(parts[1])
            status = parts[2]
            return self.process_manager.update_process_status(process_id, status)
        elif cmd == "listprocesses":
            return self.process_manager.list_processes()
        elif cmd == "allocate":
            size = int(parts[1])
            return self.memory_manager.allocate(size)
        elif cmd == "deallocate":
            alloc_id = uuid.UUID(parts[1])
            return self.memory_manager.deallocate(alloc_id)
        elif cmd == "memorystatus":
            return self.memory_manager.status()
        elif cmd == "exit":
            return "Exiting SimpleOS..."
        else:
            return "Unknown command."

def main():
    os_sim = SimpleOS()
    print("Welcome to SimpleOS. Type 'exit' to quit.")
    
    while True:
        command = input(">>> ")
        result = os_sim.run_command(command)
        print(result)
        if result == "Exiting SimpleOS...":
            break

if __name__ == "__main__":
    main()

