import java.util.*;

class Solution {
    public int[] solution(String[] park, String[] routes) {
        int[] answer = {-1, -1};
        
        for (int y = 0; y < park.length; y++) {
            for (int x = 0; x < park[y].length(); x++) {
                if (park[y].charAt(x) == 'S') {
                    answer[0] = y;
                    answer[1] = x;
                    break;
                }
            }
            if (answer[0] != -1 && answer[1] != -1) {
                break;
            }
        }
        
        for (int i = 0; i < routes.length; i++) {
            StringTokenizer st = new StringTokenizer(routes[i]);
            
            String dir = st.nextToken();
            int val = Integer.parseInt(st.nextToken());
            
            switch (dir) {
                case "N": 
                    if (answer[0] - val >= 0) {
                        boolean canMove = true;
                        
                        for (int j = answer[0]; j >= answer[0] - val; j--) {
                            if (park[j].charAt(answer[1]) == 'X') {
                                canMove = false;
                                break;
                            }
                        }
                        
                        if (canMove) {
                            answer[0] -= val;
                        }
                    }
                    break;
                case "S": 
                    if (answer[0] + val < park.length) {
                        boolean canMove = true;
                        
                        for (int j = answer[0]; j <= answer[0] + val; j++) {
                            if (park[j].charAt(answer[1]) == 'X') {
                                canMove = false;
                                break;
                            }
                        }
                        
                        if (canMove) {
                            answer[0] += val;
                        }
                    }
                    break;
                case "W": 
                    if (answer[1] - val >= 0) {
                        boolean canMove = true;
                        
                        for (int j = answer[1]; j >= answer[1] - val; j--) {
                            if (park[answer[0]].charAt(j) == 'X') {
                                canMove = false;
                                break;
                            }
                        }
                        
                        if (canMove) {
                            answer[1] -= val;
                        }
                    }
                    break;
                case "E": 
                    if (answer[1] + val < park[0].length()) {
                        boolean canMove = true;
                        
                        for (int j = answer[1]; j <= answer[1] + val; j++) {
                            if (park[answer[0]].charAt(j) == 'X') {
                                canMove = false;
                                break;
                            }
                        }
                        
                        if (canMove) {
                            answer[1] += val;
                        }
                    }
                    break;
            }
        }
        
        return answer;
    }
}