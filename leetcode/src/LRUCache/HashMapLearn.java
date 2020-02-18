package LRUCache;

import java.util.HashMap;

/**
 * Created by onion on 2017/2/21.
 */
public class HashMapLearn {
    public static void main(String[] args){
        HashMap<String, String> map = new HashMap<>();

        System.out.println(map.size());
        map.put("1","1");
        System.out.println(map.size());
        map.put("2",null);
        System.out.println(map.size());
        if(map.get("2") == null){
            System.out.println(map.containsValue("2"));
            System.out.println(map.containsKey("2"));
        }
        map.remove("1");
        System.out.println(map.size());
    }
}
