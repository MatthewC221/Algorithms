import java.util.*;

// Dynamic programming example in Java
// Coin change problem, giving a target and a list of coin sizes
// Return the least amount of coins used to fill the target.
// E.g. for $10, given coins ($1, $2, $3), the least amount of coins = 3 * $3 + 1 * $1 = 4

public class coin_change {

    public static void change(ArrayList <Integer> coins, int target) {
    
        ArrayList <Integer> minimum_amount = new ArrayList <Integer>();
        for (int i = 0; i < target + 1; i++) {
            minimum_amount.add(9999);
        }
        
        minimum_amount.set(0, 0);
        for (int i = 1; i < target + 1; i++) {
            for (int j = 0; j < coins.size(); j++) {
                if (i - coins.get(j) >= 0) {
                    if (1 + minimum_amount.get(i - 1) < 1 + minimum_amount.get(i - coins.get(j))) {
                        minimum_amount.set(i, 1 + minimum_amount.get(i - 1));
                    } else {
                        minimum_amount.set(i, 1 + minimum_amount.get(i - coins.get(j)));
                    }
                }
            }
        }
        
        for (int i = 0; i < target + 1; i++) {
            System.out.print(minimum_amount.get(i) + " ");
        }
        
        System.out.println("\nThe least amount of coins for " + target + " = " + minimum_amount.get(target));
    
    
    }
    
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java coin_change.java <amount>");
        } else {
            ArrayList <Integer> coin_amount = new ArrayList <Integer>();
            coin_amount.add(1);
            coin_amount.add(3);
            coin_amount.add(6);
            int amount = Integer.parseInt(args[0]);
            change(coin_amount, amount);
        }

    }
}
