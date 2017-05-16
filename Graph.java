import java.util.*;

// BFS and DFS in Java
// Stored edges and towns as String

public class Graph {
    ArrayList <String> Edges = new ArrayList <String>();
    ArrayList <String> Towns = new ArrayList <String>();
    
    public void insertTown(String town) {
        this.Towns.add(town);
    }
    
    public void insertEdge(String source, String destination) {
        this.Edges.add(source + " " + destination);
    }
    
    public boolean dfs(String source, String destination) {
        ArrayList <String> queue = new ArrayList <String>();
        Hashtable <String, Integer> visited = new Hashtable <String, Integer>();
        queue.add(source);
        while (!queue.isEmpty()) {
            String city = queue.remove(0);
            ArrayList <String> adjacent = this.getAllAdjacent(city);
            for (String temp : adjacent) {
                if (temp.equals(destination)) {
                    return true;
                } else {
                    if (visited.get(temp) == null) {
                        visited.put(temp, 1);
                        queue.add(0, temp);
                    }
                }
            }            
        }            
        
        return false;
    }
    
    public boolean bfs(String source, String destination) {
        ArrayList <String> queue = new ArrayList <String>();
        Hashtable <String, Integer> visited = new Hashtable <String, Integer>();
        queue.add(source);
        visited.put(source, 1);
        while (!queue.isEmpty()) {
            String city = queue.remove(0);
            ArrayList <String> adjacent = this.getAllAdjacent(city);
            for (String temp : adjacent) {
                if (temp.equals(destination)) {
                    return true;
                } else {
                    if (visited.get(temp) == null) {
                        visited.put(temp, 1);
                        queue.add(temp);
                    }
                }
            }
        }
        return false;
    }
    
    public ArrayList <String> getAllAdjacent(String source) {
        
        ArrayList <String> all_adjacent = new ArrayList <String>();
        for (String temp : this.Edges) {
            String[] split = temp.split(" ");
            if (split[0].equals(source)) {
                all_adjacent.add(split[1]);
            }
        }
        return all_adjacent;
    }
    
    public ArrayList <String> getAllTowns() {
        return this.Towns;
    }
    
    public static void main(String[] args) {
        Graph g = new Graph();
        g.insertTown("A");
        g.insertTown("B");
        g.insertTown("C");
        g.insertTown("D");
        g.insertTown("F");
        g.insertTown("E");
        g.insertTown("G");
        g.insertTown("H");
        
        g.insertEdge("A", "B");
        g.insertEdge("A", "E");
        g.insertEdge("A", "D");
        g.insertEdge("E", "A");
        g.insertEdge("E", "C");
        g.insertEdge("C", "B");
        g.insertEdge("G", "F");
        g.insertEdge("F", "D");
        g.insertEdge("G", "F");
        g.insertEdge("E", "H");
        
        ArrayList <String> all_towns = g.getAllTowns();
        for (int i = 0; i < all_towns.size(); i++) {
            for (int j = 0; j < all_towns.size(); j++) {
                String source = all_towns.get(i);
                String destination = all_towns.get(j);
                if (!source.equals(destination)) {
                    System.out.println("DFS: " + source + "->" + destination + ": " + g.dfs(source, destination));
                    System.out.println("BFS: " + source + "->" + destination + ": " + g.bfs(source, destination));
                }
            }
        }
    }
}    




