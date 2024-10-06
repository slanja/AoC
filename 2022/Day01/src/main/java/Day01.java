import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Day01 {

    public static void main(String[] args) throws IOException {

        Part2();

    }

    public static void Part1() {
        List<String> lines = null;

        try {
            lines = Files.readAllLines(Paths.get("src/main/java/input.txt"));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        int sum = 0;
        int highest = 0;

        for (int i = 0; i < lines.size(); i++) {
            if (!lines.get(i).isEmpty()) {
                sum += Integer.parseInt(lines.get(i));
            }

            else {
                if (sum > highest) highest = sum;
                sum = 0;
            }
        }

        System.out.println(highest);
    }

    public static void Part2() {
        List<String> lines = null;

        try {
            lines = Files.readAllLines(Paths.get("src/main/java/example.txt"));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        int sum = 0;
        int temp = 0;
        int temp2 = 0;

        int highest = 0;
        int second = 0;
        int third = 0;

        boolean switched = false;


        for (int i = 0; i < lines.size(); i++) {
            if (!lines.get(i).isEmpty()) {
                sum += Integer.parseInt(lines.get(i));
            }

            else {
                if (sum > highest) {
                    temp = highest;

                    highest = sum;
                    switched = true;

                    System.out.println("h: " + highest);
                }

                if (switched){
                    temp2 = second;
                    second = temp;
                    temp = 0;


                    System.out.println("s: " + second);
                }

                else if (sum < highest) second = sum;

                if (switched) {
                    third = temp2;
                    temp2 = 0;

                    System.out.println("t: " + third);
                }

                if (sum <= second) third = sum;

                sum = 0;
                switched = false;
                System.out.println();
            }
        }

        System.out.println(highest + second + third);
    }
}