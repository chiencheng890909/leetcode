<?php
    class Solution {
    
        /**
         * @param String $s1
         * @param String $s2
         * @return Boolean
         */
        function checkInclusion($s1, $s2) {
            $Len_1 = strlen($s1);
            $Len_2 = strlen($s2);
            $index_1 = 0;
            $index_2 = 0;
            $temp_2 = $index_2;
    
            $Array_1 = ["init" => 0];
            for($i=0; $i < $Len_1; $i++){
                if(array_key_exists($s1[$i], $Array_1))
                    $Array_1[$s1[$i]] += 1;
                else
                    $Array_1[$s1[$i]] = 1;
            }
            $Copy_Array_1 = $Array_1;
    
    
            do {
                if($index_1 == $Len_1)
                    return true;
                if($Array_1[$s2[$index_2]] > 0) {
                    $Array_1[$s2[$index_2]] -= 1;
                    $index_1 ++;
                    $index_2 ++;
                }
                else {
                    $Array_1 = $Copy_Array_1;
                    $index_1 = 0;
                    $temp_2++;
                    $index_2 = $temp_2;
                }
            }while($index_2 < $Len_2);
    
            if($index_1 == $Len_1)
                return true;
            return false;
        }
    }
?>
