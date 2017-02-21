package LRUCache;

import java.util.HashMap;

/**
 * Created by yunfan on 2017/2/21.
 */
public class LRUCache {
    private class Node{
        Node l;
        Node r;
        String key;
        String val;
        public Node(String key, String val){
            this.key = key;
            this.val = val;
        }

        @Override
        public String toString() {
            return super.toString() + "; key = " + key + ", val = " + val;
        }
    }

    private HashMap<String, Node> map;
    private Node head;
    private Node ends;
    private int size;

    public LRUCache(int size){
        this.size = size;
        head = new Node("$","$");
        ends = new Node("&","&");
        head.r = ends;
        ends.l = head;
        map = new HashMap<>();
    }

    private void setInHead(Node node){
        node.l = head;
        node.r = head.r;

        node.l.r = node;
        node.r.l = node;
    }

    private void removeNode(Node node){
        node.l.r = node.r;
        node.r.l = node.l;
    }

    public String get(String key){
        String res = null;
        if(map.containsKey(key) == true){
            Node changedNode = map.get(key);
            res = changedNode.val;
            removeNode(changedNode);
            setInHead(changedNode);
        }
        return res;
    }

    public void set(String key, String val){
        if(map.containsKey(key) == true){
            Node changedNode = map.get(key);
            changedNode.val = val;
            removeNode(changedNode);
            setInHead(changedNode);
        }else{
            if(map.size() >= size){
                Node deleteNode = ends.l;
                removeNode(deleteNode);
                map.remove(deleteNode.key);
            }
            Node newNode = new Node(key, val);
            setInHead(newNode);
            map.put(key,newNode);
        }
    }

    @Override
    public String toString() {
        String res = super.toString();
        res += "; size = " + map.size() + "\r\n";
        Node node = head;
        while(node != ends){
            res += "--" + node.toString() + "\r\n";
            node = node.r;
        }
        return res;
    }

    public static void main(String[] args){
        LRUCache lruCache = new LRUCache(4);
        for(int i = 0; i < 4; i ++){
            lruCache.set(String.valueOf(i),String.valueOf(i));
            System.out.println("-------------");
            System.out.println(lruCache.toString());
        }
        for(int i = 0; i < 4; i ++){
            lruCache.set(String.valueOf(i),String.valueOf(i + 1));
            System.out.println("-------------");
            System.out.println(lruCache.toString());
        }

        for(int i = 0; i < 4; i ++){
            System.out.println(lruCache.get(String.valueOf(i)));
            System.out.println("######");
            System.out.println(lruCache.toString());
        }
    }
}