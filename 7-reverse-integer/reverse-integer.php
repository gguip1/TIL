class Solution {

    /**
     * @param Integer $x
     * @return Integer
     */
    function reverse($x) {
        $resverse = 0;
        $isNegative = $x < 0;
        $x = abs($x);

        $minLimit = -2**31;
        $maxLimit = 2**31 - 1;

        while ($x > 0) {
            $pop = $x % 10;
            $x = (int)($x / 10);

            $reversed = $reversed * 10 + $pop;
        }

        $answer = $isNegative ? -$reversed : $reversed;
    
        if ($answer < $minLimit or $answer > $maxLimit) {
            return 0;
        }
        return $answer;
    }
}