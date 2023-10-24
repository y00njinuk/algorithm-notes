object Main {
  def main(args: Array[String]): Unit = {
    var num = (scala.io.StdIn.readLine() split " " take 2 map (_.toInt));
    println(num(0) - num(1))
  }
}