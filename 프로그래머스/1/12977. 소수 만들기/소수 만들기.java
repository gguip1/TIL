class Solution {
    public boolean isPrime(int num){
        int limit = (int) Math.sqrt(num);
        for (int i = 2; i <= limit; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
    
    public int solution(int[] nums) {
        int answer = 0;

        for (int idx1 = 0; idx1 < nums.length - 2; idx1++) {
            for (int idx2 = idx1 + 1; idx2 < nums.length - 1; idx2++) {
                for (int idx3 = idx2 + 1; idx3 < nums.length; idx3++) {
                    if (isPrime(nums[idx1] + nums[idx2] + nums[idx3])) {
                        answer++;
                    }
                }
            }
        }

        return answer;
    }
}