// Tree insertion (recursion)
// Tree inorder, preorder and postorder traversal! (recursion)


public class Tree {
    Node root;
    
    public Tree() {
        root = null;
    }
    
    public void insertNode(int key) {
        root = insertNode(new Node(key), root);
    }
    
    // Current starts at root
    private Node insertNode(Node new_node, Node current) {
        if (current == null) {
            return new_node;
        } else if (current.getKey() > new_node.getKey()) {
            current.left = insertNode(new_node, current.left);
        } else if (current.getKey() < new_node.getKey()) {
            current.right = insertNode(new_node, current.right);
        }
        
        return current;    
    }
    
    public Node getRoot() {
        return this.root;
    }
    
    public void Test() {
        System.out.println(this.root.getLeft());
    }
    
    public void inOrder() {
        System.out.println("Attempting an in-order print!");
        this.inOrder_print(root);
    }
    
    private void inOrder_print(Node root) {
        if (root == null) {
            return;
        } else {
            this.inOrder_print(root.getLeft());
            System.out.println(root.getKey());
            this.inOrder_print(root.getRight());
        }
    
    }
    
    private void preOrder() {
        System.out.println("Attempting a pre-order print!");
        this.preOrder_print(root);
    }

    private void preOrder_print(Node root) {
        if (root == null) {
            return;
        } else {
            System.out.println(root.getKey());
            this.preOrder_print(root.getLeft());
            this.preOrder_print(root.getRight());
        }
    
    }
    
    private void postOrder() {
        System.out.println("Attempting a post-order print!");
        this.postOrder_print(root);
    }

    private void postOrder_print(Node root) {
        if (root == null) {
            return;
        } else {
            this.postOrder_print(root.getLeft());
            this.postOrder_print(root.getRight());
            System.out.println(root.getKey());
        }
    
    }

    public static void main(String[] args) {

        Tree t = new Tree();
        
        t.insertNode(5);
        t.insertNode(2);
        t.insertNode(1);
        t.insertNode(3);
        t.insertNode(7);
        t.insertNode(10);
        t.inOrder();
        t.preOrder();
        t.postOrder();
    }
}

class Node {
    private int key;
    public Node left;
    public Node right;
    
    Node(int key) {
        this.key = key;
        right = null;
        left = null;
    }
    
    public int getKey() {
        return this.key;
    }
}
