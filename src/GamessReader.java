import java.io.BufferedReader;
import java.io.Reader;
import java.io.StreamTokenizer;
import java.io.StringReader;
import java.util.Vector;

class GamessReader implements MoleculeReader {
  static final double angstromPerBohr = 0.529177249D;
  
  BufferedReader input;
  
  public GamessReader(Reader paramReader) { this.input = new BufferedReader(paramReader); }
  
  public void read(Molecule paramMolecule) throws Exception {
    while (this.input.ready()) {
      String str = this.input.readLine();
      if (str.indexOf("TOTAL ENERGY =") >= 0) {
        paramMolecule.energy = toEnergy(str);
        continue;
      } 
      if (str.indexOf("COORDINATES (BOHR)") >= 0) {
        str = this.input.readLine();
        readCoordinates(paramMolecule);
        continue;
      } 
      if (str.indexOf("FREQUENCIES IN CM") >= 0) {
        str = this.input.readLine();
        str = this.input.readLine();
        if (str.indexOf("*****") >= 0) {
          str = this.input.readLine();
          str = this.input.readLine();
          str = this.input.readLine();
          str = this.input.readLine();
          str = this.input.readLine();
        } 
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
      String str = this.input.readLine();
      if (str.trim().length() == 0)
        break; 
      Atom atom = new Atom();
      StringReader stringReader = new StringReader(str);
      StreamTokenizer streamTokenizer = new StreamTokenizer(stringReader);
      streamTokenizer.nextToken();
      if (streamTokenizer.nextToken() == -2) {
        atom.atomicNumber = (int)streamTokenizer.nval;
        if (atom.atomicNumber == 0)
          continue; 
      } else {
        throw new Exception("Error reading coordinates");
      } 
      atom.position = new Point3d();
      if (streamTokenizer.nextToken() == -2) {
        atom.position.x = streamTokenizer.nval * 0.529177249D;
      } else {
        throw new Exception("Error reading coordinates");
      } 
      if (streamTokenizer.nextToken() == -2) {
        atom.position.y = streamTokenizer.nval * 0.529177249D;
      } else {
        throw new Exception("Error reading coordinates");
      } 
      if (streamTokenizer.nextToken() == -2) {
        atom.position.z = streamTokenizer.nval * 0.529177249D;
      } else {
        throw new Exception("Error reading coordinates");
      } 
      paramMolecule.addAtom(atom);
    } 
  }
  
  void readFrequencies(Molecule paramMolecule) throws Exception {
    paramMolecule.removeFrequencies();
    String str = this.input.readLine();
    while (str.indexOf("FREQUENCY:") >= 0) {
      StringReader stringReader = new StringReader(str.substring(16));
      StreamTokenizer streamTokenizer = new StreamTokenizer(stringReader);
      Vector vector = new Vector();
      for (Frequency frequency = new Frequency(); streamTokenizer.nextToken() != -1; frequency = frequency1) {
        if (streamTokenizer.ttype == -3) {
          frequency.value = -frequency.value;
          streamTokenizer.nextToken();
        } 
        Frequency frequency1 = new Frequency();
        frequency1.value = streamTokenizer.nval;
        vector.addElement(frequency1);
      } 
      Frequency[] arrayOfFrequency = new Frequency[vector.size()];
      vector.copyInto(arrayOfFrequency);
      Vector3d[] arrayOfVector3d = new Vector3d[arrayOfFrequency.length];
      str = this.input.readLine();
      str = this.input.readLine();
      byte b;
      for (b = 0; b < paramMolecule.getNumberAtoms(); b++) {
        str = this.input.readLine();
        StringReader stringReader1 = new StringReader(str);
        streamTokenizer = new StreamTokenizer(stringReader1);
        streamTokenizer.nextToken();
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
        if (str.indexOf("FREQUENCY:") >= 0)
          break; 
      } 
    } 
  }
}


/* Location:              /home/xyz666/gausspy/Xvibs/xvibs.jar!/GamessReader.class
 * Java compiler version: 2 (46.0)
 * JD-Core Version:       1.0.7
 */