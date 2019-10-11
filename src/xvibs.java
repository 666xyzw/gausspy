import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Enumeration;
import java.util.Locale;
import java.util.Vector;

public class xvibs {
  static final String version = "17m2";
  
  static boolean debugging = false;
  
  private static double defaultFreqScale = 0.7D;
  
  private static double defaultVectorScale = 2.0D;
  
  private static boolean defaultByBounce = false;
  
  private static int defaultNumberFrames = 20;
  
  private static boolean defaultUseFreqInName = false;
  
  static double freqScale = defaultFreqScale;
  
  static double vectorScale = defaultVectorScale;
  
  static boolean byBounce = defaultByBounce;
  
  static int numberFrames = defaultNumberFrames;
  
  static String listFileName = null;
  
  static boolean useFreqInName = defaultUseFreqInName;
  
  private static final DecimalFormatSymbols decimalSymbols = new DecimalFormatSymbols(Locale.US);
  
  public static void main(String[] paramArrayOfString) {
    try {
      int m;
      int k;
      if (debugging) {
        System.err.print("args: ");
        for (byte b = 0; b < paramArrayOfString.length; b++)
          System.err.print(String.valueOf(paramArrayOfString[b]) + ' '); 
        System.out.println();
      } 
      int i = 0;
      while (i < paramArrayOfString.length && paramArrayOfString[i].charAt(0) == '-') {
        if (paramArrayOfString[i].equals("--")) {
          i++;
          break;
        } 
        if (paramArrayOfString[i].equals("-useFreqInName")) {
          useFreqInName = true;
          if (debugging)
            System.err.println("useFreqInName mode"); 
          i++;
          continue;
        } 
        if (paramArrayOfString[i].equals("-bounce")) {
          byBounce = true;
          if (debugging)
            System.err.println("bounce mode"); 
          i++;
          continue;
        } 
        if (paramArrayOfString[i].equals("-h")) {
          printUsage(System.out);
          return;
        } 
        if (paramArrayOfString[i].equals("-version")) {
          System.out.println("xvibs version 17m2");
          return;
        } 
        if (paramArrayOfString[i].equals("-frames")) {
          if (++i >= paramArrayOfString.length)
            throw new Error("-frames requires an argument"); 
          try {
            numberFrames = Integer.parseInt(paramArrayOfString[i]);
            if (numberFrames < 0)
              throw new Error("invalid -frames argument. Must be 0 or a positive integer"); 
          } catch (NumberFormatException numberFormatException) {
            throw new Error("invalid -frames argument. Must be 0 or a positive integer");
          } 
          i++;
          if (debugging)
            System.err.println(String.valueOf(numberFrames) + " frames"); 
          continue;
        } 
        if (paramArrayOfString[i].equals("-amplitude")) {
          if (++i >= paramArrayOfString.length)
            throw new Error("-amplitude requires an argument"); 
          try {
            freqScale = Double.parseDouble(paramArrayOfString[i]);
          } catch (NumberFormatException numberFormatException) {
            throw new Error("invalid -amplitude argument. Must be a floating-point number");
          } 
          i++;
          if (debugging)
            System.err.println(String.valueOf(freqScale) + " amplitude"); 
          continue;
        } 
        if (paramArrayOfString[i].equals("-list")) {
          if (++i >= paramArrayOfString.length)
            throw new Error("-list requires an argument"); 
          listFileName = paramArrayOfString[i];
          i++;
          if (debugging)
            System.err.println(String.valueOf(listFileName) + " list file"); 
          continue;
        } 
        break;
      } 
      int j = 0;
      boolean bool = false;
      String str1 = "";
      if (paramArrayOfString.length - i < 2) {
        System.out.println("Insufficient arguments. Using interactive mode.");
        System.out.println();
        System.out.println("xvibs version 17m2,\n Copyright (C) 1999, 2000  Bradley A. Smith,\n Copyright (C) 2007, 2010  Kun Attila-Zsolt ");
        System.out.println("xvibs comes with ABSOLUTELY NO WARRANTY; for details type `show w'.");
        System.out.println("This is free software, and you are welcome to redistribute it\nunder certain conditions; type `show c' for details.");
        System.out.println();
        try {
          BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
          System.out.print("Input file? ");
          String str = bufferedReader.readLine();
          str1 = str.trim();
          if (str1.length() == 0)
            throw new Error("invalid input file name"); 
          if (str1.equals("show w")) {
            showWarranty(System.out);
            return;
          } 
          if (str1.equals("show c")) {
            showCopying(System.out);
            return;
          } 
          System.out.println("Input from " + str1);
          System.out.print("Vibration number [all]? ");
          str = bufferedReader.readLine();
          if (str.length() == 0 || str.equals("all")) {
            bool = true;
          } else {
            bool = false;
            try {
              j = Integer.parseInt(str) - 1;
            } catch (Exception exception) {
              j = -1;
            } 
          } 
          if (j < 0)
            throw new Error("Invalid vibration number. Must be a positive integer."); 
          System.out.print("Generating ");
          if (bool) {
            System.out.println("all frequencies");
          } else {
            System.out.println("frequency " + (j + 1));
          } 
          System.out.print("Number of frames [" + numberFrames + "]? ");
          if (numberFrames == 0)
            System.out.println("Generating Single file with all frequencies for Jmol 10."); 
          str = bufferedReader.readLine();
          if (str.length() > 0)
            numberFrames = Integer.parseInt(str); 
          if (numberFrames < 0)
            throw new Error("Invalid number of frames. Must be 0 or a positive integer."); 
          System.out.println("Generating " + numberFrames + " frames");
          System.out.print("Generate for loop or bounce animation [loop]? ");
          str = bufferedReader.readLine();
          if (str.length() > 0 && (str.charAt(0) == 'B' || str.charAt(0) == 'b'))
            byBounce = true; 
          System.out.print("Generating ");
          if (byBounce) {
            System.out.print("bounce");
          } else {
            System.out.print("loop");
          } 
          System.out.println(" animations");
          System.out.print("Frequency amplitude [" + freqScale + "]? ");
          str = bufferedReader.readLine();
          if (str.length() > 0)
            freqScale = Double.parseDouble(str); 
          System.out.println("Amplitude " + freqScale);
        } catch (IOException iOException) {
          throw new Error("Error reading user input: " + iOException);
        } 
      } else {
        str1 = paramArrayOfString[i].trim();
        if (paramArrayOfString[++i].equals("all")) {
          bool = true;
        } else {
          j = Integer.parseInt(paramArrayOfString[i]) - 1;
        } 
      } 
      if (debugging)
        System.err.println("input file: " + str1); 
      if (str1.length() == 0)
        throw new Error("invalid input file name"); 
      FileReader fileReader = null;
      try {
        fileReader = new FileReader(str1);
      } catch (FileNotFoundException fileNotFoundException) {
        throw new Error("unable to open '" + str1 + "' for input");
      } 
      String str2 = str1.substring(0, str1.lastIndexOf('.') + 1);
      if (debugging)
        System.err.println("output base: " + str2); 
      MoleculeReader moleculeReader = ReaderFactory.createReader(fileReader);
      if (debugging) {
        System.err.print("input file type: ");
        if (moleculeReader instanceof Gaussian98Reader) {
          System.err.println("Gaussian98");
        } else if (moleculeReader instanceof Gaussian94Reader) {
          System.err.println("Gaussian94");
        } else if (moleculeReader instanceof Gaussian92Reader) {
          System.err.println("Gaussian92");
        } else if (moleculeReader instanceof GamessReader) {
          System.err.println("Gamess");
        } else if (moleculeReader instanceof Aces2Reader) {
          System.err.println("Aces2");
        } else if (moleculeReader instanceof ADFReader) {
          System.err.println("ADF");
        } else if (moleculeReader instanceof MopacReader) {
          System.err.println("Mopac");
        } else if (moleculeReader instanceof HyperchemReader) {
          System.err.println("Hyperchem");
        } else if (moleculeReader instanceof SpartanReader) {
          System.err.println("Spartan");
        } else {
          System.err.println("unknown");
        } 
      } 
      if (moleculeReader == null)
        throw new Error("unknown input file type"); 
      Molecule molecule = new Molecule();
      try {
        moleculeReader.read(molecule);
      } catch (Exception exception) {
        System.err.println(exception);
        if (debugging)
          exception.printStackTrace(); 
      } 
      if (debugging) {
        System.err.println(String.valueOf(molecule.getNumberAtoms()) + " atoms and " + molecule.getNumberFrequencies() + " frequencies read.");
        System.err.println("Energy: " + molecule.energy);
        System.err.println("Atoms:");
        DecimalFormat decimalFormat4 = new DecimalFormat("0.000000", decimalSymbols);
        DecimalFormat decimalFormat5 = new DecimalFormat("0.00", decimalSymbols);
        Enumeration enumeration = molecule.getFrequencies();
        while (enumeration.hasMoreElements()) {
          Enumeration enumeration1 = molecule.getAtoms();
          Frequency frequency = (Frequency)enumeration.nextElement();
          Enumeration enumeration2 = frequency.getVectors();
          System.err.println(molecule.getNumberAtoms());
          System.err.println("Energy: " + molecule.energy + "  Freq: " + frequency.value);
          while (enumeration1.hasMoreElements() && enumeration2.hasMoreElements()) {
            Atom atom = (Atom)enumeration1.nextElement();
            Vector3d vector3d = (Vector3d)enumeration2.nextElement();
            System.err.print(atom.atomicNumber);
            System.err.print(' ');
            String str = decimalFormat4.format(atom.position.x);
            byte b;
            for (b = 0; b < 10 - str.length(); b++)
              System.err.print(' '); 
            System.err.print(str);
            str = decimalFormat4.format(atom.position.y);
            for (b = 0; b < 10 - str.length(); b++)
              System.err.print(' '); 
            System.err.print(str);
            str = decimalFormat4.format(atom.position.z);
            for (b = 0; b < 10 - str.length(); b++)
              System.err.print(' '); 
            System.err.print(str);
            System.err.print("  ");
            str = decimalFormat5.format(vector3d.x);
            for (b = 0; b < 5 - str.length(); b++)
              System.err.print(' '); 
            System.err.print(str);
            System.err.print(' ');
            str = decimalFormat5.format(vector3d.y);
            for (b = 0; b < 5 - str.length(); b++)
              System.err.print(' '); 
            System.err.print(str);
            System.err.print(' ');
            str = decimalFormat5.format(vector3d.z);
            for (b = 0; b < 5 - str.length(); b++)
              System.err.print(' '); 
            System.err.print(str);
            System.err.println();
          } 
        } 
      } 
      if (molecule.getNumberFrequencies() <= 0)
        throw new Error("no frequencies found"); 
      if (bool) {
        k = 0;
        m = molecule.getNumberFrequencies();
      } else {
        if (j > molecule.getNumberFrequencies()) {
          System.err.println("Error: requested frequency is greater than number of frequencies found, " + molecule.getNumberFrequencies());
          return;
        } 
        k = j;
        m = j + 1;
      } 
      DecimalFormat decimalFormat1 = new DecimalFormat("000", decimalSymbols);
      DecimalFormat decimalFormat2 = new DecimalFormat("000.000", decimalSymbols);
      DecimalFormat decimalFormat3 = new DecimalFormat("0000.000", decimalSymbols);
      Vector vector = new Vector();
      if (numberFrames == 0) {
        PrintWriter printWriter;
        System.out.println("Generating single file containing all frequencies for Frames = 0");
        String str = String.valueOf(str2) + "all.xyz";
        try {
          printWriter = new PrintWriter(new FileWriter(str));
        } catch (IOException iOException) {
          System.err.println(iOException);
          return;
        } 
        for (int n = m - 1; n >= k; n--) {
          Vector vector1 = molecule.vibration(n, 1, freqScale, false);
          if (listFileName != null) {
            String str3;
            if ((molecule.getFrequency(n)).value > 1000.0D) {
              str3 = decimalFormat3.format((molecule.getFrequency(n)).value);
            } else {
              str3 = decimalFormat2.format((molecule.getFrequency(n)).value);
            } 
            vector.addElement(str3);
          } 
          Enumeration enumeration = vector1.elements();
          while (enumeration.hasMoreElements()) {
            Molecule molecule1 = (Molecule)enumeration.nextElement();
            printWriter.println(molecule1.getNumberAtoms());
            printWriter.println(String.valueOf(m - n) + "  Energy: " + molecule1.energy + "  Freq: " + (molecule.getFrequency(n)).value);
            for (byte b = 0; b < molecule1.getNumberAtoms(); b++) {
              Atom atom = molecule1.getAtom(b);
              writeAtom(printWriter, atom, molecule.getFrequency(n).getVector(b), vectorScale);
            } 
          } 
        } 
        printWriter.close();
      } else {
        for (int n = k; n < m; n++) {
          PrintWriter printWriter;
          String str;
          if (useFreqInName) {
            str = String.valueOf(str2) + decimalFormat3.format((molecule.getFrequency(n)).value).replace('.', '_') + ".xyz";
          } else {
            str = String.valueOf(str2) + decimalFormat1.format((n + 1)) + ".xyz";
          } 
          if (listFileName != null)
            vector.addElement(str); 
          try {
            printWriter = new PrintWriter(new FileWriter(str));
          } catch (IOException iOException) {
            System.err.println(iOException);
            return;
          } 
          Vector vector1 = molecule.vibration(n, numberFrames, freqScale, byBounce);
          Enumeration enumeration = vector1.elements();
          while (enumeration.hasMoreElements()) {
            Molecule molecule1 = (Molecule)enumeration.nextElement();
            printWriter.println(molecule1.getNumberAtoms());
            printWriter.println("Energy: " + molecule1.energy + "  Freq: " + (molecule.getFrequency(n)).value);
            for (byte b = 0; b < molecule1.getNumberAtoms(); b++) {
              Atom atom = molecule1.getAtom(b);
              writeAtom(printWriter, atom, molecule.getFrequency(n).getVector(b), vectorScale);
            } 
          } 
          printWriter.close();
        } 
      } 
      if (listFileName != null) {
        PrintWriter printWriter;
        try {
          printWriter = new PrintWriter(new FileWriter(listFileName));
        } catch (IOException iOException) {
          System.err.println(iOException);
          return;
        } 
        if (numberFrames == 0) {
          printWriter.print("var freqVals = \"");
        } else {
          printWriter.print("var xyzfiles = \"");
        } 
        for (byte b = 0; b < vector.size() - 1; b++) {
          printWriter.print(vector.elementAt(b));
          printWriter.print(',');
          if ((b + 1) % 5 == 0) {
            printWriter.println('"');
            printWriter.print(" + \"");
          } 
        } 
        printWriter.print(vector.elementAt(vector.size() - 1));
        printWriter.print("\";");
        printWriter.close();
      } 
    } catch (Error error) {
      System.err.println("xvibs: " + error.getMessage());
      printUsage(System.err);
    } 
  }
  
  static void writeAtom(PrintWriter paramPrintWriter, Atom paramAtom, Vector3d paramVector3d, double paramDouble) {
    DecimalFormat decimalFormat = new DecimalFormat("0.000000", decimalSymbols);
    paramPrintWriter.print(padRight(AtomicSymbol.atomicNumberToSymbol(paramAtom.atomicNumber), ' ', 2));
    paramPrintWriter.print(' ');
    paramPrintWriter.print(padLeft(decimalFormat.format(paramAtom.position.x), ' ', 11));
    paramPrintWriter.print(' ');
    paramPrintWriter.print(padLeft(decimalFormat.format(paramAtom.position.y), ' ', 11));
    paramPrintWriter.print(' ');
    paramPrintWriter.print(padLeft(decimalFormat.format(paramAtom.position.z), ' ', 11));
    paramPrintWriter.print(' ');
    paramPrintWriter.print(padLeft(decimalFormat.format(paramVector3d.x * paramDouble), ' ', 11));
    paramPrintWriter.print(' ');
    paramPrintWriter.print(padLeft(decimalFormat.format(paramVector3d.y * paramDouble), ' ', 11));
    paramPrintWriter.print(' ');
    paramPrintWriter.print(padLeft(decimalFormat.format(paramVector3d.z * paramDouble), ' ', 11));
    paramPrintWriter.println();
  }
  
  static String padLeft(String paramString, char paramChar, int paramInt) {
    StringBuffer stringBuffer = new StringBuffer();
    for (int i = paramString.length(); i < paramInt; i++)
      stringBuffer.append(paramChar); 
    stringBuffer.append(paramString);
    return stringBuffer.toString();
  }
  
  public static String padRight(String paramString, char paramChar, int paramInt) {
    StringBuffer stringBuffer = new StringBuffer(paramString);
    for (int i = stringBuffer.length(); i < paramInt; i++)
      stringBuffer.append(paramChar); 
    return stringBuffer.toString();
  }
  
  static void printUsage(PrintStream paramPrintStream) {
    paramPrintStream.println("Usage: java xvibs [-h] [-version] [-useFreqInName] [-bounce] [-frames n] [-amplitude f] [-list listFile] file frequency_number");
    paramPrintStream.println("  -useFreqInName  produce files numbered by frequency value rather");
    paramPrintStream.println("                  than frequency number (default: " + defaultUseFreqInName + ")");
    paramPrintStream.println("  -bounce         produce bouncing animations (default: " + defaultByBounce + ")");
    paramPrintStream.println("  -frames         output n frames (default: " + defaultNumberFrames + ")");
    paramPrintStream.println("  -amplitude      scale frequencies by f (default: " + defaultFreqScale + ")");
    paramPrintStream.println("  -list           output a Javascript list of the generated");
    paramPrintStream.println("                  files to the given listFile (default: null)");
  }
  
  static void showWarranty(PrintStream paramPrintStream) {
    paramPrintStream.println("                    GNU GENERAL PUBLIC LICENSE");
    paramPrintStream.println("                            NO WARRANTY");
    paramPrintStream.println();
    paramPrintStream.println("  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY");
    paramPrintStream.println("FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN");
    paramPrintStream.println("OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES");
    paramPrintStream.println("PROVIDE THE PROGRAM \"AS IS\" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED");
    paramPrintStream.println("OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF");
    paramPrintStream.println("MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS");
    paramPrintStream.println("TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE");
    paramPrintStream.println("PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,");
    paramPrintStream.println("REPAIR OR CORRECTION.");
    paramPrintStream.println();
    paramPrintStream.println("  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING");
    paramPrintStream.println("WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR");
    paramPrintStream.println("REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,");
    paramPrintStream.println("INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING");
    paramPrintStream.println("OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED");
    paramPrintStream.println("TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY");
    paramPrintStream.println("YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER");
    paramPrintStream.println("PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE");
    paramPrintStream.println("POSSIBILITY OF SUCH DAMAGES.");
  }
  
  static void showCopying(PrintStream paramPrintStream) {
    paramPrintStream.println("                    GNU GENERAL PUBLIC LICENSE");
    paramPrintStream.println("   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION");
    paramPrintStream.println();
    paramPrintStream.println("  0. This License applies to any program or other work which contains");
    paramPrintStream.println("a notice placed by the copyright holder saying it may be distributed");
    paramPrintStream.println("under the terms of this General Public License.  The \"Program\", below,");
    paramPrintStream.println("refers to any such program or work, and a \"work based on the Program\"");
    paramPrintStream.println("means either the Program or any derivative work under copyright law:");
    paramPrintStream.println("that is to say, a work containing the Program or a portion of it,");
    paramPrintStream.println("either verbatim or with modifications and/or translated into another");
    paramPrintStream.println("language.  (Hereinafter, translation is included without limitation in");
    paramPrintStream.println("the term \"modification\".)  Each licensee is addressed as \"you\".");
    paramPrintStream.println();
    paramPrintStream.println("Activities other than copying, distribution and modification are not");
    paramPrintStream.println("covered by this License; they are outside its scope.  The act of");
    paramPrintStream.println("running the Program is not restricted, and the output from the Program");
    paramPrintStream.println("is covered only if its contents constitute a work based on the");
    paramPrintStream.println("Program (independent of having been made by running the Program).");
    paramPrintStream.println("Whether that is true depends on what the Program does.");
    paramPrintStream.println();
    paramPrintStream.println("  1. You may copy and distribute verbatim copies of the Program's");
    paramPrintStream.println("source code as you receive it, in any medium, provided that you");
    paramPrintStream.println("conspicuously and appropriately publish on each copy an appropriate");
    paramPrintStream.println("copyright notice and disclaimer of warranty; keep intact all the");
    paramPrintStream.println("notices that refer to this License and to the absence of any warranty;");
    paramPrintStream.println("and give any other recipients of the Program a copy of this License");
    paramPrintStream.println("along with the Program.");
    paramPrintStream.println();
    paramPrintStream.println("You may charge a fee for the physical act of transferring a copy, and");
    paramPrintStream.println("you may at your option offer warranty protection in exchange for a fee.");
    paramPrintStream.println();
    paramPrintStream.println("  2. You may modify your copy or copies of the Program or any portion");
    paramPrintStream.println("of it, thus forming a work based on the Program, and copy and");
    paramPrintStream.println("distribute such modifications or work under the terms of Section 1");
    paramPrintStream.println("above, provided that you also meet all of these conditions:");
    paramPrintStream.println();
    paramPrintStream.println("    a) You must cause the modified files to carry prominent notices");
    paramPrintStream.println("    stating that you changed the files and the date of any change.");
    paramPrintStream.println();
    paramPrintStream.println("    b) You must cause any work that you distribute or publish, that in");
    paramPrintStream.println("    whole or in part contains or is derived from the Program or any");
    paramPrintStream.println("    part thereof, to be licensed as a whole at no charge to all third");
    paramPrintStream.println("    parties under the terms of this License.");
    paramPrintStream.println();
    paramPrintStream.println("    c) If the modified program normally reads commands interactively");
    paramPrintStream.println("    when run, you must cause it, when started running for such");
    paramPrintStream.println("    interactive use in the most ordinary way, to print or display an");
    paramPrintStream.println("    announcement including an appropriate copyright notice and a");
    paramPrintStream.println("    notice that there is no warranty (or else, saying that you provide");
    paramPrintStream.println("    a warranty) and that users may redistribute the program under");
    paramPrintStream.println("    these conditions, and telling the user how to view a copy of this");
    paramPrintStream.println("    License.  (Exception: if the Program itself is interactive but");
    paramPrintStream.println("    does not normally print such an announcement, your work based on");
    paramPrintStream.println("    the Program is not required to print an announcement.)");
    paramPrintStream.println();
    paramPrintStream.println("These requirements apply to the modified work as a whole.  If");
    paramPrintStream.println("identifiable sections of that work are not derived from the Program,");
    paramPrintStream.println("and can be reasonably considered independent and separate works in");
    paramPrintStream.println("themselves, then this License, and its terms, do not apply to those");
    paramPrintStream.println("sections when you distribute them as separate works.  But when you");
    paramPrintStream.println("distribute the same sections as part of a whole which is a work based");
    paramPrintStream.println("on the Program, the distribution of the whole must be on the terms of");
    paramPrintStream.println("this License, whose permissions for other licensees extend to the");
    paramPrintStream.println("entire whole, and thus to each and every part regardless of who wrote it.");
    paramPrintStream.println();
    paramPrintStream.println("Thus, it is not the intent of this section to claim rights or contest");
    paramPrintStream.println("your rights to work written entirely by you; rather, the intent is to");
    paramPrintStream.println("exercise the right to control the distribution of derivative or");
    paramPrintStream.println("collective works based on the Program.");
    paramPrintStream.println();
    paramPrintStream.println("In addition, mere aggregation of another work not based on the Program");
    paramPrintStream.println("with the Program (or with a work based on the Program) on a volume of");
    paramPrintStream.println("a storage or distribution medium does not bring the other work under");
    paramPrintStream.println("the scope of this License.");
    paramPrintStream.println();
    paramPrintStream.println("  3. You may copy and distribute the Program (or a work based on it,");
    paramPrintStream.println("under Section 2) in object code or executable form under the terms of");
    paramPrintStream.println("Sections 1 and 2 above provided that you also do one of the following:");
    paramPrintStream.println();
    paramPrintStream.println("    a) Accompany it with the complete corresponding machine-readable");
    paramPrintStream.println("    source code, which must be distributed under the terms of Sections");
    paramPrintStream.println("    1 and 2 above on a medium customarily used for software interchange; or,");
    paramPrintStream.println();
    paramPrintStream.println("    b) Accompany it with a written offer, valid for at least three");
    paramPrintStream.println("    years, to give any third party, for a charge no more than your");
    paramPrintStream.println("    cost of physically performing source distribution, a complete");
    paramPrintStream.println("    machine-readable copy of the corresponding source code, to be");
    paramPrintStream.println("    distributed under the terms of Sections 1 and 2 above on a medium");
    paramPrintStream.println("    customarily used for software interchange; or,");
    paramPrintStream.println();
    paramPrintStream.println("    c) Accompany it with the information you received as to the offer");
    paramPrintStream.println("    to distribute corresponding source code.  (This alternative is");
    paramPrintStream.println("    allowed only for noncommercial distribution and only if you");
    paramPrintStream.println("    received the program in object code or executable form with such");
    paramPrintStream.println("    an offer, in accord with Subsection b above.)");
    paramPrintStream.println();
    paramPrintStream.println("The source code for a work means the preferred form of the work for");
    paramPrintStream.println("making modifications to it.  For an executable work, complete source");
    paramPrintStream.println("code means all the source code for all modules it contains, plus any");
    paramPrintStream.println("associated interface definition files, plus the scripts used to");
    paramPrintStream.println("control compilation and installation of the executable.  However, as a");
    paramPrintStream.println("special exception, the source code distributed need not include");
    paramPrintStream.println("anything that is normally distributed (in either source or binary");
    paramPrintStream.println("form) with the major components (compiler, kernel, and so on) of the");
    paramPrintStream.println("operating system on which the executable runs, unless that component");
    paramPrintStream.println("itself accompanies the executable.");
    paramPrintStream.println();
    paramPrintStream.println("If distribution of executable or object code is made by offering");
    paramPrintStream.println("access to copy from a designated place, then offering equivalent");
    paramPrintStream.println("access to copy the source code from the same place counts as");
    paramPrintStream.println("distribution of the source code, even though third parties are not");
    paramPrintStream.println("compelled to copy the source along with the object code.");
    paramPrintStream.println();
    paramPrintStream.println("  4. You may not copy, modify, sublicense, or distribute the Program");
    paramPrintStream.println("except as expressly provided under this License.  Any attempt");
    paramPrintStream.println("otherwise to copy, modify, sublicense or distribute the Program is");
    paramPrintStream.println("void, and will automatically terminate your rights under this License.");
    paramPrintStream.println("However, parties who have received copies, or rights, from you under");
    paramPrintStream.println("this License will not have their licenses terminated so long as such");
    paramPrintStream.println("parties remain in full compliance.");
    paramPrintStream.println();
    paramPrintStream.println("  5. You are not required to accept this License, since you have not");
    paramPrintStream.println("signed it.  However, nothing else grants you permission to modify or");
    paramPrintStream.println("distribute the Program or its derivative works.  These actions are");
    paramPrintStream.println("prohibited by law if you do not accept this License.  Therefore, by");
    paramPrintStream.println("modifying or distributing the Program (or any work based on the");
    paramPrintStream.println("Program), you indicate your acceptance of this License to do so, and");
    paramPrintStream.println("all its terms and conditions for copying, distributing or modifying");
    paramPrintStream.println("the Program or works based on it.");
    paramPrintStream.println();
    paramPrintStream.println("  6. Each time you redistribute the Program (or any work based on the");
    paramPrintStream.println("Program), the recipient automatically receives a license from the");
    paramPrintStream.println("original licensor to copy, distribute or modify the Program subject to");
    paramPrintStream.println("these terms and conditions.  You may not impose any further");
    paramPrintStream.println("restrictions on the recipients' exercise of the rights granted herein.");
    paramPrintStream.println("You are not responsible for enforcing compliance by third parties to");
    paramPrintStream.println("this License.");
    paramPrintStream.println();
    paramPrintStream.println("  7. If, as a consequence of a court judgment or allegation of patent");
    paramPrintStream.println("infringement or for any other reason (not limited to patent issues),");
    paramPrintStream.println("conditions are imposed on you (whether by court order, agreement or");
    paramPrintStream.println("otherwise) that contradict the conditions of this License, they do not");
    paramPrintStream.println("excuse you from the conditions of this License.  If you cannot");
    paramPrintStream.println("distribute so as to satisfy simultaneously your obligations under this");
    paramPrintStream.println("License and any other pertinent obligations, then as a consequence you");
    paramPrintStream.println("may not distribute the Program at all.  For example, if a patent");
    paramPrintStream.println("license would not permit royalty-free redistribution of the Program by");
    paramPrintStream.println("all those who receive copies directly or indirectly through you, then");
    paramPrintStream.println("the only way you could satisfy both it and this License would be to");
    paramPrintStream.println("refrain entirely from distribution of the Program.");
    paramPrintStream.println();
    paramPrintStream.println("If any portion of this section is held invalid or unenforceable under");
    paramPrintStream.println("any particular circumstance, the balance of the section is intended to");
    paramPrintStream.println("apply and the section as a whole is intended to apply in other");
    paramPrintStream.println("circumstances.");
    paramPrintStream.println();
    paramPrintStream.println("It is not the purpose of this section to induce you to infringe any");
    paramPrintStream.println("patents or other property right claims or to contest validity of any");
    paramPrintStream.println("such claims; this section has the sole purpose of protecting the");
    paramPrintStream.println("integrity of the free software distribution system, which is");
    paramPrintStream.println("implemented by public license practices.  Many people have made");
    paramPrintStream.println("generous contributions to the wide range of software distributed");
    paramPrintStream.println("through that system in reliance on consistent application of that");
    paramPrintStream.println("system; it is up to the author/donor to decide if he or she is willing");
    paramPrintStream.println("to distribute software through any other system and a licensee cannot");
    paramPrintStream.println("impose that choice.");
    paramPrintStream.println();
    paramPrintStream.println("This section is intended to make thoroughly clear what is believed to");
    paramPrintStream.println("be a consequence of the rest of this License.");
    paramPrintStream.println("");
    paramPrintStream.println("  8. If the distribution and/or use of the Program is restricted in");
    paramPrintStream.println("certain countries either by patents or by copyrighted interfaces, the");
    paramPrintStream.println("original copyright holder who places the Program under this License");
    paramPrintStream.println("may add an explicit geographical distribution limitation excluding");
    paramPrintStream.println("those countries, so that distribution is permitted only in or among");
    paramPrintStream.println("countries not thus excluded.  In such case, this License incorporates");
    paramPrintStream.println("the limitation as if written in the body of this License.");
    paramPrintStream.println();
    paramPrintStream.println("  9. The Free Software Foundation may publish revised and/or new versions");
    paramPrintStream.println("of the General Public License from time to time.  Such new versions will");
    paramPrintStream.println("be similar in spirit to the present version, but may differ in detail to");
    paramPrintStream.println("address new problems or concerns.");
    paramPrintStream.println();
    paramPrintStream.println("Each version is given a distinguishing version number.  If the Program");
    paramPrintStream.println("specifies a version number of this License which applies to it and \"any");
    paramPrintStream.println("later version\", you have the option of following the terms and conditions");
    paramPrintStream.println("either of that version or of any later version published by the Free");
    paramPrintStream.println("Software Foundation.  If the Program does not specify a version number of");
    paramPrintStream.println("this License, you may choose any version ever published by the Free Software");
    paramPrintStream.println("Foundation.");
    paramPrintStream.println();
    paramPrintStream.println("  10. If you wish to incorporate parts of the Program into other free");
    paramPrintStream.println("programs whose distribution conditions are different, write to the author");
    paramPrintStream.println("to ask for permission.  For software which is copyrighted by the Free");
    paramPrintStream.println("Software Foundation, write to the Free Software Foundation; we sometimes");
    paramPrintStream.println("make exceptions for this.  Our decision will be guided by the two goals");
    paramPrintStream.println("of preserving the free status of all derivatives of our free software and");
    paramPrintStream.println("of promoting the sharing and reuse of software generally.");
  }
}