import java.io.*;
public class TestMathExpr
{
    public static void main(String[] args) throws Exception {
        FileReader freader = new FileReader(args[0]);
        BufferedReader breader = new BufferedReader(freader);
        FileWriter fwriter = new FileWriter(args[1], false);
        BufferedWriter bwriter = new BufferedWriter(fwriter);
        String str = breader.readLine();
        while (true){
            double result = MathExpr.parse(str);
            if ()
        }
    }
}
