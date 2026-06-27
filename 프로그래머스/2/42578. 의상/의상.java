import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> c = new HashMap<>();
        
        for(String[] clothe : clothes){
            c.merge(clothe[1], 1, Integer::sum);
        }
        
        for(Integer v : c.values()){
            answer *= v + 1;
        }
        
        return answer - 1;
    }
}