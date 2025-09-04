def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} → {destination}")
        return
    # Step 1: Move top n-1 disks from source to auxiliary
    tower_of_hanoi(n-1, source, destination, auxiliary)
    
    # Step 2: Move the largest disk from source to destination
    print(f"Move disk {n} from {source} → {destination}")
    
    # Step 3: Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n-1, auxiliary, source, destination)


# Example usage
n = 3
print("Steps to solve Tower of Hanoi:")
tower_of_hanoi(n, "A", "B", "C")
