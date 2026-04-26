# Version: v3 (Alternative)

# Approach:
# To maximize distance, assign all '_' to the dominant direction

class Solution:
    def furthestDistanceFromOrigin(self, moves):
        pos = 0
        blanks = 0

        for ch in moves:
            if ch == 'L':
                pos -= 1
            elif ch == 'R':
                pos += 1
            else:
                blanks += 1

        # push all blanks in the same direction
        return max(abs(pos + blanks), abs(pos - blanks))