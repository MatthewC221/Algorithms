import java.util.*;

// Binary search in Java! Recursive

public class binSearch {

    public static int index(ArrayList <Integer> numbers, int target, int start, int end) {
        
        int middle = (start + end) / 2;
        
        if (start + 1 == end && numbers.get(start) != target) {
            return -1;
        }
        
        if (numbers.get(middle).equals(target)) {
            return middle;
        } else if (numbers.get(middle) > target) {      // Have to go back
            return index(numbers, target, start, middle);
        } else if (numbers.get(middle) < target) {
            return index(numbers, target, middle, end);
        }
        
        return -1;
    
    }

    public static void main(String[] args) {
        if (args.length == 1) {
            int target = Integer.parseInt(args[0]);
            ArrayList <Integer> numbers = new ArrayList <Integer>();
            for (int i = 0; i < 10; i = i + 2) {
                numbers.add(i);
            }
            
            if (target > 9 || target < 0) {
                System.out.println("Target out of range!");
            } else if (target == 0) {
                System.out.println("Found at index 0");
            } else {
                System.out.println("Found at index " + index(numbers, target, 0, numbers.size()));
            }
        } else {
            System.out.println("Usage: java binSearch <number>");
        }
    }


}
