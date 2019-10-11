import java.io.BufferedReader;
import java.io.IOException;
import java.io.Reader;

class ReaderFactory {
  static MoleculeReader createReader(Reader paramReader) {
    BufferedReader bufferedReader = new BufferedReader(paramReader);
    try {
      while (bufferedReader.ready()) {
        String str = bufferedReader.readLine();
        if (str.indexOf("Gaussian 09:") >= 0)
          return new Gaussian09Reader(bufferedReader); 
        if (str.indexOf("Gaussian 03:") >= 0)
          return new Gaussian03Reader(bufferedReader); 
        if (str.indexOf("Gaussian 98:") >= 0)
          return new Gaussian98Reader(bufferedReader); 
        if (str.indexOf("Gaussian 95:") >= 0)
          return new Gaussian94Reader(bufferedReader); 
        if (str.indexOf("Gaussian 94:") >= 0)
          return new Gaussian94Reader(bufferedReader); 
        if (str.indexOf("Gaussian 92:") >= 0)
          return new Gaussian92Reader(bufferedReader); 
        if (str.indexOf("Gaussian G90") >= 0)
          return new Gaussian90Reader(bufferedReader); 
        if (str.indexOf("GAMESS") >= 0)
          return new GamessReader(bufferedReader); 
        if (str.indexOf("ACES2") >= 0)
          return new Aces2Reader(bufferedReader); 
        if (str.indexOf("Amsterdam Density Functional") >= 0)
          return new ADFReader(bufferedReader); 
        if (str.indexOf("DALTON") >= 0)
          return new DaltonReader(bufferedReader); 
        if (str.indexOf("Jaguar") >= 0)
          return new JaguarReader(bufferedReader); 
        if (str.indexOf("MOPAC") >= 0)
          return new MopacReader(bufferedReader); 
        if (str.indexOf("HyperChem") >= 0)
          return new HyperchemReader(bufferedReader); 
        if (str.indexOf("SPARTAN SEMIEMPIRICAL PROGRAM") >= 0)
          return new SpartanReader(bufferedReader); 
      } 
    } catch (IOException iOException) {
      System.err.println(iOException);
    } 
    return null;
  }
}
