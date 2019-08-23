import java.io.BufferedReader;
import java.io.Reader;
import java.io.StreamTokenizer;
import java.io.StringReader;
import java.util.Vector;

class Gaussian98Reader implements MoleculeReader {
  BufferedReader input;
  
  public Gaussian98Reader(Reader paramReader) { this.input = new BufferedReader(paramReader); }
  
  public void read(Molecule paramMolecule) throws Exception {
    while (this.input.ready()) {
      String str = this.input.readLine();
      if (str.indexOf("SCF Done:") >= 0) {
        paramMolecule.energy = toEnergy(str);
        continue;
      } 
      if (str.indexOf("Standard orientation:") >= 0 || str.indexOf("Input orientation:") >= 0) {
        readCoordinates(paramMolecule);
        continue;
      } 
      if (str.indexOf("Harmonic frequencies") >= 0) {
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
    while (streamTokenizer.nextToken() != -1) {
      if (streamTokenizer.ttype == -2) {
        d = streamTokenizer.nval;
        break;
      } 
    } 
    if (streamTokenizer.ttype == -1)
      throw new Exception("Error reading energy"); 
    return d;
  }
  
  void readCoordinates(Molecule paramMolecule) throws Exception {
    paramMolecule.removeAtoms();
    String str = this.input.readLine();
    str = this.input.readLine();
    str = this.input.readLine();
    str = this.input.readLine();
    while (this.input.ready()) {
      str = this.input.readLine();
      if (str.indexOf("-----") >= 0)
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
    String str = this.input.readLine();
    str = this.input.readLine();
    for (str = this.input.readLine(); str.startsWith(" Frequencies --"); str = this.input.readLine()) {
      Vector vector = new Vector();
      StringReader stringReader = new StringReader(str.substring(15));
      StreamTokenizer streamTokenizer = new StreamTokenizer(stringReader);
      while (streamTokenizer.nextToken() != -1) {
        Frequency frequency = new Frequency();
        frequency.value = streamTokenizer.nval;
        vector.addElement(frequency);
      } 
      str = this.input.readLine();
      str = this.input.readLine();
      str = this.input.readLine();
      str = this.input.readLine();
      str = this.input.readLine();
      str = this.input.readLine();
      byte b;
      for (b = 0; b < paramMolecule.getNumberAtoms(); b++) {
        str = this.input.readLine();
        StringReader stringReader1 = new StringReader(str);
        streamTokenizer = new StreamTokenizer(stringReader1);
        streamTokenizer.nextToken();
        streamTokenizer.nextToken();
        for (byte b1 = 0; b1 < vector.size(); b1++) {
          Vector3d vector3d = new Vector3d();
          if (streamTokenizer.nextToken() == -2) {
            vector3d.x = streamTokenizer.nval;
          } else {
            throw new Exception("Error reading frequencies");
          } 
          if (streamTokenizer.nextToken() == -2) {
            vector3d.y = streamTokenizer.nval;
          } else {
            throw new Exception("Error reading frequencies");
          } 
          if (streamTokenizer.nextToken() == -2) {
            vector3d.z = streamTokenizer.nval;
          } else {
            throw new Exception("Error reading frequencies");
          } 
          ((Frequency)vector.elementAt(b1)).addVector(vector3d);
        } 
      } 
      for (b = 0; b < vector.size(); b++)
        paramMolecule.addFrequency((Frequency)vector.elementAt(b)); 
      str = this.input.readLine();
      str = this.input.readLine();
    } 
  }
}


/* Location:              /home/xyz666/gausspy/Xvibs/xvibs.jar!/Gaussian98Reader.class
 * Java compiler version: 2 (46.0)
 * JD-Core Version:       1.0.7
 */