import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine();
        int value = 0;

        char strBits[] = new char[str.length()];

        // strBits에 str의 모든 자리값을 담는다.
        for(int i = 0; i < strBits.length; i++){
            strBits[i] = str.charAt(i);
        }

        for(char bit : strBits){
            switch(bit){
                case 'A':
                case 'B':
                case 'C':
                    value += 3;
                    break;
                case 'D':
                case 'E':
                case 'F':
                    value += 4;
                    break;
                case 'G':
                case 'H':
                case 'I':
                    value += 5;
                    break;
                case 'J':
                case 'K':
                case 'L':
                    value += 6;
                    break;
                case 'M':
                case 'N':
                case 'O':
                    value += 7;
                    break;
                case 'P':
                case 'Q':
                case 'R':
                case 'S':
                    value += 8;
                    break;
                case 'T':
                case 'U':
                case 'V':
                    value += 9;
                    break;
                case 'W':
                case 'X':
                case 'Y':
                case 'Z':
                    value += 10;
                    break;

            }
        }
        System.out.println(value);

    }
}