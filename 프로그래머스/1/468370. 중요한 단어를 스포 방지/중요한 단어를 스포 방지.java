import java.util.*;

class Solution {
    boolean isSpoilerProof(int sIdx, int eIdx, int[][] spoiler_ranges) {
        for (int[] spoiler_range : spoiler_ranges) {
            if (spoiler_range[0] <= eIdx && sIdx <= spoiler_range[1]) {
                return true;
            }
        }
        return false;
    }
    
    public int solution(String message, int[][] spoiler_ranges) {
        int answer = 0;
        
        Set<String> spoiledSet = new HashSet<>();
        Set<String> dupSet = new HashSet<>();
        
        int ssIdx = 0;
        int eeIdx = 0;
        String wword = "";
        for (int idx = 0; idx < message.length(); idx++) {
            char ch = message.charAt(idx);
            
            if (ch == ' ' || idx == message.length() - 1) {
                if (idx == message.length() - 1) {
                    wword += ch;
                    eeIdx = idx;
                } else {
                    eeIdx = idx - 1;    
                }
                
                if (!isSpoilerProof(ssIdx, eeIdx, spoiler_ranges)) {
                    spoiledSet.add(wword);
                }
                ssIdx = idx + 1;
                wword = "";
            } else {
                wword += ch;
            }
        }   
        
        int sIdx = 0;
        int eIdx = 0;
        String word = "";
        for (int idx = 0; idx < message.length(); idx++) {
            char ch = message.charAt(idx);
            
            if (ch == ' ' || idx == message.length() - 1) {
                if (idx == message.length() - 1) {
                    word += ch;
                    eIdx = idx;
                } else {
                    eIdx = idx - 1;   
                }
                if (isSpoilerProof(sIdx, eIdx, spoiler_ranges)) {
                    if (!spoiledSet.contains(word) && !dupSet.contains(word)) {
                        answer += 1;
                        dupSet.add(word);
                    }
                }
                sIdx = idx + 1;
                word = "";
            } else {
                word += ch;
            }
        }        
        
        return answer;
    }
}