import java.util.*;
import java.io.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        Map<String, Integer> ps = new HashMap<>();
        Map<String, Integer> cs = new HashMap<>();
        
        for(String p : participant){
            ps.merge(p, 1, Integer::sum);
        }
        
        for(String c : completion){
            ps.merge(c, -1, Integer::sum);
        }
        
        for(String key : ps.keySet()){
            if(ps.get(key) != 0){
                return key;
            }
        }
        
        return answer;
    }
}