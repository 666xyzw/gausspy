import java.io.BufferedReader;
import java.io.Reader;
import java.io.StreamTokenizer;
import java.io.StringReader;
import java.util.Vector;

class JaguarReader implements MoleculeReader {
  BufferedReader input;
  
  public JaguarReader(Reader paramReader) { this.input = new BufferedReader(paramReader); }
  
  public void read(Molecule paramMolecule) throws Exception {
    while (this.input.ready()) {
      String str = this.input.readLine();
      if (str.indexOf("SCF energy:") >= 0) {
        paramMolecule.energy = toEnergy(str);
        continue;
      } 
      if (str.indexOf("Input geometry:") >= 0) {
        str = this.input.readLine();
        str = this.input.readLine();
        readCoordinates(paramMolecule);
        continue;
      } 
      if (str.indexOf("harmonic frequencies in cm") >= 0) {
        str = this.input.readLine();
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
    for (byte b = 0; b < 6; b++)
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
      String str = this.input.readLine();
      if (str.trim().length() == 0)
        break; 
      Atom atom = new Atom();
      StringReader stringReader = new StringReader(str);
      StreamTokenizer streamTokenizer = new StreamTokenizer(stringReader);
      if (streamTokenizer.nextToken() == -3) {
        atom.atomicNumber = atomLabelToAtomicNumber(streamTokenizer.sval);
      } else {
        throw new Exception("Error reading coordinates");
      } 
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
  
  static int atomLabelToAtomicNumber(String paramString) {
    StringBuffer stringBuffer = new StringBuffer();
    for (byte b = 0; b < paramString.length() && Character.isLetter(paramString.charAt(b)); b++)
      stringBuffer.append(paramString.charAt(b)); 
    return AtomicSymbol.elementToAtomicNumber(stringBuffer.toString());
  }
  
  void readFrequencies(Molecule paramMolecule) throws Exception {
    paramMolecule.removeFrequencies();
    String str = this.input.readLine();
    while (str.indexOf("frequencies") >= 0) {
      StringReader stringReader = new StringReader(str.substring(13));
      StreamTokenizer streamTokenizer = new StreamTokenizer(stringReader);
      Vector vector = new Vector();
      while (streamTokenizer.nextToken() != -1) {
        Frequency frequency = new Frequency();
        frequency.value = streamTokenizer.nval;
        vector.addElement(frequency);
      } 
      Frequency[] arrayOfFrequency = new Frequency[vector.size()];
      vector.copyInto(arrayOfFrequency);
      Vector3d[] arrayOfVector3d = new Vector3d[arrayOfFrequency.length];
      str = this.input.readLine();
      if (str != null && str.trim().startsWith("intensities"))
        str = this.input.readLine(); 
      byte b;
      for (b = 0; b < paramMolecule.getNumberAtoms(); b++) {
        str = this.input.readLine();
        StringReader stringReader1 = new StringReader(str);
        streamTokenizer = new StreamTokenizer(stringReader1);
        streamTokenizer.nextToken();
        streamTokenizer.nextToken();
        byte b1;
        for (b1 = 0; b1 < arrayOfFrequency.length; b1++) {
          arrayOfVector3d[b1] = new Vector3d();
          if (streamTokenizer.nextToken() == -2) {
            (arrayOfVector3d[b1]).x = streamTokenizer.nval;
          } else {
            throw new Exception("Error reading frequencies");
          } 
        } 
        str = this.input.readLine();
        stringReader1 = new StringReader(str);
        streamTokenizer = new StreamTokenizer(stringReader1);
        streamTokenizer.nextToken();
        streamTokenizer.nextToken();
        for (b1 = 0; b1 < arrayOfFrequency.length; b1++) {
          if (streamTokenizer.nextToken() == -2) {
            (arrayOfVector3d[b1]).y = streamTokenizer.nval;
          } else {
            throw new Exception("Error reading frequencies");
          } 
        } 
        str = this.input.readLine();
        stringReader1 = new StringReader(str);
        streamTokenizer = new StreamTokenizer(stringReader1);
        streamTokenizer.nextToken();
        streamTokenizer.nextToken();
        for (b1 = 0; b1 < arrayOfFrequency.length; b1++) {
          if (streamTokenizer.nextToken() == -2) {
            (arrayOfVector3d[b1]).z = streamTokenizer.nval;
          } else {
            throw new Exception("Error reading frequencies");
          } 
          arrayOfFrequency[b1].addVector(arrayOfVector3d[b1]);
        } 
      } 
      for (b = 0; b < arrayOfFrequency.length; b++)
        paramMolecule.addFrequency(arrayOfFrequency[b]); 
      for (b = 0; b < 15; b++) {
        str = this.input.readLine();
        if (str.indexOf("frequencies") >= 0)
          break; 
      } 
    } 
  }
}
