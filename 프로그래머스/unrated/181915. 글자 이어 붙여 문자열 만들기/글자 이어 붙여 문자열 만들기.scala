object Solution {
    def solution(my_string: String, index_list: Vector[Int]): String = {
        val sList = my_string.toList
    	index_list.map(sList(_)).mkString("")
    }
}