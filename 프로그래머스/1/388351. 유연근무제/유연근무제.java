class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        
        for (int i = 0; i < schedules.length; i++) {
            boolean check = true;
            for (int j = 0; j < 7; j++) {
                int day = ((startday - 1) + j > 6) ? ((startday - 1) + j) % 7 : (startday - 1) + j;
                
                int sH = schedules[i] / 100;
                int sM = schedules[i] % 100 + 10;
                
                if (sM > 59) {
                    sH += 1;
                    sM %= 60;
                }
                
                int tH = timelogs[i][j] / 100;
                int tM = timelogs[i][j] % 100;
                
                // System.out.println(sH + " : " + sM + ", " + tH + " : " + tM);
                
                if (day != 5 && day != 6) {
                    if (tH > sH || (tH == sH && tM > sM)) {
                        check = false;
                    }   
                }
                // System.out.println(day + " " + check);
            }
            if (check) {
                answer++;
            }   
        }
        
        return answer;
    }
}