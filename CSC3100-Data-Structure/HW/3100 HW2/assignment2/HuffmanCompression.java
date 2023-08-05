import java.io.*;
public class HuffmanCompression {
    public static String getCompressedCode(String inputText, String[] huffmanCodes) {
        String compressedCode = null;
        // Your code obtains the compressed code for inputText based on huffmanCodes
        // For example, if inputText="SUSIE SAYS IT IS EASY\n", and '\n' denotes linefeed.
        // , and huffmanCodes for inputText are: 
        // Space="00", A="010", T="0110", Linefeed="01110", U="01111", S="11",I="110",Y="1110",E="1111".
        // Then, your program will return the String shown in the following line:
        // "11011111111011110011010111011001100110001101100111101011111001110"
        //  S U    S I  E   SpS A  Y   S   I  T     I  S   E   A  S Y   Lf
        return compressedCode;
    }
    public static String[] getHuffmanCode(String inputText) {
        String[] huffmanCodes = new String[128];
        // Your code would obtain huffmanCodes for inputText
        // huffmanCodes[i]: huffman code of character with ASCII code i
        // if a character does not appear in inputText, then its huffmanCodes = null
        // For example, if inputText="SUSIE SAYS IT IS EASY\n", and '\n' denotes linefeed.
        // A possible huffmanCodes would be:
        // Space="00",A="010",T="0110",Linefeed="01110",U="01111",S="11",I="110",Y="1110",E="1111".
        return huffmanCodes;
    }
    public static void main(String[] args) throws Exception {
        // obtain input text from a text file encoded with ASCII code
        String inputText = new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get(args[0])), "US-ASCII");
        // get Huffman codes for each character and write them to a dictionary file
        String[] huffmanCodes = HuffmanCompression.getHuffmanCode(inputText);
        FileWriter fwriter1 = new FileWriter(args[1], false);
        BufferedWriter bwriter1 = new BufferedWriter(fwriter1);
        for (int i = 0; i < huffmanCodes.length; i++) 
            if (huffmanCodes[i] != null) {
                bwriter1.write(Integer.toString(i) + ":" + huffmanCodes[i]);
                bwriter1.newLine();
            }
        bwriter1.flush();
        bwriter1.close();
        // get compressed code for input text based on huffman codes of each character
        String compressedCode = HuffmanCompression.getCompressedCode(inputText, huffmanCodes);
        FileWriter fwriter2 = new FileWriter(args[2], false);
        BufferedWriter bwriter2 = new BufferedWriter(fwriter2);
        if (compressedCode != null) 
            bwriter2.write(compressedCode);
        bwriter2.flush();
        bwriter2.close();
    }
}
