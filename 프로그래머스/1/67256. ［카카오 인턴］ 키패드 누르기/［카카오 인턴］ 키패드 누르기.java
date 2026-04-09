class Solution {
    
    public int getY(int number) {
        return number % 3 == 0 ? number / 3 : number / 3 + 1;
    }
    
    public int getX(int number) {
        return number % 3 == 0 ? 3 : number % 3;
    }
    
    public String lr(int number, String hand, int left, int right) {
        if (number == 1 || number == 4 || number == 7) {
            return "L";
        }
        
        if (number == 3 || number == 6 || number == 9) {
            return "R";
        }
        
        int ny;
        int nx;
        
        if (number == 0) {
            ny = 4;
            nx = 2;
        } else {
            ny = getY(number);
            nx = getX(number);
        }
        
        double ld;
        if (left == -1) {
            ld = Math.abs(ny - 4) + Math.abs(nx - 1);
        } else {
            int ly;
            int lx;
            
            if (left == 0) {
                ly = 4;
                lx = 2;
            } else {
                ly = getY(left);
                lx = getX(left);
            }
            
            ld = Math.abs(ny - ly) + Math.abs(nx - lx);
        }
        
        double rd;
        if (right == -1) {
            rd = Math.abs(ny - 4) + Math.abs(nx - 3);
        } else {
            int ry;
            int rx;
            
            if (right == 0) {
                ry = 4;
                rx = 2;
            } else {
                ry = getY(right);
                rx = getX(right);
            }
            
            rd = Math.abs(ny - ry) + Math.abs(nx - rx);
        }
        
        if (ld == rd) {
            if (hand.equals("left")) {
                return "L";
            } else {
                return "R";
            }
        } else if (ld < rd) {
            return "L";
        } else {
            return "R";
        }
    }
    
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int right = -1;
        int left = -1;
        
        for (int number : numbers) {
            String f = lr(number, hand, left, right);

            if (f.equals("L")) {
                left = number;
            }
            
            if (f.equals("R")) {
                right = number;
            }
                
            answer += f;
        }
        
        return answer;
    }
}