import java.util.Scanner;
public class Testy {
	public final char[] CHARSET = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','W','Z',';','.',',','!','?','1','2','3','4','5','6','7','8','9','0'};
	public final static String CHARSETSTRING = " ABCDEFGHIJKLMNOPQRSTUVWXYZ,.;:?!1234567890";
	public static void main(String[] args) {
		boolean done = false;
		boolean caught = false;	
		boolean advanced = false;
		Scanner shreyas = new Scanner(System.in);
		System.out.println("Key?");
		String key = shreyas.nextLine();
		//while(!done){
		System.out.println("Message?");
		String plainText = shreyas.nextLine();
		/*System.out.println("Is that it? y/n");
		if(shreyas.nextLine().equals("y")){
			done = true;
		}
		}*/
		System.out.println("Super-Secure mode? (adds the previous character to the character to be encrypted)");
		if(shreyas.nextLine().equals("y")){
			advanced = true;
		}
		//while(!caught){
		System.out.println("Decrypt or Encrypt?");
		String mode = shreyas.nextLine();
		if(mode.equals("encrypt")){
			System.out.println(encode(plainText, key, advanced));
		//	caught = true;
		}else if(mode.equals("decrypt")){
			System.out.println(decode(plainText, key, advanced));
		//	caught = true;
		}else{
			System.out.println("Didn't catch that");
		}
		//}
		
	}
	public static String encode(String plainText, String key, boolean advanced){
		int[] cipherText = convertInto(plainText);
		int[] numKey = convertInto(key);
		int prevChar = 0;
		for(int i = 0; i < cipherText.length; i ++){
			cipherText[i] += numKey[i%numKey.length] + prevChar + CHARSETSTRING.length();
			cipherText[i] %= CHARSETSTRING.length();
			if(advanced){
				prevChar = cipherText[i];
			}		
		}
		return convertOut(cipherText);
	}
	public static String decode(String plainText, String key, boolean advanced){
		int[] cipherText = convertInto(plainText);
		int[] numKey = convertInto(key);
		int prevChar = 0;
		for(int i = 0; i < cipherText.length; i ++){
			cipherText[i] -= numKey[i] + prevChar - CHARSETSTRING.length();
			cipherText[i] %= CHARSETSTRING.length();
			if(advanced){
				prevChar = cipherText[i];

			}	
		}
		return convertOut(cipherText);
	}
	public static int[] convertInto(String input){
		input = input.toUpperCase();
		int[] output = new int[input.length()];
		for(int i = 0; i < input.length(); i ++){
			output[i] = CHARSETSTRING.indexOf(input.charAt(i));
		}
		return output;
	}
	public static String convertOut(int[] input){
		String output = "";
		for(int i = 0; i < input.length; i ++){
			if(input[i] < 0)
				input[i] += CHARSETSTRING.length();
			output += CHARSETSTRING.charAt(input[i]);
		}
		return output;
	}

}
