import java.io.BufferedReader;
import java.io.IOException;
import java.io.Reader;
import java.io.StreamTokenizer;
import java.io.StringReader;
import java.util.Vector;

class HyperchemReader implements MoleculeReader {
  BufferedReader input;
  
  public HyperchemReader(Reader paramReader) { this.input = new BufferedReader(paramReader); }
  
  public void read(Molecule paramMolecule) throws Exception {
    while (this.input.ready()) {
      String str = this.input.readLine();
      if (str.indexOf("Total Energy") >= 0) {
        paramMolecule.energy = toEnergy(str);
        continue;
      } 
      if (str.indexOf("Coordinates(Angstrom)") >= 0) {
        str = this.input.readLine();
        readCoordinates(paramMolecule);
        continue;
      } 
      if (str.indexOf("Frequencies of the Normal Modes") >= 0) {
        for (byte b = 0; b < 3; b++)
          str = this.input.readLine(); 
        readFrequencies(paramMolecule);
        break;
      } 
    } 
  }
  
  double toEnergy(String paramString) throws Exception {
    double d = 0.0D;
    StringReader stringReader = new StringReader(paramString);
    StreamTokenizer streamTokenizer = new StreamTokenizer(stringReader);
    for (byte b = 0; b < 3; b++)
      streamTokenizer.nextToken(); 
    if (streamTokenizer.nextToken() == -2) {
      d = streamTokenizer.nval;
    } else {
      throw new Exception("Error reading energy");
    } 
    return d;
  }
  
  void readCoordinates(Molecule paramMolecule) throws Exception {
    paramMolecule.removeAtoms();
    while (this.input.ready()) {
      String str = readLine();
      if (str.trim().length() == 0)
        break; 
      Atom atom = new Atom();
      StringReader stringReader = new StringReader(str);
      StreamTokenizer streamTokenizer = new StreamTokenizer(stringReader);
      streamTokenizer.nextToken();
      if (streamTokenizer.nextToken() == -2) {
        atom.atomicNumber = (int)streamTokenizer.nval;
      } else {
        throw new Exception("Error reading coordinates");
      } 
      streamTokenizer.nextToken();
      atom.position = new Point3d();
      if (streamTokenizer.nextToken() == -2) {
        atom.position.x = streamTokenizer.nval;
      } else {
        throw new Exception("Error reading coordinates");
      } 
      if (streamTokenizer.nextToken() == -2) {
        atom.position.y = streamTokenizer.nval;
      } else {
        throw new Exception("Error reading coordinates");
      } 
      if (streamTokenizer.nextToken() == -2) {
        atom.position.z = streamTokenizer.nval;
      } else {
        throw new Exception("Error reading coordinates");
      } 
      paramMolecule.addAtom(atom);
    } 
  }
  
  void readFrequencies(Molecule paramMolecule) throws Exception {
    paramMolecule.removeFrequencies();
    String str = readLine();
    while (str != null && str.indexOf("Mode") >= 0) {
      str = readLine();
      str = readLine();
      StringReader stringReader = new StringReader(str.trim());
      StreamTokenizer streamTokenizer = new StreamTokenizer(stringReader);
      streamTokenizer.nextToken();
      Vector vector = new Vector();
      while (streamTokenizer.nextToken() != -1) {
        Frequency frequency = new Frequency();
        frequency.value = streamTokenizer.nval;
        vector.addElement(frequency);
      } 
      Frequency[] arrayOfFrequency = new Frequency[vector.size()];
      vector.copyInto(arrayOfFrequency);
      Vector3d[] arrayOfVector3d = new Vector3d[arrayOfFrequency.length];
      str = readLine();
      byte b1;
      for (b1 = 0; b1 < paramMolecule.getNumberAtoms(); b1++) {
        str = readLine();
        str = str.substring(8);
        StringReader stringReader1 = new StringReader(str);
        streamTokenizer = new StreamTokenizer(stringReader1);
        byte b2;
        for (b2 = 0; b2 < arrayOfFrequency.length; b2++) {
          arrayOfVector3d[b2] = new Vector3d();
          if (streamTokenizer.nextToken() == -2) {
            (arrayOfVector3d[b2]).x = streamTokenizer.nval;
          } else {
            throw new Exception("Error reading frequencies");
          } 
        } 
        str = readLine();
        str = str.substring(8);
        stringReader1 = new StringReader(str);
        streamTokenizer = new StreamTokenizer(stringReader1);
        for (b2 = 0; b2 < arrayOfFrequency.length; b2++) {
          if (streamTokenizer.nextToken() == -2) {
            (arrayOfVector3d[b2]).y = streamTokenizer.nval;
          } else {
            throw new Exception("Error reading frequencies");
          } 
        } 
        str = readLine();
        str = str.substring(8);
        stringReader1 = new StringReader(str);
        streamTokenizer = new StreamTokenizer(stringReader1);
        for (b2 = 0; b2 < arrayOfFrequency.length; b2++) {
          if (streamTokenizer.nextToken() == -2) {
            (arrayOfVector3d[b2]).z = streamTokenizer.nval;
          } else {
            throw new Exception("Error reading frequencies");
          } 
          arrayOfFrequency[b2].addVector(arrayOfVector3d[b2]);
        } 
      } 
      for (b1 = 0; b1 < arrayOfFrequency.length; b1++)
        paramMolecule.addFrequency(arrayOfFrequency[b1]); 
      for (b1 = 0; b1 < 5; b1++) {
        str = readLine();
        if (str == null || str.trim().length() > 0 || str.indexOf("Mode") >= 0)
          break; 
      } 
    } 
    for (byte b = 0; b < 6; b++)
      paramMolecule.removeFrequency(paramMolecule.getNumberFrequencies() - 1); 
  }
  
  private String readLine() throws IOException {
    for (String str = this.input.readLine(); str != null && str.length() > 0 && Character.isDigit(str.charAt(0)); str = this.input.readLine());
    return str;
  }
}

