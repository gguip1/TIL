class Solution {

    /**
     * @param Integer $x
     * @return Integer
     */
    function reverse($x) {
        $string_x = (string) abs($x);
        $string_x = strrev($string_x);
        if ($x < 0) {
            $answer = -((int)$string_x);
        } else {
            $answer = ((int)$string_x);   
        }

        if ($answer < -2**31 or $answer > 2**31 - 1) {
            return 0;
        }
        return $answer;
    }
}